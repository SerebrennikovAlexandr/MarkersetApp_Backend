from flask_restful import Resource
from app.models import Cart, User, Marker
from flask import jsonify
from app.database import db
from app.parsers import post_cart_parser, put_cart_parser, delete_cart_parser
from flask_jwt_extended import jwt_required, get_jwt_identity


class CartApi(Resource):
    @jwt_required
    def get(self):
        user_id = get_jwt_identity()
        user = db.session.query(User).get_or_404(user_id)
        res = []
        carts = user.cart_markers

        for cart in carts:
            marker_dict = db.session.query(Marker).get(cart.Marker_id).to_dict()
            if cart.Amount is not None:
                marker_dict['amount'] = cart.Amount
            res.append(marker_dict)

        return jsonify({'status': 'OK', 'result': res})

    @jwt_required
    def post(self):
        user_id = get_jwt_identity()
        args = post_cart_parser.parse_args()
        user = db.session.query(User).get_or_404(user_id)
        marker = db.session.query(Marker).get_or_404(args['marker_id'])

        cart = Cart(
            User_id=user_id,
            Marker_id=args['marker_id']
        )
        if args['amount'] is not None:
            cart.Amount = args['amount']

        db.session.add(cart)
        user.cart_markers.append(cart)
        marker.carts.append(cart)
        db.session.commit()
        return jsonify({'status': 'OK'})

    @jwt_required
    def put(self):
        user_id = get_jwt_identity()
        args = put_cart_parser.parse_args()
        user = db.session.query(User).get_or_404(user_id)
        for cart in user.cart_markers:
            if cart.Marker_id == args['marker_id']:
                cart.Amount = args['amount']
                db.session.add(cart)
                db.session.commit()
                break
        return jsonify({'status': 'OK'})

    @jwt_required
    def delete(self):
        user_id = get_jwt_identity()
        args = delete_cart_parser.parse_args()
        user = db.session.query(User).get_or_404(user_id)
        for cart in user.cart_markers:
            if cart.Marker_id == args['marker_id']:
                db.session.delete(cart)
                break

        db.session.commit()
        return jsonify({'status': 'OK'})
