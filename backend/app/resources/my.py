from flask_restful import Resource
from app.models import User, Marker
from flask import jsonify
from app.database import db
from app.parsers import post_my_parser
from flask_jwt_extended import jwt_required, get_jwt_identity


class MyApi(Resource):
    @jwt_required
    def get(self):
        user_id = get_jwt_identity()
        user = db.session.query(User).get_or_404(user_id)
        marker_list = user.owned_markers
        marker_list = sorted(marker_list, key=Marker.by_brand_series_key)
        res = []
        for marker in marker_list:
            res.append(marker.to_dict())
        return jsonify({'status': 'OK', 'result': res})

    @jwt_required
    def post(self):
        user_id = get_jwt_identity()
        args = post_my_parser.parse_args()
        user = db.session.query(User).get_or_404(user_id)

        if args['added_markers'] is not None:
            for id in args['added_markers']:
                marker = db.session.query(Marker).get_or_404(id)
                user.owned_markers.append(marker)

        if args['deleted_markers'] is not None:
            for id in args['deleted_markers']:
                marker = db.session.query(Marker).get_or_404(id)
                if marker in user.owned_markers:
                    user.owned_markers.remove(marker)

        db.session.commit()
        return jsonify({'status': 'OK'})
