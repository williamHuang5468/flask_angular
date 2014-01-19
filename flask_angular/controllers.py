from flask import render_template
from flask_angular import app

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def angular(path):
	return render_template('index.html')