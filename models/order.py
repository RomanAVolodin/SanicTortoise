import uuid

from sanic import Request, HTTPResponse
from tortoise import models
from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator, PydanticListModel
from tortoise.fields import (
    UUIDField,
    ForeignKeyField,
    BooleanField,
    DatetimeField,
    DecimalField,
    CharField,
    ForeignKeyRelation,
)

from models.customer import Customer


class Order(models.Model):
    id = UUIDField(pk=True, default=uuid.uuid4)
    customer: ForeignKeyRelation[Customer] = ForeignKeyField('models.Customer', related_name='orders')
    is_payed = BooleanField(default=False)
    created_at = DatetimeField(auto_now=True)
    price = DecimalField(max_digits=10, decimal_places=2, null=True)
    title = CharField(max_length=100, null=False)


OrderPydantic = pydantic_model_creator(Order)
OrdersPydanticList = pydantic_queryset_creator(Order)


def order_serializer(order: Order, _: Request, status: int, **kwargs) -> HTTPResponse:
    order_schema = OrderPydantic.model_validate(order)
    return HTTPResponse(body=order_schema.model_dump_json(), content_type='application/json', status=status)


def orders_list_serializer(orders: list[Order], _: Request, status: int, **kwargs) -> HTTPResponse:
    orders_schema = OrdersPydanticList.model_validate(orders)
    return HTTPResponse(body=orders_schema.model_dump_json(), content_type='application/json', status=status)
