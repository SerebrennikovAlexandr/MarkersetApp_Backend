from flask_restful import Resource
from app.models import User, Marker
from flask import jsonify
from app.database import db
from hashlib import md5


class MarkerHashApi(Resource):
    def get(self):
        marker_list = db.session.query(Marker).all()
        marker_list = sorted(marker_list, key=Marker.by_brand_series_key)
        s = ""
        for marker in marker_list:
            s += repr(marker)
        res = md5(s.encode("utf-8")).hexdigest()
        return jsonify({'status': 'OK', 'result': res})
