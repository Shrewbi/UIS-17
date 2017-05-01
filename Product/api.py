from flask import *
import database

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

def credentials_valid(username, password):
    return username == "hey"
