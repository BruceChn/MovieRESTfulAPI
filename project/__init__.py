#### project/__init.py

from flask import Flask,render_template
from pymongo import MongoClient


application = Flask(__name__)
application.config.from_pyfile('_config.py')
app = application
db = MongoClient('54.237.243.112:27017').mv

from project.api.views import api_blueprint
from project.main.views import main_blueprint

app.register_blueprint(api_blueprint)
app.register_blueprint(main_blueprint)

@app.errorhandler(404)
def not_found(error):
	return render_template('404.html'),404

