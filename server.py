from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def search():
	return render_template('search.html')

@app.route('/results', methods = ['POST'])
def results():
	return "GIF to search:" + request.form['query']

app.debug = True	
app.run()