from flask import Flask, url_for
from markupsafe import escape
app = Flask(__name__)

@app.route('/test')
def hello():
    return 'Welcome to my Watchlist!'

@app.route('/user/<name>')
def user_name(name):
	return f'User: my name is who {escape(name)}'


@app.route('/user/test')
def whatever():
	print(url_for('user_name', name='petter'))
	print(url_for('hello', name='hihihi'))		
	print(url_for('hello', num=3))
	return 'Test page'
