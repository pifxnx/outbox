from fastapi import FastAPI, Depends
from pydantic import BaseModel, ConfigDict
from uuid import UUID
from sqlalchemy import select
from ..db import get_db
from ..models import Order

app = FastAPI()


class OrderCreate(BaseModel):
    client: str

class OrderResponse(BaseModel):
    id: UUID
    client: str

    model_config = ConfigDict(from_attributes=True)


@app.post("/orders")
async def create_order(order: OrderCreate, session=Depends(get_db)):
    order = Order(client=order.client)
    session.add(order)
    await session.commit()
    await session.refresh(order)

    return OrderResponse.model_validate(order)


@app.get("/orders_list")
async def list_orders(session = Depends(get_db)):
    result = await session.execute(select(Order))
    orders = result.scalars().all()

    return [OrderResponse.model_validate(order) for order in orders]
