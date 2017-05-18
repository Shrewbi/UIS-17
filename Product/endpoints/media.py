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





UPLOAD_FOLDER = '/folder/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif', 'mov', 'mp4', 'avi', 'mpeg'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@bp.route("/api/uploadfile", methods=['GET', 'POST'])
def upload_file():
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
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''