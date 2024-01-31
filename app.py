from flask import Flask, render_template, request, make_response, send_file
#import json
from jinja2 import Environment, PackageLoader, select_autoescape

app = Flask(__name__)

@app.route('/')
def home():
    items = []
    items.append({
        'productId': 0,
        'price': 100,
        'grade': 5.4
    })
    items.append({ 
        'productId': 1,
        'price': 234,
        'grade': 6.1
    })
    items.append({ 
        'productId': 2,
        'price': 391,
        'grade': 2.1
    })
    items.append({ 
        'productId': 3,
        'price': 567,   
        'grade': 9.1
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