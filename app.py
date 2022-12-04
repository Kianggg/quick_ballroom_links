import os

from flask import Flask, render_template, request, url_for

# from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/dances", methods=["GET", "POST"])
def dances():
    if request.method == "POST":
        if request.form.get("figure"):
            return render_template("figure.html", figure_name=request.form.get("figure"))
        elif request.form.get("syllabus"):
            destination = request.form.get("syllabus") + ".html"
            return render_template(f"syllabi/{destination}")
        else:
            return render_template("dances.html")
    else:
        return render_template("dances.html")

@app.route("/entries", methods=["GET", "POST"])
def entries():
    return render_template("entries.html")

@app.route("/ycn", methods=["GET", "POST"])
def ycn():
    return render_template("ycn.html")