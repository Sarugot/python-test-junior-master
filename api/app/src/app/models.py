import uuid

from sqlalchemy import Column, VARCHAR, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from src.init_database import Base


class UserEvent(Base):
    __tablename__ = 'Events'

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        nullable=False
        )
    date_created = Column(
        DateTime(timezone=False),
        server_default=func.now(),
        nullable=False
        )
    user_ip = Column(
        VARCHAR(15),
        nullable=False
        )

    def __repr__(self):
        return "<{0.__class__.__name__}(id={0.id!r})>".format(self)
