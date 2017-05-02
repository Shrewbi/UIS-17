from flask import *
import endpoints.site
import endpoints.admins
import endpoints.media
import endpoints.templates

app = Flask(__name__, static_url_path = "/static", static_folder = "static")
app.debug = True
app.secret_key = "314"

app.register_blueprint(endpoints.site.bp)
app.register_blueprint(endpoints.admins.bp)
app.register_blueprint(endpoints.media.bp)
app.register_blueprint(endpoints.templates.bp)
