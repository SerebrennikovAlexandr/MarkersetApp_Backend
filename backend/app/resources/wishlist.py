from flask_restful import Resource
from app.models import User, Marker
from flask import jsonify
from app.database import db
from app.parsers import post_wishlist_parser
from flask_jwt_extended import jwt_required, get_jwt_identity


class WishlistApi(Resource):
    @jwt_required
    def get(self):
        user_id = get_jwt_identity()
        user = db.session.query(User).get_or_404(user_id)
        marker_list = user.wished_markers
        res = []
        for marker in marker_list:
            res.append(marker.to_dict())
        return jsonify({'status': 'OK', 'result': res})

    @jwt_required
    def post(self):
        user_id = get_jwt_identity()
        args = post_wishlist_parser.parse_args()
        user = db.session.query(User).get_or_404(user_id)

        if args['added_markers'] is not None:
            for id in args['added_markers']:
                marker = db.session.query(Marker).get_or_404(id)
                user.wished_markers.append(marker)

        if args['deleted_markers'] is not None:
            for id in args['deleted_markers']:
                marker = db.session.query(Marker).get_or_404(id)
                if marker in user.wished_markers:
                    user.wished_markers.remove(marker)

        db.session.commit()
        return jsonify({'status': 'OK'})
