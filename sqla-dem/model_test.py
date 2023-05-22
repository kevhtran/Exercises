from unittest import TestCase
from datetime import datetime
from app import app
from models import db, User, Post, Tag, PostTag

# Use test database and don't clutter tests with SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_test'
app.config['SQLALCHEMY_ECHO'] = False

db.drop_all()
db.create_all()

class UserModelTestCase(TestCase):
    """Tests for model for User."""

    def setUp(self):
        """Clean up any existing data."""

        User.query.delete()
        DEFAULT_IMAGE_URL = 'https://p7.hiclipart.com/preview/596/856/933/pokemon-yellow-pokemon-red-and-blue-pokemon-mystery-dungeon-explorers-of-darkness-time-pikachu-ash-ketchum-pikachu-png.jpg'
        user = User(first_name="Patrick", last_name="Bateman", image_url=DEFAULT_IMAGE_URL)
        db.session.add(user)
        db.session.commit()

        self.user = user

    def tearDown(self):
        """Clean up any fouled transaction."""

        db.session.rollback()

    def test_first_name(self):
        user = User(first_name="Patrick", last_name="Bateman")
        self.assertEqual(user.first_name, "Patrick")

    def test_last_name(self):
        user = User(first_name="Patrick", last_name="Bateman")
        self.assertEqual(user.last_name, "Bateman")
    
    def test_url_default(self):
        DEFAULT_IMAGE_URL = 'https://p7.hiclipart.com/preview/596/856/933/pokemon-yellow-pokemon-red-and-blue-pokemon-mystery-dungeon-explorers-of-darkness-time-pikachu-ash-ketchum-pikachu-png.jpg'
        user = User(first_name="Patrick", last_name="Bateman", image_url=DEFAULT_IMAGE_URL)
        self.assertEqual(user.image_url, "https://p7.hiclipart.com/preview/596/856/933/pokemon-yellow-pokemon-red-and-blue-pokemon-mystery-dungeon-explorers-of-darkness-time-pikachu-ash-ketchum-pikachu-png.jpg")   
    def test_post(self):
        post = Post(title='Oh Honey', content='Miley Thee Cyrus', user_id=self.user.id, created_at=datetime.now)
        self.assertEqual(post.title, 'Oh Honey')
        self.assertEqual(post.content, 'Miley Thee Cyrus')
        self.assertEqual(post.user_id, self.user.id)
        self.assertEqual(post.created_at, datetime.now)

    def test_tags(self):
        tag = Tag(name='scary')
        db.session.add(tag)
        db.session.commit()
        self.assertEqual(tag.name, 'scary')
