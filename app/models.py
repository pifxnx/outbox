from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from uuid import UUID, uuid4


class Base(DeclarativeBase):
    pass

class Order(Base):
    __tablename__ = "orders"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=lambda : uuid4())
    client: Mapped[str]
