from sqlalchemy import ForeignKey, Column, String, Integer
from sqlalchemy.orm import relationship
from db.base import Base

class Matricula(Base):
    __tablename__ = 'matriculas'

    id = Column(Integer, primary_key=True)
    aluno_id = Column(Integer, ForeignKey('alunos.id'))
    oferta_disciplina_id = Column(Integer, ForeignKey("ofertas_disciplinas.id"))
    status = Column(String, default='ativo')

    aluno = relationship('Aluno', back_populates='matriculas')
    oferta_disciplina = relationship("OfertaDisciplina", back_populates="matriculas")