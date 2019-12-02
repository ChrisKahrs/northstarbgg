from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class usernamesform(FlaskForm):
    usernames = StringField("Usernames", validators=[DataRequired()])
    password = StringField("Password", validators=[DataRequired()])
    sorter = SelectField("Sort", choices=[("alpha","Alpha"), ("rank","Rank")])
    submit = SubmitField("Submit")
