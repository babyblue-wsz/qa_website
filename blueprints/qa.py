from flask import Blueprint,render_template

bp = Blueprint("qa",__name__,url_prefix="/")

@bp.route('/')
def login():
    return render_template("index.html")