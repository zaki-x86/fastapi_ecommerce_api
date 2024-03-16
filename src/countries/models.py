from sqlalchemy.orm import Mapped, relationship

from src.database import Base
from src.models import str256, uuidpk


class Country(Base):
    __tablename__ = "countries"

    id: Mapped[uuidpk]
    name: Mapped[str256]

    addresses = relationship("Address", back_populates="country")
