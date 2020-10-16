from flask import render_template, url_for, request, redirect, flash
from app import app

@app.route("/index")
@app.route("/")
def index():
    title = "Index"
    return render_template("index.html", title=title)