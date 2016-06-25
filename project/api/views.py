from project import db
from flask import Flask,flash,render_template,session,url_for,Blueprint,make_response,jsonify,request
import json
api_blueprint = Blueprint('api',__name__)

@api_blueprint.route('/api/movies/')
def movie():
	if 't' not in request.args or 'y' not in request.args or len(request.args) != 2:
		result = {"error":"You must use Title and Year info to get results"}
		code = 400
		return make_response(jsonify(result),code)
	result = db.movies.find_one({"Title":request.args['t'],"Year":{'$regex': request.args['y']}},{'_id':0})
	

	if result:
		code = 200
		return make_response(jsonify(result),code)
	else:
		result = {"error":"Element does not exist"}
		code = 400
		return make_response(jsonify(result),code)
	