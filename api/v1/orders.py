from http import HTTPStatus
from uuid import UUID

from sanic import Blueprint, SanicException, Request
from sanic_ext import serializer, validate

from api.v1.schemas.order import OrderSchema
from models.customer import Customer
from models.order import Order, order_serializer, orders_list_serializer

bp_orders = Blueprint('orders', url_prefix='orders', version=1)


@bp_orders.get('/')
@serializer(orders_list_serializer)
async def list_all(_: Request):
    orders = await Order.all()
    return orders


@bp_orders.get('/<customer_id:uuid>')
@serializer(orders_list_serializer)
async def list_for_customer(_: Request, customer_id: UUID):
    orders = await Order.filter(customer_id=customer_id).all()
    return orders


@bp_orders.post('/<customer_id:uuid>')
@validate(json=OrderSchema)
@serializer(order_serializer)
async def add_order(_: Request, body: OrderSchema, customer_id: UUID):
    customer = await Customer.filter(id=customer_id).first()
    if not customer:
        raise SanicException('Customer was not found', status_code=HTTPStatus.NOT_FOUND)
    order = await Order.create(customer=customer, price=body.price, title=body.title)
    return order
