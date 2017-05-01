from flask import *
import database

app = Flask(__name__)
app.debug = True

@app.route("/test")
def test():
    query = "select t.id, t.body from test t"
    rows = database.execute(query)
    res = [{"id" : r[0], "body" : r[1]} for r in rows]
    return jsonify(data=res)
