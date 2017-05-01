from flask import *
import database
import hashlib

app = Flask(__name__)
app.debug = True
app.secret_key = "314"

@app.route("/")
def home():
    return render_template("map.html")

@app.route("/test")
def test():
    query = "select t.id, t.body from test t"
    rows = database.execute(query)
    res = [{"id" : r[0], "body" : r[1]} for r in rows]
    return jsonify(data=res)

@app.route('/login', methods=['GET', 'POST'])
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

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect('/')

@app.route("/admin/users")
def admins():
    return render_template("admins.html", is_admin_page=True)

@app.route("/api/admins", methods=['GET'])
def get_admins():
    query = "select a.id, a.username from admins a"
    rows = database.execute(query)
    res = [{"id" : r[0], "username" : r[1]} for r in rows]
    return jsonify(data=res)

@app.route("/api/admins", methods=['POST'])
def create_admin():
    # Get submit data
    data = request.get_json()
    username = data["username"]
    password_hash = hash_password(data["password"])

    # Insert into db
    query = "insert into admins(username, password_hash) values('{}', '{}') returning id, username"
    query = query.format(username, password_hash)
    cursor = database.execute(query)

    # Prepare response
    row = cursor.fetchone()
    return jsonify(data={"id" : row[0], "username" : row[1]})

@app.route("/api/admins/<int:admin_id>", methods=['DELETE'])
def delete_admin(admin_id):
    query = "delete from admins where id = {}".format(admin_id)
    database.execute(query)
    return jsonify(data=None)

def credentials_valid(username, password):
    query = """
        select *
        from admins a
        where a.username = '{}'
        and   a.password_hash = '{}'
    """
    query = query.format(username, hash_password(password))
    cursor = database.execute(query)
    rows = cursor.fetchall()
    return len(rows) > 0

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()
