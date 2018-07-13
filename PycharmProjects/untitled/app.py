from flask import Flask, render_template, request
from datetime import date
import tkinter
from tkinter import messagebox

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/', methods=['POST'])
def login():
    x = set()
    a = []
    mtkid = request.form['mtkid']
    print(mtkid)
    processed_text = mtkid.upper()
    today = str(date.today())
    print(today)
    f = open(today, "a+")
    f.write(mtkid + "\n")
    f.close()
    return ('Thank you for choosing the dates!')

if __name__=='__main__':
    app.run()