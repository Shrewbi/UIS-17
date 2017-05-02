from flask import *
import endpoints.site
import endpoints.admins
import endpoints.media
import endpoints.templates

app = Flask(__name__)
app.debug = True
app.secret_key = "314"

app.register_blueprint(endpoints.site.bp)
app.register_blueprint(endpoints.admins.bp)
app.register_blueprint(endpoints.media.bp)
app.register_blueprint(endpoints.templates.bp)

#
# GET /api/items
#
# POST /api/items (template_id, x_coordinate, y_coordinate)
#
# POST /api/items/id/fields (name, media_id)
#
# DELETE /api/items/id/fields/id
#
# DELETE /api/items/id
#
# GET /api/items/paths
#
# POST /api/items/paths from_item_id, to_item_id
#
# DELETE /api/items/paths/id
