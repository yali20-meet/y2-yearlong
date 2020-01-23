from flask import Flask, render_template, request

from database import *

app = Flask(__name__)

@app.route('/')
def home():
    
    return render_template("home.html")

@app.route('/FLOWER')
def flower():
    
    return render_template("flower.html")

@app.route('/SUN')
def sun():
    
    return render_template("sun.html")

@app.route('/MOON')
def moon():
    
    return render_template("moon.html")

@app.route('/MOON2')
def moon2():
    
    return render_template("moon2.html")

@app.route('/LIGHTS')
def lights():
    
    return render_template("lights.html")

@app.route('/FEEDBACK' ,  methods=["GET" , "POST"])
def feedback():
	if request.method == "GET":
		return render_template("feedback.html")
	else:
		playlist = request.form["playlist"]
		feedback = request.form["feedback"]
		add_feed(playlist, feedback)
		return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True)