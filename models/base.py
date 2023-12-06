from sqlalchemy.orm import declarative_base

Base = declarative_base()

from models.resources.user import User
from models.resources.pet import Pet
