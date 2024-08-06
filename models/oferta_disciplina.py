from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base

class OfertaDisciplina(Base):
    __tablename__ = 'ofertas_disciplinas'

    id = Column(Integer, primary_key=True)
    disciplina_id = Column(Integer, ForeignKey('disciplinas.id'))
    professor_id = Column(Integer, ForeignKey('professores.id'))
    periodo = Column(String)
    horario = Column(String)
    
    professor = relationship('Professor', back_populates='disciplinas')
    disciplina = relationship('Disciplina')
    matriculas = relationship("Matricula", back_populates="oferta_disciplina")