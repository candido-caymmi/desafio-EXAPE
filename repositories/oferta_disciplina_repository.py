from models.oferta_disciplina import OfertaDisciplina 
from .repository import Repository

class OfertaDisciplinaRepository(Repository):
    def __init__(self, session):
        super().__init__(OfertaDisciplina, session)