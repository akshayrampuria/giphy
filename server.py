from flask import Flask, render_template, request
import requests, json

app = Flask(__name__)
HOST = 'http://api.giphy.com'
PATH = '/v1/gifs/search'
API_KEY = 'dc6zaTOxFJmzC'

@app.route('/')
def search():
	return render_template('search.html')

@app.route('/results', methods = ['POST'])
def results():
	
	params = {}
	params['q'] = request.form['query']
	params['fmt'] = 'json'
	params['api_key'] = API_KEY

	r = requests.get(HOST + PATH, params=params)
	gif_urls = []
	if r.text == ' \n\n':
		return "Sorry, no GIF's were found."
	else:
		data = json.loads(r.text)['data']
		for url in data:
			gif_urls.append(url['images']['fixed_width']['url'])

	return render_template('results.html', data=gif_urls)	
	

app.debug = True	
app.run()