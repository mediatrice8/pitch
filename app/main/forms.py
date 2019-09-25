from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required
 
class PitchForm(FlaskForm):
    
    content = TextAreaField('YOUR PITCH')
    submit = SubmitField('SUBMIT')

class CommentForm(FlaskForm):
    opinion = TextAreaField('WRITE COMMENT')
    submit = SubmitField('SUBMIT')
    
class CategoryForm(FlaskForm):
    name =  StringField('Category Name', validators=[Required()])
    submit = SubmitField('Create')
    
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
