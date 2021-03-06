from flask import *
from helpers import *
import os
import errno

bp = Blueprint('media', __name__)

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'static/media')
STATIC_FOLDER = os.path.join(os.getcwd(), 'static')
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif', 'mov', 'mp4', 'avi', 'mpeg'])
ALLOWED_EXTENSIONS_IMG = set(['png', 'jpg', 'jpeg', 'gif'])
ALLOWED_EXTENSIONS_VID = set(['mov', 'mp4'])

def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

def file_extension(filename):
    return filename.rsplit('.', 1)[1].lower()

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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

    if mtype == "text":
        # Insert into db
        query = "INSERT INTO media(type, value) VALUES('{}', '{}') returning id, type, value"
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

@bp.route("/api/upload_file", methods=['POST'])
def upload_file():
    make_sure_path_exists(UPLOAD_FOLDER)
    # check if the post request has the file part
    if 'filedata' not in request.files:
        print("File upload failed, no filedata in POST request.")
        return abort(400)
    file = request.files['filedata']
    # if user does not select file, browser also // ? - Mikkel
    # submit a empty part without filename
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        fileext = file_extension(file.filename)
        if fileext in ALLOWED_EXTENSIONS_IMG:
            media_type = "image"
        elif fileext in ALLOWED_EXTENSIONS_VID:
            media_type = "video"
        query = "insert into media(type, value) values('{}', 'NULL') returning id, type, value"
        query = query.format(media_type)
        cursor = database.execute(query)
        row = cursor.fetchone()
        givenid = row[0]
        filename = str(givenid) + '.' + str(fileext)
        file.save(os.path.join(UPLOAD_FOLDER, filename))

        query = "update media set value = '{}' where id = '{}' returning id, type, value"
        query = query.format(filename, givenid)
        cursor = database.execute(query)
        row = cursor.fetchone()
        return jsonify(data={"media": { "id": row[0] }})

    return abort(400)

@bp.route("/api/upload_map", methods=['POST'])
def upload_map():
    # check if the post request has the file part
    #if 'filedata' not in request.files:
    if 'file' not in request.files: # To be compatible with standard HTTPRequests
        print("Map upload failed, no filedata in POST request.")
        return abort(400)
    #file = request.files['filedata']
    file = request.files['file'] # To be compatible with standard HTTPRequests
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        fileext = file_extension(file.filename)
        if fileext != 'png':
            print("Map must be a .png format image.")
            return abort(400)
        file.save(os.path.join(STATIC_FOLDER, "map.png"))
        #return jsonify(data=None)
        return redirect("..") # To be compatible with standard HTTPRequests

    return abort(400)
