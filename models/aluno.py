from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from db.base import Base
from dataclasses import dataclass

class Aluno(Base):
    __tablename__ = 'alunos'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    curso = Column(String)
    matriculas = relationship('Matricula', back_populates='aluno')

    def __repr__(self):
        return f"({self.id}) {self.nome}, cursando {self.curso}"