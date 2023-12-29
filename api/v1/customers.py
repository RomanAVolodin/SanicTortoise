from uuid import UUID

from sanic import Blueprint, Request
from sanic.log import logger
from sanic_ext import serializer, validate

from api.v1.schemas.customers import CustomerSchema
from models.customer import customers_list_serializer, customer_serializer, Customer

bp_customers = Blueprint('customers', url_prefix='customers', version=1)


@bp_customers.get('/')
@serializer(customers_list_serializer)
async def list_all(request: Request):
    users = await Customer.all()
    logger.info(request)
    return users


@bp_customers.get('/<customer_id:uuid>')
@serializer(customer_serializer)
async def get_by_id(_: Request, customer_id: UUID):
    customer = await Customer.filter(id=customer_id).first()
    return customer


@bp_customers.post('/')
@serializer(customer_serializer)
@validate(json=CustomerSchema)
async def add_user(_: Request, body: CustomerSchema):
    user = await Customer.create(name=body.name, email=body.email, age=body.age)
    return user
