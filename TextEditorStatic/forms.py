from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField



class TextForm(FlaskForm):
	text_box = TextAreaField()
	validate = StringField()
	submit = SubmitField('Save')
class UploadForm(FlaskForm):
	submit = SubmitField('Choose File')
class Filepath(FlaskForm):
    submit = SubmitField('Script Compile')
	