from flask_restful import Resource
from app.models import User, Marker
from flask import jsonify
from app.database import db
from hashlib import md5
from flask_jwt_extended import jwt_required, get_jwt_identity


class WishlistHashApi(Resource):
    @jwt_required
    def get(self):
        user_id = get_jwt_identity()
        user = db.session.query(User).get_or_404(user_id)
        marker_list = user.wished_markers
        s = ""
        for marker in marker_list:
            s += repr(marker)
        res = md5(s.encode("utf-8")).hexdigest()
        return jsonify({'status': 'OK', 'result': res})
