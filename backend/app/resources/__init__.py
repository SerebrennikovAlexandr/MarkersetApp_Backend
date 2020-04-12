from flask_restful import Api
from .user import UserApi
from .marker import MarkerApi
from .store import StoreApi
from .status import Status
from .wishlist import WishlistApi
from .my import MyApi
from .cart import CartApi
from .cart_hash import CartHashApi
from .marker_hash import MarkerHashApi
from .my_hash import MyHashApi
from .wishlist_hash import WishlistHashApi


def create_api(app):
    api = Api(app)
    api.add_resource(UserApi, "/user")
    api.add_resource(MarkerApi, "/marker")
    api.add_resource(MarkerHashApi, "/marker-hash")
    api.add_resource(StoreApi, "/store")
    api.add_resource(Status, "/status")
    api.add_resource(WishlistApi, "/wishlist")
    api.add_resource(WishlistHashApi, "/wishlist-hash")
    api.add_resource(MyApi, "/my")
    api.add_resource(MyHashApi, "/my-hash")
    api.add_resource(CartApi, "/cart")
    api.add_resource(CartHashApi, "/cart-hash")

    return api
