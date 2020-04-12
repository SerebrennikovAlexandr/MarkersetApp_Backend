from flask_restful import reqparse

# ========== User parsers ============

post_user_parser = reqparse.RequestParser()
post_user_parser.add_argument('name', type=str)
post_user_parser.add_argument('email', type=str, required=True)
post_user_parser.add_argument('display_name', type=str)
post_user_parser.add_argument('family_name', type=str)

put_user_parser = reqparse.RequestParser()
put_user_parser.add_argument('name', type=str)
put_user_parser.add_argument('email', type=str)
put_user_parser.add_argument('display_name', type=str)
put_user_parser.add_argument('family_name', type=str)

# ========== Marker parsers ============

get_marker_parser = reqparse.RequestParser()
get_marker_parser.add_argument('id', type=int)
get_marker_parser.add_argument('hex', type=str)
get_marker_parser.add_argument('brand', type=str)
get_marker_parser.add_argument('series', type=str)
get_marker_parser.add_argument('full_name', type=str)
get_marker_parser.add_argument('color_group_full_name', type=str)

post_marker_parser = reqparse.RequestParser()
post_marker_parser.add_argument('hex', type=str, required=True)
post_marker_parser.add_argument('brand', type=str, required=True)
post_marker_parser.add_argument('series', type=str, required=True)
post_marker_parser.add_argument('color_group', type=str)
post_marker_parser.add_argument('full_name', type=str, required=True)
post_marker_parser.add_argument('short_name', type=str, required=True)
post_marker_parser.add_argument('color_group_full_name', type=str, required=True)

put_marker_parser = reqparse.RequestParser()
put_marker_parser.add_argument('id', type=int, required=True)
put_marker_parser.add_argument('hex', type=str)
put_marker_parser.add_argument('brand', type=str)
put_marker_parser.add_argument('series', type=str)
put_marker_parser.add_argument('color_group', type=str)
put_marker_parser.add_argument('full_name', type=str)
put_marker_parser.add_argument('short_name', type=str)
put_marker_parser.add_argument('color_group_full_name', type=str)

delete_marker_parser = reqparse.RequestParser()
delete_marker_parser.add_argument('id', type=int, required=True)

# ========== Store parsers ============

get_store_parser = reqparse.RequestParser()
get_store_parser.add_argument('id', type=int)
get_store_parser.add_argument('name', type=str)

post_store_parser = reqparse.RequestParser()
post_store_parser.add_argument('name', type=str, required=True)
post_store_parser.add_argument('site', type=str, required=True)
post_store_parser.add_argument('logo', type=str, required=True)

put_store_parser = reqparse.RequestParser()
put_store_parser.add_argument('id', type=int, required=True)
put_store_parser.add_argument('name', type=str)
put_store_parser.add_argument('site', type=str)
put_store_parser.add_argument('logo', type=str)

delete_store_parser = delete_marker_parser.copy()

# ========== Wishlist parsers ============

post_wishlist_parser = reqparse.RequestParser()
post_wishlist_parser.add_argument('added_markers', type=int, action='append')
post_wishlist_parser.add_argument('deleted_markers', type=int, action='append')

# ========== My parsers ============

post_my_parser = post_wishlist_parser.copy()

# ========== Cart parsers ============

post_cart_parser = reqparse.RequestParser()
post_cart_parser.add_argument('marker_id', type=int, required=True)
post_cart_parser.add_argument('amount', type=int)

put_cart_parser = reqparse.RequestParser()
put_cart_parser.add_argument('marker_id', type=int, required=True)
put_cart_parser.add_argument('amount', type=int, required=True)

delete_cart_parser = reqparse.RequestParser()
delete_cart_parser.add_argument('marker_id', type=int, required=True)
