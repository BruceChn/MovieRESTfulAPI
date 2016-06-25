###project/main/views.py
from project import db
from flask import Flask,flash,render_template,session,url_for,Blueprint,redirect,request,make_response,jsonify
from project.main.forms import QueryForm
main_blueprint = Blueprint('main',__name__)

@main_blueprint.route('/',methods = ['GET','POST'])
def mainpage():
	form = QueryForm(request.form)
	if request.method == 'POST':
		if form.validate_on_submit():
			session['title'] = request.form['title']
			session['year'] = request.form['year']
	return render_template('main.html',form = form)
	
@main_blueprint.route('/query',methods = ['GET','POST'])
def query():
	result = {"error":"Element does not exist"}
	print request.form['title']
	result = db.movies.find_one({"Title":request.form['title'],"Year":{"$regex":request.form['year']}},{"_id":0})
	print result
	if result:
		code = 200
		return make_response(jsonify(result),code)
	else:
		result = {"error":"Element does not exist"}
		code = 400
		return make_response(jsonify(result),code)
	