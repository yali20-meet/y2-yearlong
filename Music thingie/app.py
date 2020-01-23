from flask import Flask, render_template, request
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

@app.route('/FEEDBACK')
def feedback():
    
    return render_template("feedback.html")

if __name__ == '__main__':
    app.run(debug=True)