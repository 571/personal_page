import time
from flask import Flask

app = Flask(__name__)

@app.route('/')
def get_main():
	return """<h1> Qinyun Wang's Page </h1>
	<br/>
	<p> This personal page is under construction. </p>
	<p> Please wait for further information. </p>"""

@app.route('/time')
def get_current_time():
	return {'time': time.time()}

@app.route('/source')
def get_source():
	return "https://blog.miguelgrinberg.com/post/how-to-create-a-react--flask-project"
