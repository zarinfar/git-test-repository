from flask import Flask, make_response
from flask import redirect, abort, render_template
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required




@app.route('/<name>')
def index(name):
    return 'hello %s' % name



@app.route('/')
def bad_request():
    return '<h1>bad request</h1>', 400


@app.route('/response/')
def response():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '10')
    return response


@app.route('/redirect/')
def redirect2google():
    return redirect('http://www.google.com')


def load_user(id):
    return None


@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>hello %s</h1>' % user.name


@app.route('/rendertemplate/')
def rendertemplate():
    return render_template('index.html')


@app.route('/render_template_user/<name>')
def render_template_user(name):
    return render_template('user.html', name=name)


@app.errorhandler(404)
def page_not_found(error_this_name_is_optional):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(error_this_name_is_optional):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)
