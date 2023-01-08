from flask import Blueprint, render_template
from wiki import name, image, status, days

ferrari = Blueprint(__name__, "ferrari")

@ferrari.route("/")
def home():
    return render_template("index.html", name=name, image=image, status=status, days=days)