from flask import Flask , make_response
app=Flask(__name__)

@app.route('/<name>')
def index(name):
	return 'hello %s' %name 

@app.route('/')
def badrequest():
	return '<h1>bad request</h1>',400

@app.route('/response/')
def response():	
	response=make_response('<h1>This document carries a cookie!</h1>')
	response.set_cookie('answer','10')
	return response

if __name__=='__main__':
	app.run(debug=True)
