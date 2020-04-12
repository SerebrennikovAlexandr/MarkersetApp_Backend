from flask_restful import Resource
from app.models import Marker
from flask import jsonify
from app.parsers import get_marker_parser, post_marker_parser, put_marker_parser, delete_marker_parser
from app.database import db
from flask_jwt_extended import jwt_required


class MarkerApi(Resource):
    def get(self):
        args = get_marker_parser.parse_args()
        if args['id'] is not None:
            return jsonify({'status': 'OK', 'result': db.session.query(Marker).get_or_404(args['id']).to_dict()})

        elif args['hex'] is not None:
            marker_list = db.session.query(Marker).filter(Marker.Hex.like(args['hex'])).all()

        elif args['brand'] is not None:
            marker_list = db.session.query(Marker).filter(Marker.Brand.like(args['brand'])).all()

        elif args['series'] is not None:
            marker_list = db.session.query(Marker).filter(Marker.Series.like(args['series'])).all()

        elif args['full_name'] is not None:
            marker_list = db.session.query(Marker).filter(Marker.FullName.like(args['full_name'])).all()

        elif args['color_group_full_name'] is not None:
            marker_list = db.session.query(Marker).filter(Marker.ColorGroupFullName.like(args['color_group_full_name'])).all()

        else:
            marker_list = db.session.query(Marker).all()

        marker_list = sorted(marker_list, key=Marker.by_brand_series_key)
        res = []
        for marker in marker_list:
            res.append(marker.to_dict())
        return jsonify({'status': 'OK', 'result': res})

    @jwt_required
    def post(self):
        args = post_marker_parser.parse_args()
        marker = Marker(
            Hex=args['hex'],
            Brand=args['brand'],
            Series=args['series'],
            FullName=args['full_name'],
            ShortName=args['short_name'],
            ColorGroupFullName=args['color_group_full_name']
        )
        if args['color_group'] is not None:
            marker.ColorGroup = args['color_group']
        db.session.add(marker)
        db.session.commit()
        return jsonify({'status': 'OK', 'result': marker.to_dict()})

    @jwt_required
    def put(self):
        args = put_marker_parser.parse_args()
        marker = db.session.query(Marker).get_or_404(args['id'])

        if args['hex'] is not None:
            marker.Hex = args['hex']

        if args['brand'] is not None:
            marker.Brand = args['brand']

        if args['series'] is not None:
            marker.Series = args['series']

        if args['color_group'] is not None:
            marker.ColorGroup = args['color_group']

        if args['full_name'] is not None:
            marker.FullName = args['full_name']

        if args['short_name'] is not None:
            marker.ShortName = args['short_name']

        if args['color_group_full_name'] is not None:
            marker.ShortName = args['color_group_full_name']

        db.session.add(marker)
        db.session.commit()
        return jsonify({'status': 'OK', 'result': marker.to_dict()})

    @jwt_required
    def delete(self):
        args = delete_marker_parser.parse_args()
        marker = db.session.query(Marker).get_or_404(args['id'])
        db.session.delete(marker)
        db.session.commit()
        if db.session.query(Marker).get(marker.Id) is None:
            return jsonify({'status': 'OK'})
        else:
            return jsonify({'status': 'BAD'})
