from unittest import TestCase

from app import app
from models import db, User

# Use test database and don't clutter tests with SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_test'
app.config['SQLALCHEMY_ECHO'] = False

db.drop_all()
db.create_all()

class UserModelTestCase(TestCase):
    """Tests for model for User."""

    def setUp(self):
        """Clean up any existing pets."""

        User.query.delete()

    def tearDown(self):
        """Clean up any fouled transaction."""

        db.session.rollback()

    def test_first_name(self):
        user = User(first_name="Patrick", last_name="Bateman")
        self.assertEquals(user.first_name, "Patrick")

    def test_last_name(self):
        user = User(first_name="Patrick", last_name="Bateman")
        self.assertEquals(user.last_name, "Bateman")
    
    def test_url_default(self):
        DEFAULT_IMAGE_URL = 'https://p7.hiclipart.com/preview/596/856/933/pokemon-yellow-pokemon-red-and-blue-pokemon-mystery-dungeon-explorers-of-darkness-time-pikachu-ash-ketchum-pikachu-png.jpg'
        user = User(first_name="Patrick", last_name="Bateman", image_url=DEFAULT_IMAGE_URL)
        self.assertEquals(user.image_url, "https://p7.hiclipart.com/preview/596/856/933/pokemon-yellow-pokemon-red-and-blue-pokemon-mystery-dungeon-explorers-of-darkness-time-pikachu-ash-ketchum-pikachu-png.jpg")   
    