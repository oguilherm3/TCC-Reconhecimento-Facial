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


def listaAlunos():
    try:
        collection = ConnectionFactory.getConnection('Aluno')
        alunos = list(collection.find())
        return alunos
    except Exception as e:
        print('Error Listing Alunos: ', e)
        return ["Error"]


def update(aluno):
    try:
        collection = ConnectionFactory.getConnection('Aluno')
        filtro = {"_id": aluno._id}
        att = {"$set": aluno.__dict__}
        collection.update_one(filtro, att)
        return True
    except Exception as e:
        print('Error in update Aluno: ', e)
        return False
