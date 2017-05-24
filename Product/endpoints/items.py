from flask import *
from helpers import *
from collections import defaultdict

bp = Blueprint('items', __name__)

@bp.route("/api/items", methods=['GET'])
def get_items():
    query = """
        select i.id, i.x_coordinate, i.y_coordinate, t.id, t.name,
            itf.id, itf.name, m.type, m.value
        from items i
        join templates t on i.template_id=t.id
        left join item_fields itf on i.id=itf.item_id
        left join media m on itf.media_id=m.id
    """
    rows = database.execute(query)

    # Reformat to hierarchic structure
    res = defaultdict(lambda: defaultdict(list))
    for row in rows:
        # Get values
        item_id = row[0]
        item_x = row[1]
        item_y = row[2]
        template_id = row[3]
        template_name = row[4]
        item_field_id = row[5]
        item_field_name = row[6]
        media_type = row[7]
        media_value = row[8]

        # Add to/update res
        res[item_id]["id"] = item_id

        res[item_id]["coordinates"] = {
            "x" : item_x,
            "y" : item_y
        }

        res[item_id]["template"] = {
            "id" : template_id,
            "name": template_name
        }

        if item_field_id:
            res[item_id]["fields"] += [{
                "id" : item_field_id,
                "name" : item_field_name,
                "type" : media_type,
                "value" : media_value
            }]

    # Done
    return jsonify(data=list(res.values()))

@bp.route("/api/items", methods=['POST'])
def create_item():
    # Get submit data
    data = request.get_json()
    template_id = data["template_id"]
    x_coordinate = data["x_coordinate"]
    y_coordinate = data["y_coordinate"]

    # Insert into db
    query = """
        insert into items(template_id, x_coordinate, y_coordinate)
        values({}, {}, {})
        returning id, template_id, x_coordinate, y_coordinate
    """.format(template_id, x_coordinate, y_coordinate)
    cursor = database.execute(query)

    # Prepare response
    row = cursor.fetchone()
    return jsonify(data={
        "id" : row[0],
        "template_id" : row[1],
        "x_coordinate" : row[2],
        "y_coordinate" : row[3]
    })

@bp.route("/api/items/<int:item_id>", methods=['DELETE'])
def delete_item(item_id):
    query = "delete from items where id = {}".format(item_id)
    database.execute(query)
    return jsonify(data=None)

@bp.route("/api/items/<int:item_id>/fields", methods=['POST'])
def add_item_field(item_id):
    # Get submit data
    data = request.get_json()
    name = data["name"]
    media_id = data["media_id"]

    # Insert into db
    query = """
        insert into item_fields(name, item_id, media_id)
        values('{}', {}, {})
        returning id, name, item_id, media_id
    """
    query = query.format(name, item_id, media_id)
    cursor = database.execute(query)
    row = cursor.fetchone()

    data={
        "id" : row[0],
        "name" : row[1],
        "item_id" : row[2],
        "media_id" : row[3]
    }

    # Get media info
    query = """
        select m.type, m.value
        from media m
        where m.id = {}
    """.format(data["media_id"])
    cursor = database.execute(query)
    row = cursor.fetchone()

    data["type"] = row[0]
    data["value"] = row[1]

    # Prepare response
    return jsonify(data=data)

@bp.route("/api/items/<int:item_id>/fields/<int:item_field_id>", methods=['DELETE'])
def delete_item_field(item_id, item_field_id):
    query = "delete from item_fields where id = {} and item_id = {}"
    query = query.format(item_field_id, item_id)
    database.execute(query)
    return jsonify(data=None)

@bp.route("/api/items/paths", methods=['GET'])
def get_paths():
    query = "select p.from_item_id, p.to_item_id from paths p"
    rows = database.execute(query)
    res = [{"from_item_id" : row[0], "to_item_id" : row[1] } for row in rows]
    return jsonify(data=res)

@bp.route("/api/items/paths", methods=['POST'])
def add_path():
    # Get input
    data = request.get_json()
    from_item_id = data["from_item_id"]
    to_item_id = data["to_item_id"]

    # Check doesn't already exist
    query = """
        select *
        from paths p
        where (p.from_item_id = {} and p.to_item_id = {})
            or (p.from_item_id = {} and p.to_item_id = {})
    """.format(from_item_id, to_item_id, to_item_id, from_item_id)
    cursor = database.execute(query)

    if cursor.rowcount > 0:
        return abort(400)

    # Insert
    query = """
        insert into paths(from_item_id, to_item_id)
        values ({}, {})
        returning from_item_id, to_item_id
    """
    query = query.format(from_item_id, to_item_id)
    cursor = database.execute(query)

    # Prepare response
    row = cursor.fetchone()
    return jsonify(data={
        "from_item_id" : row[0],
        "to_item_id" : row[1],
    })

@bp.route("/api/items/paths", methods=['DELETE'])
def delete_path():
    from_item_id = request.args.get("from_item_id")
    to_item_id = request.args.get("to_item_id")

    query = "delete from paths where from_item_id = {} and to_item_id = {}"
    query = query.format(from_item_id, to_item_id)
    cursor = database.execute(query)
    return jsonify(data=None)
