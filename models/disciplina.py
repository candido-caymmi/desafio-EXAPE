from sqlalchemy import Column, Integer, String
from db.base import Base

class Disciplina(Base):
    __tablename__ = 'disciplinas'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    descricao = Column(String)
    carga_horaria = Column(Integer)