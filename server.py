from flask import Flask

app = Flask(__name__)

@app.route('/')
def search():
	return "Hi, I work! YAY!"

app.debug = True	
app.run()