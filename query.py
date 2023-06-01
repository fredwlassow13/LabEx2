class SchoolDatabase:

    def __init__(self, database):
        self.db = database
    def get_professor(self):
        query = "MATCH (e:Teacher {name:'Renzo'}) RETURN e.ano_nasc AS ano_nasc , e.cpf AS cpf"
        results = self.db.execute_query(query)
        x = [result["ano_nasc"]for result in results]
        y = [result["cpf"] for result in results]
        return x,y

    def get_professorM(self):
        query = "MATCH (e:Teacher) WHERE (e.name STARTS WITH 'M') RETURN e.name AS nome_Teacher"
        results = self.db.execute_query(query)
        a = [result["nome_Teacher"]for result in results]
        return a
    def get_cidade(self):
        query = "MATCH (e:City) RETURN  e.name AS nome_City"
        results = self.db.execute_query(query)
        b = [result["nome_City"]for result in results]
        return b

    def get_school(self):
        query = "MATCH (e:School) WHERE (e.number >= 150 AND e.number <= 550)  RETURN e.name AS nome_School, e.address AS nome_Address, e.number AS n_Number"
        results = self.db.execute_query(query)
        c = [result["nome_School"] for result in results]
        d = [result["nome_Address"] for result in results]
        e = [result["n_Number"] for result in results]
        return c,d,e

    def get_older_younger(self):
        query = "MATCH (e:Teacher) RETURN max(e.ano_nasc) AS a_maior, min(e.ano_nasc) AS a_menor"
        results = self.db.execute_query(query)
        f = [result["a_maior"] for result in results]
        g = [result["a_menor"] for result in results]
        return f,g
    def get_media(self):
        query = "MATCH (e:City) RETURN avg(e.population) AS media"
        results = self.db.execute_query(query)
        return [result["media"] for result in results]
    def get_CEP(self):
        query = "MATCH (e:City {cep:'37540-000'}) RETURN e.name AS n_city"
        results = self.db.execute_query(query)
        h = [result["n_city"] for result in results]
        i = h[0].replace("a", "A")
        return i
    def get_terceira(self):
        query = "MATCH (e:Teacher) RETURN e.name as name"
        results = self.db.execute_query(query)
        j = [result["name"] for result in results]
        k = []
        for name in j:
            k.append(name[3])
        return name


