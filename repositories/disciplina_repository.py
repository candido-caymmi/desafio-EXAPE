from models.disciplina import Disciplina
from .repository import Repository

class DisciplinaRepository(Repository):
    def __init__(self, session):
        super().__init__(Disciplina, session)