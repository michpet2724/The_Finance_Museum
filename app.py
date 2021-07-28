# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, render_template, request
from datetime import datetime
# from model import getImageUrlFrom
import os

# -- Initialization section --
app = Flask(__name__)


app.config['GIPHY_KEY'] = "HPPlTs8kpN7jMHde8sQy9y0MYEGir6fL"
KEY = app.config['GIPHY_KEY']

# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", time = datetime.now())

@app.route('/yourgif', methods = ['GET', 'POST'])
def display_gif():
    print(request.form)
    gif = request.form['gifchoice']
    # url = getImageUrlFrom(gif, KEY)
    # return render_template('yourgif.html', url = url)
    return "I am alive"