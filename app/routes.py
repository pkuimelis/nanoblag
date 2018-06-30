from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'username' : 'petuhcloud'}
	posts = [
			{
				'author' : {'username' : 'Peter'},
				'body' : 'Nice day in PA today.'
			},
			{
				'author' : {'username' : 'Calvin'},
				'body' : 'Blockchain is the future!'
			}
		]
	return render_template('index.html', title='Home', user=user, posts=posts)
