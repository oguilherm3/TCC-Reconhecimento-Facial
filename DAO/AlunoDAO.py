from Connection.ConnectionFactory import ConnectionFactory

def insert(aluno):
    try:
        collection = ConnectionFactory.getConnection('Aluno')
        collection.insert_one(aluno.__dict__)
    except Exception as e:
        print('Error in Aluno insert: ', e)

def insert_getId(aluno):
    try:
        collection = ConnectionFactory.getConnection('Aluno')
        return collection.insert_one(aluno.__dict__).inserted_id
    except Exception as e:
        print('Error in Aluno insert: ', e)
