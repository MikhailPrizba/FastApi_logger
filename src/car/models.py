from base import Base
from sqlalchemy.orm import Mapped, mapped_column


class Car(Base):
    __tablename__ = "car"

    id: Mapped[int] = mapped_column(primary_key=True)
    mark: Mapped[str]
    models: Mapped[str]
    car_type: Mapped[str]
    color: Mapped[str]
    descriptions: Mapped[str | None]
    max_price: Mapped[int]
    is_active: Mapped[bool]
