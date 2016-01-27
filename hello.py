from flask import Flask
app=Flask(__name__)

@app.route('/<name>')
def index(name):
	return 'hello %s' %name 

@app.route('/<namea>')
def user(namea):
	return 'hello %s' %namea 










salammmmmmmmmmmmmmmmmmmm












if __name__=='__main__':
	app.run(debug=True)
