from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE_URL = 'https://p7.hiclipart.com/preview/596/856/933/pokemon-yellow-pokemon-red-and-blue-pokemon-mystery-dungeon-explorers-of-darkness-time-pikachu-ash-ketchum-pikachu-png.jpg'


class User (db.Model):
    "site user"
    __tablename__ = "users"

    def __repr__(self):
        "show info"
        u = self
        return f"<User {u.id} {u.first_name} {u.last_name}>"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE_URL)

def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)
