""" melody """
from sqlalchemy import Column,\
                       String

from models.utils import Model, Wrapper


class Melody(Wrapper,
             Model):

    name = Column(String(1000))

    intervals = Column(String(1000))
