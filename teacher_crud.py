
from neo4j import GraphDatabase

class TeacherCRUD:
        def __init__(self, uri, user, password):
            self.driver = GraphDatabase.driver(uri, auth=(user, password))

        def close(self):
            self.driver.close()

        def create_professor(self, name, ano_nasc, cpf):
            with self.driver.session() as session:
                session.run("CREATE(e:Teacher {name: $name, ano_nasc: $ano_nasc, cpf: $cpf}) RETURN  e.id as id", name=name, ano_nasc=ano_nasc, cpf=cpf)

        def update_professor(self, name, newCpf):
            with self.driver.session() as session:
                session.run("MATCH(e:Teacher) WHERE (e.name = $name) SET e.cpf = $cpf", name=name, cpf=newCpf)

        def delete_professor(self, name):
            with self.driver.session() as session:
                session.run("MATCH(e:Teacher) WHERE (e.name = $name) DETACH DELETE e", name=name)

        def get_professor(self, name):
            with self.driver.session() as session:
                result = session.run("MATCH (e:Teacher) WHERE (e.name = $name) RETURN e.name AS name, e.cpf AS cpf, e.ano_nasc AS nasc", name=name)
                return [{"Name": record["name"], "cpf": record["cpf"], "ano_nasc": record["nasc"]} for record in result]


