from flask import *
from helpers import *

bp = Blueprint('site', __name__)

@bp.route("/")
def home():
    return render_template("index.html")

@bp.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if credentials_valid(username, password):
            session['logged_in'] = True
            return redirect('/')
        else:
            error = "Invalid credentials"
    return render_template('login.html', error=error)

@bp.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect('/')

@bp.route("/admin/users")
def admins():
    return render_template("admins.html", is_admin_page=True)

@bp.route("/admin/map")
def maps():
    return render_template("manage.html", is_manage_page=True)

@bp.route("/uploadfile")
def uploadfile():
    return render_template("uploadfile.html", is_manage_page=True)

@bp.route("/admin/uploadmap")
def uploadmap():
    return render_template("uploadmap.html", is_upload_page=True)