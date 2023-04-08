from Connection.ConnectionFactory import ConnectionFactory

def insert(aluno):
    try:
        collection = ConnectionFactory.getConnection('Aluno')
        collection.insert_one(aluno.__dict__)
    except Exception as e:
        print('Error in mongo insert: ', e)
