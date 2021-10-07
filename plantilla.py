from flask import Flask,request, render_template
app = Flask(__name__)

@app.route('/')

def index():
	return render_template("plantilla1.html")

app.run(host='0.0.0.0', port=5001, debug=True)