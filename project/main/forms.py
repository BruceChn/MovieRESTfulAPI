from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class QueryForm(Form):
	title = StringField("name",validators = [DataRequired()])
	year = StringField("year",validators = [DataRequired()])