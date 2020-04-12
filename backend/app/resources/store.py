from flask_restful import Resource
from app.models import Store
from flask import jsonify
from app.parsers import get_store_parser, post_store_parser, put_store_parser, delete_store_parser
from app.database import db
from flask_jwt_extended import jwt_required


class StoreApi(Resource):
    @jwt_required
    def get(self):
        args = get_store_parser.parse_args()
        if args['id'] is not None:
            return jsonify({'status': 'OK', 'result': db.session.query(Store).get_or_404(args['id']).to_dict()})

        elif args['name'] is not None:
            store_list = db.session.query(Store).filter(Store.Name.like(args['name'])).all()
            res = []
            for store in store_list:
                res.append(store.to_dict())
            return jsonify({'status': 'OK', 'result': res})

        else:
            store_list = db.session.query(Store).all()
            res = []
            for store in store_list:
                res.append(store.to_dict())
            return jsonify({'status': 'OK', 'result': res})

    @jwt_required
    def post(self):
        args = post_store_parser.parse_args()
        store = Store(
            Name=args['name'],
            Site=args['site'],
            Logo=args['logo']
        )
        db.session.add(store)
        db.session.commit()
        return jsonify({'status': 'OK', 'result': store.to_dict()})

    @jwt_required
    def put(self):
        args = put_store_parser.parse_args()
        store = db.session.query(Store).get_or_404(args['id'])

        if args['name'] is not None:
            store.Name = args['name']

        if args['site'] is not None:
            store.Site = args['site']

        if args['logo'] is not None:
            store.Logo = args['logo']

        db.session.add(store)
        db.session.commit()
        return jsonify({'status': 'OK', 'result': store.to_dict()})

    @jwt_required
    def delete(self):
        args = delete_store_parser.parse_args()
        store = db.session.query(Store).get_or_404(args['id'])
        db.session.delete(store)
        db.session.commit()
        if db.session.query(Store).get(store.Id) is None:
            return jsonify({'status': 'OK'})
        else:
            return jsonify({'status': 'BAD'})
