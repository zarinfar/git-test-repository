from flask import Flask, make_response
from flask import redirect, abort, render_template
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard too guess string'


class Give_data(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')


class UserInfo(Form):
    first_name = StringField('username :')
    last_name = StringField('family :')
    phone_number = StringField('phone :')
    submit = SubmitField('Submit')

@app.route('/<name>')
def index(name):
    return 'hello %s' % name


@app.route('/')
def badrequest():
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


@app.route('/input_data_from_form/', methods=['GET', 'POST'])
# @app.route('/input_data_from_form/', methods=['POST'])
def input_data_from_form():
    name = None
    form = Give_data()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''

    return render_template('form.html', form=form, name=name)


@app.route('/user_info_input_data/', methods=['GET', 'POST'])
def user_info():
    form_user_info = UserInfo()

    first_name = form_user_info.first_name.data
    last_name = form_user_info.last_name.data
    phone_number = form_user_info.phone_number.data

    form_user_info.first_name.data = ''
    form_user_info.last_name.data = ''
    form_user_info.phone_number.data = ''
    #
    return render_template('UserInfo.html', form_user_info=form_user_info,
                           first_name=first_name,
                           last_name=last_name,
                           phone_number=phone_number)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
