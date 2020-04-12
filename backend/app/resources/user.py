from flask_restful import Resource
from app.models import User
from flask import jsonify
from app.parsers import post_user_parser, put_user_parser
from app.database import db
from app.mail import send_email
from datetime import datetime
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from re import match


class UserApi(Resource):
    @jwt_required
    def get(self):
        user_id = get_jwt_identity()
        return jsonify({'status': 'OK', 'result': db.session.query(User).get_or_404(user_id).to_dict()})

    def post(self):
        args = post_user_parser.parse_args()

        if db.session.query(User).filter(User.Email.like(args['email'])).first() is None:
            if not match(r"(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)", args['email']):
                return jsonify({'status': 'BAD', 'result': 'Incorrect email address'})

            user = User(Name=args['name'],
                        Email=args['email'],
                        DisplayName=args['display_name'],
                        FamilyName=args['family_name'],
                        RegistrationDate=datetime.now(),
                        LastVisit=datetime.now())
            db.session.add(user)
            db.session.commit()

        user = db.session.query(User).filter(User.Email.like(args['email'])).first()
        access_token = create_access_token(identity=user.Id)
        send_email(subject="Auth MarkerSet",
                   recipients=[args['email']],
                   text_body="You have recently authorized to MarkerSet.",
                   html_body="")
        return jsonify({'status': 'OK', 'result': access_token})

    @jwt_required
    def put(self):
        user_id = get_jwt_identity()
        args = put_user_parser.parse_args()
        user = db.session.query(User).get_or_404(user_id)

        if args['email'] is not None:
            if db.session.query(User).filter(User.Email.like(args['email'])).first() is not None:
                return jsonify({'status': 'BAD', 'result': 'Such user already exists'})

            user.Email = args['email']

        if args['name'] is not None:
            user.Name = args['name']

        if args['display_name'] is not None:
            user.DisplayName = args['display_name']

        if args['family_name'] is not None:
            user.FamilyName = args['family_name']

        user.LastVisit = datetime.now()

        db.session.add(user)
        db.session.commit()
        return jsonify({'status': 'OK', 'result': user.to_dict()})

    @jwt_required
    def delete(self):
        user_id = get_jwt_identity()
        user = db.session.query(User).get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        if db.session.query(User).get(user_id) is None:
            return jsonify({'status': 'OK'})
        else:
            return jsonify({'status': 'BAD'})
