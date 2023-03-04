from Connection.ConnectionFactory import Connection

def insert(aluno):
    try:
        collection = Connection.getConnection('Aluno')
        collection.insert_one(aluno.__dict__)
    except Exception as e:
        print('Error in mongo insert: ', e)
