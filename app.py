from flask import Flask, url_for, render_template
from markupsafe import escape
app = Flask(__name__)
name = 'Grey Li'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]



@app.route('/')
def index():
	return render_template('index.html', name=name, movies=movies)

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
