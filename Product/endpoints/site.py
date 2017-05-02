from flask import *
from helpers import *

bp = Blueprint('site', __name__)

@bp.route("/")
def home():
    return render_template("map.html")

@bp.route("/test")
def test():
    query = "select t.id, t.body from test t"
    rows = database.execute(query)
    res = [{"id" : r[0], "body" : r[1]} for r in rows]
    return jsonify(data=res)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if credentials_valid(username, password):
            session['logged_in'] = True
            print("wow")
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