###project/main/views.py

from flask import Flask,flash,render_template,session,url_for,Blueprint,redirect

main_blueprint = Blueprint('main',__name__)

@main_blueprint.route('/')
def mainpage():
	return render_template('main.html')

