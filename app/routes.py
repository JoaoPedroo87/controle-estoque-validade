from flask import Blueprint, render_template, request, redirect

routes_bp = Blueprint("routes", __name__)

@routes_bp.route("/")
def index():
    return render_template("index.html")
@routes_bp.route("/add", methods=["POST"])
def add():
    name = request.form["name"]
    batch = request.form["batch"]
    quantity = request.form["quantity"]
    expiration_date = request.form["expiration_date"]
    
    return redirect("/")
