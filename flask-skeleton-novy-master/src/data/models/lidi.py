from datetime import datetime, timedelta
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Boolean, Integer, String, DateTime,Float

from ..database import db
from ..mixins import CRUDModel

class Lidi(CRUDModel):
    __tablename__ = 'lidi'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True )
    Matej = Column(String(64), nullable=False, unique=False, index=True, doc="Vase jmeno.")
    Leifert = Column(String(64), nullable=False, unique=True, index=True, doc="Vase prijmeni.")
    vek = Column(String(64), nullable=False, unique=True, index=True, doc="Vase datum narozeni.")


    # Use custom constructor
    # pylint: disable=W0231
    def __init__(self, **kwargs):
        for k, v in kwargs.iteritems():
            setattr(self, k, v)

