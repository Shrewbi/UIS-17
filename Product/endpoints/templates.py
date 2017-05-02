from flask import *
from helpers import *
from collections import defaultdict

bp = Blueprint('templates', __name__)

@bp.route("/api/templates", methods=['GET'])
def get_templates():
    # Run query
    query = """
        select t.id, t.name, tf.id, tf.name, m.type, m.value
        from templates t
        left join template_fields tf on t.id=tf.template_id
        left join media m on tf.media_id=m.id
    """
    rows = database.execute(query)

    # Reformat to hierarchic structure
    res = defaultdict(lambda: defaultdict(list))
    for row in rows:
        # Get values
        template_id = row[0]
        template_name = row[1]
        template_field_id = row[2]
        template_field_name = row[3]
        media_type = row[4]
        media_value = row[5]

        # Add to/update res
        res[template_id]["id"] = template_id
        res[template_id]["name"] = template_name
        if template_field_id:
            res[template_id]["fields"] += [{
                "id" : template_field_id,
                "name" : template_field_name,
                "type" : media_type,
                "value" : media_value
            }]

    # Done
    return jsonify(data=list(res.values()))

@bp.route("/api/templates", methods=['POST'])
def create_template():
    # Get submit data
    data = request.get_json()
    name = data["name"]

    # Insert into db
    query = "insert into templates(name) values('{}') returning id, name"
    query = query.format(name)
    cursor = database.execute(query)

    # Prepare response
    row = cursor.fetchone()
    return jsonify(data={"id" : row[0], "name" : row[1]})

@bp.route("/api/templates/<int:template_id>", methods=['DELETE'])
def delete_template(template_id):
    query = "delete from templates where id = {}".format(template_id)
    database.execute(query)
    return jsonify(data=None)

@bp.route("/api/templates/<int:template_id>/fields", methods=['POST'])
def add_template_field(template_id):
    # Get submit data
    data = request.get_json()
    name = data["name"]
    media_id = data["media_id"]

    # Insert into db
    query = """
        insert into template_fields(name, template_id, media_id)
        values('{}', '{}', '{}')
        returning id, name, template_id, media_id
    """
    query = query.format(name, template_id, media_id)
    cursor = database.execute(query)

    # Prepare response
    row = cursor.fetchone()
    return jsonify(data={"id" : row[0], "name" : row[1], "template_id" : row[2], "media_id" : row[3]})

@bp.route("/api/templates/<int:template_id>/fields/<int:template_field_id>", methods=['DELETE'])
def delete_template_field(template_id, template_field_id):
    query = "delete from template_fields where id = {} and template_id = {}"
    query = query.format(template_field_id, template_id)
    database.execute(query)
    return jsonify(data=None)
