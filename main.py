from sanic import Sanic

from api.v1.customers import bp_customers
from api.v1.orders import bp_orders
from db.postgres import init_db


def create_app() -> Sanic:
    app = Sanic('CustomerService')
    init_db(app)

    app.blueprint(bp_customers)
    app.blueprint(bp_orders)

    return app
