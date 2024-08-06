from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.base import Base

class Professor(Base):
    __tablename__ = 'professores'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    departamento = Column(String)
    disciplinas = relationship('OfertaDisciplina', back_populates='professor')