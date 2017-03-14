from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, DecimalField, TextAreaField, FileField, SelectField, validators


class profileForm(Form):
    firstname = StringField(
        'firstname', [validators.Required(message="This field cannot be empty"), validators.Length(min=4, max=25)])
    lastname = StringField(
        'lastname', [validators.Required(message="This field cannot be empty"), validators.Length(min=4, max=25)])
    age = StringField(
        'age', [validators.Required(message="This field cannot be empty")])
    image = FileField('upload image')
    sex = SelectField('Sex', choices=[('male', 'male'), ('female', 'female')])
    username = StringField('username', [validators.Required()])
