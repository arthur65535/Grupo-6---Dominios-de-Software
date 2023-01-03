from typing import TYPE_CHECKING

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

from core.app.db.base import Base

if TYPE_CHECKING:
    from .address import Address  # noqa: F401


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    fullname = Column(String)

    addresses = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"


