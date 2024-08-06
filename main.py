from db.base import Base
from db.session import engine, get_session
from models import Aluno, Disciplina, Professor, OfertaDisciplina, Matricula
from repositories import AlunoRepository, DisciplinaRepository, MatriculaRepository, ProfessorRepository, OfertaDisciplinaRepository

Base.metadata.create_all(engine)
session = get_session()

aluno_repository = AlunoRepository(session)
disciplina_repository = DisciplinaRepository(session)
professor_repository = ProfessorRepository(session)
matricula_repository = MatriculaRepository(session)
oferta_disciplina_repository = OfertaDisciplinaRepository(session)

novo_aluno = Aluno(nome='João Cândido', curso='Análise e Desenvolvimento de Sistemas')
novo_professor = Professor(nome='João Souza', departamento='Computação')
nova_disciplina = Disciplina(nome='Introdução à Programação', descricao='Lorem Ipsum', carga_horaria=70)
nova_oferta_disciplina = OfertaDisciplina(disciplina=nova_disciplina, professor=novo_professor, periodo='2024/1', horario='Segundas e Quartas, 10h-12h')
nova_matricula = Matricula(aluno=novo_aluno, oferta_disciplina=nova_oferta_disciplina)


aluno_repository.add(novo_aluno)
matricula_repository.add(nova_matricula)
disciplina_repository.add(nova_disciplina)
professor_repository.add(novo_professor)


results = aluno_repository.get(1)


print(results)

        
