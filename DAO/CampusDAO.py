from Connection.ConnectionFactory import ConnectionFactory


def listaCampi():
    try:
        collection = ConnectionFactory.getConnection('Campus')
        campi = []
        for item in collection.find():
            campi.append(item['nome'])
        return campi
    except Exception as e:
        print('Error in listing Campus: ', e)
        return ["Error"]


def insert(campus):
    try:
        collection = ConnectionFactory.getConnection('Campus')
        collection.insert_one(campus.__dict__)
    except Exception as e:
        print('Error in mongo insert: ', e)
