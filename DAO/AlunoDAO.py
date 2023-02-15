from Connection.ConnectionFactory import Connection

def insert(aluno):
    collection = Connection.getConnection('Aluno')
    collection.insert_one(aluno.__dict__)
