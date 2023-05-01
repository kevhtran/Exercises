from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField

class AddSnackForm(FlaskForm):
    """form for adding snacks."""
    name = StringField("Snack Name")
    price = FloatField("Price in USD")
    is_healthy = BooleanField("This is a healthy snack")

class NewEmployeeForm(FlaskForm):
    
    name = StringField("employee name")
    state = StringField('state')
    dept_code = SelectField('department code')