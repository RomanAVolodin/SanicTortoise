import uuid

from sanic import json, Request, HTTPResponse
from tortoise import models
from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator
from tortoise.fields import UUIDField, CharField, IntField


class Customer(models.Model):
    id = UUIDField(pk=True, default=uuid.uuid4)
    name = CharField(200)
    email = CharField(200, unique=True, index=True)
    age = IntField()

    def __str__(self):
        return f'{self.name}:{self.age}'


CustomerPydantic = pydantic_model_creator(Customer)
CustomersPydanticList = pydantic_queryset_creator(Customer)


def customer_serializer(customer: Customer, _: Request, status: int, **kwargs) -> HTTPResponse:
    customer_schema = CustomerPydantic.model_validate(customer)
    return HTTPResponse(body=customer_schema.model_dump_json(), content_type='application/json', status=status)


def customers_list_serializer(customers: list[Customer], _: Request, status: int, **kwargs) -> HTTPResponse:
    customers_schema = CustomersPydanticList.model_validate(customers)
    return HTTPResponse(body=customers_schema.model_dump_json(), content_type='application/json', status=status)


def customers_list_serializer_raw(customers: list[Customer], _: Request, status: int, **kwargs) -> HTTPResponse:
    return json(
        [
            {
                'id': str(customer.id),
                'name': customer.name,
                'email': customer.email,
                'age': customer.age,
            }
            for customer in customers
        ],
        status=status,
    )
