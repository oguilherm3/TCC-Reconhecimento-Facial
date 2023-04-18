from Connection.ConnectionFactory import ConnectionFactory


def listaCursos():
    try:
        collection = ConnectionFactory.getConnection('Cursos')
        cursos = []
        for item in collection.find():
            cursos.append(item['nome'])
        return cursos
    except Exception as e:
        print('Error in listing: ', e)
        return ["Error"]

def insert(curso):
    try:
        collection = ConnectionFactory.getConnection('Cursos')
        collection.insert_one(curso.__dict__)
    except Exception as e:
        print('Error in mongo insert: ', e)
