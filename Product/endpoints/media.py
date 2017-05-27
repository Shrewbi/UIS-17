from flask import *
from helpers import *
import os
import errno

bp = Blueprint('media', __name__)

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'media')
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif', 'mov', 'mp4', 'avi', 'mpeg'])
ALLOWED_EXTENSIONS_IMG = set(['png', 'jpg', 'jpeg', 'gif'])
ALLOWED_EXTENSIONS_VID = set(['mov', 'mp4', 'avi', 'mpeg'])

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



@bp.route("/api/uploadfile", methods=['GET', 'POST'])
def upload_file():
    make_sure_path_exists(UPLOAD_FOLDER)
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
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
            return jsonify(data={"id" : row[0], "type" : row[1], "value" : row[2]})
            '''
            return redirect(url_for('uploaded_file',
                                    filename=filename))'''
                                    
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''