from flask import *
from helpers import *

bp = Blueprint('admins', __name__)

@bp.route("/api/admins", methods=['GET'])
def get_admins():
    query = "select a.id, a.username from admins a"
    rows = database.execute(query)
    res = [{"id" : r[0], "username" : r[1]} for r in rows]
    return jsonify(data=res)

@bp.route("/api/admins", methods=['POST'])
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

@bp.route("/api/admins/<int:admin_id>", methods=['DELETE'])
def delete_admin(admin_id):
    query = "delete from admins where id = {}".format(admin_id)
    database.execute(query)
    return jsonify(data=None)
