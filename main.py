from database import Database
from query import SchoolDatabase
from teacher_crud import TeacherCRUD

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://18.233.93.132:7687", "neo4j", "person-ending-cars")
db2 = TeacherCRUD("bolt://18.233.93.132:7687", "neo4j", "person-ending-cars")

# Criando uma instância da classe SchoolDatabase para interagir com o banco de dados
school_db = SchoolDatabase(db)

#1
print(school_db.get_professor())
print(school_db.get_professorM())
print(school_db.get_cidade())
print(school_db.get_school())

# 2

print(school_db.get_older_younger())
print(school_db.get_media())
print(school_db.get_CEP())
print(school_db.get_terceira())

# 3

db2.create_professor('Chris Lima', 1956, '189.052.396-66')
print(db2.get_professor('Chris Lima'))
db2.update_professor('Chris Lima', '162.052.777-77')
print(db2.get_professor('Chris Lima'))
db2.delete_professor('Chris Lima')