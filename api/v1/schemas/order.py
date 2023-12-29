from pydantic import BaseModel, conint


class OrderSchema(BaseModel):
    title: str
    price: conint(ge=0, le=100_000)
