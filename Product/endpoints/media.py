from flask import *
from helpers import *

bp = Blueprint('media', __name__)

@bp.route("/api/media", methods=['GET'])
def get_media():
    query = "select m.id, m.type, m.value from media m"
    rows = database.execute(query)
    res = [{"id" : r[0], "type" : r[1], "value" : r[2]} for r in rows]
    return jsonify(data=res)

@bp.route("/api/media", methods=['POST'])
def create_media():
    # Get submit data
    data = request.get_json()
    mtype = data["type"]
    value = data["value"]

    # Check it's a valid media type
    if mtype != "text":
        return abort(400)

    # Insert into db
    query = "insert into media(type, value) values('{}', '{}') returning id, type, value"
    query = query.format(mtype, value)
    cursor = database.execute(query)

    # Prepare response
    row = cursor.fetchone()
    return jsonify(data={"id" : row[0], "type" : row[1], "value" : row[2]})

@bp.route("/api/media/<int:media_id>", methods=['DELETE'])
def delete_media(media_id):
    query = "delete from media where id = {}".format(media_id)
    database.execute(query)
    return jsonify(data=None)
