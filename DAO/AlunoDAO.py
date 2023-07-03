from Connection.ConnectionFactory import ConnectionFactory


def insert(aluno):
    try:
        collection = ConnectionFactory.getConnection('Aluno')
        collection.insert_one(aluno.__dict__)
        return True
    except Exception as e:
        print('Error in Aluno insert: ', e)
        return False


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
        filtro = {"cpf": aluno.cpf}
        att = {"$set": aluno.__dict__}
        collection.update_one(filtro, att)
        return True
    except Exception as e:
        print('Error in update Aluno: ', e)
        return False


def delete(aluno):
    try:
        collection = ConnectionFactory.getConnection('Aluno')
        filtro = {"cpf": aluno.cpf}
        collection.delete_one(filtro)
        return True
    except Exception as e:
        print('Error in delete Aluno: ', e)
        return False
