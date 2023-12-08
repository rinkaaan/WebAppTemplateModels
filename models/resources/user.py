import datetime
import os
import uuid

from models.base import Base
from jose import jwt
from sqlalchemy import Column, UUID, ColumnElement, DateTime, Text
from sqlalchemy.orm import relationship

from nguylinc_python_utils.sqlalchemy import BaseExtended


class User(Base, BaseExtended):
    __tablename__ = "users"
    id = Column(UUID, primary_key=True, index=True, default=uuid.uuid4)
    created_at: ColumnElement = Column(DateTime(), index=True)
    email = Column(Text(), unique=True)
    name = Column(Text())
    picture = Column(Text())
    given_name = Column(Text())
    family_name = Column(Text())
    locale = Column(Text())

    pets = relationship("Pet", backref="user", passive_deletes=True)

    editable_fields = []
    google_fields = ["email", "name", "picture", "given_name", "family_name", "locale"]

    def generate_token(self):
        timestamp = datetime.datetime.now(datetime.timezone.utc).timestamp()
        payload = {
            "iss": "com.nguylinc",
            "iat": int(timestamp),
            "sub": str(self.id),
        }

        return jwt.encode(payload, os.getenv("JWT_SECRET"))
