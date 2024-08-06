from models.aluno import Aluno
from .repository import Repository

class AlunoRepository(Repository):
    def __init__(self, session):
        super().__init__(Aluno, session)