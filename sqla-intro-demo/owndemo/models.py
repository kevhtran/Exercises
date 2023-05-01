from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)


#MODELS GO BELOW:

# class Pet:

#     kyle = Pet(name='Kyle The Chicken', species='Chicken')
#     kyle.name="Kyle The Rooste"

#     kyle.getOffspring()