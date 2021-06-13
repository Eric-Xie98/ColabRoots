from flask import Flask
from markupsafe import escape
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/hello/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"


@app.route("/testing")
def testing():
    return "<h1>Hello, World!</h1>"

@app.route("/template")
def my_template():
    return render_template('my_template.html', name = "maple", items = range(1, 100))