from models.matricula import Matricula
from .repository import Repository

class MatriculaRepository(Repository):
    def __init__(self, session):
        super().__init__(Matricula, session)