from unittest import TestCase
from datetime import datetime
from app import app
from models import db, User, Post

# Use test database and don't clutter tests with SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_test'
app.config['SQLALCHEMY_ECHO'] = False

app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

db.drop_all()
db.create_all()

class UsersTestCase(TestCase):
    """Tests for views for Pets."""

    def setUp(self):
        """Add sample user."""

        User.query.delete()
        DEFAULT_IMAGE_URL = 'https://p7.hiclipart.com/preview/596/856/933/pokemon-yellow-pokemon-red-and-blue-pokemon-mystery-dungeon-explorers-of-darkness-time-pikachu-ash-ketchum-pikachu-png.jpg'
        user = User(first_name="Patrick", last_name="Bateman", image_url=DEFAULT_IMAGE_URL)
        db.session.add(user)
        db.session.commit()
        self.user = user

    def tearDown(self):
        """Clean up any fouled transaction."""

        db.session.rollback()

    def test_home_redirect(self):
        with app.test_client() as client:
            resp = client.get("/", follow_redirects=True)
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
    
    def test_users_page(self):
        with app.test_client() as client:
            resp = client.get("/users")
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('Patrick', html)

    def test_id_page(self):
        with app.test_client() as client:
            resp = client.get(f"/users/{self.user.id}")
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1>Patrick Bateman</h1>', html)
    
    def test_add_user(self):
        with app.test_client() as client:
            d = {"first_name":"Nancy", "last_name":"Drew", "image_url":""}
            resp = client.post("/users/new", data=d, follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Nancy Drew', html)
    
    def test_delete_user(self):
        with app.test_client() as client:
            d = {"first_name":self.user.first_name, "last_name":self.user.last_name, "image_url":self.user.image_url}
            resp = client.post(f"/users/{self.user.id}/delete", data=d, follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertNotIn('Patrick', html)

    def test_add_post(self):
        with app.test_client() as client:
            d = {'title':'Oh Bother', 'content':'Winnie thee Pooh', 'user':self.user, 'user_id':self.user.id, 'created_at':datetime.now()}
            resp = client.post(f"/users/{self.user.id}/posts/new", data=d, follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Oh Bother', html)
    # /users/<int:user_id>/posts/new

    # /posts/<int:post_id>/delete
