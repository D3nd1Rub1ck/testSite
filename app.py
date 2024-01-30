from flask import Flask, render_template, request, make_response, send_file
#import json
from jinja2 import Environment, PackageLoader, select_autoescape

app = Flask(__name__)

@app.route('/')
def home():
    items = []
    items.append({ 
        'price': 100,
        'grade': 5.4
    })
    items.append({ 
        'price': 234,
        'grade': 6.1
    })
    return render_template("index.html", data=items)

@app.route('/f')
def f():
    return "<a href=\"/start\">something went wrong, contact server admin</a>"

@app.route('/<n>')
def render_test(n):
    return f"<h1><h1>{n}</h1></h1>"
    
if __name__ == "__main__":
    app.run(debug=True)