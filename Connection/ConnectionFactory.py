import pymongo


class Connection:

    @staticmethod
    def getConnection(collection_name):
        try:
            client = pymongo.MongoClient("mongodb+srv://unip:aluno@cluster0.c2q6lgv.mongodb.net/?retryWrites=true&w=majority")
            db = client.get_database('TCC')
            collection = db.get_collection(collection_name)
            return collection
        except Exception as e:
            print('Error in mongo connection: ', e)
