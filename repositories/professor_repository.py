from models.professor import Professor
from .repository import Repository

class ProfessorRepository(Repository):
    def __init__(self, session):
        super().__init__(Professor, session)