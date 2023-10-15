import pymongo
import requests


class ConnectionFactory:

    @staticmethod
    def getDatabase(database):
        try:
            client = pymongo.MongoClient(
                "mongodb+srv://unip:aluno@cluster0.c2q6lgv.mongodb.net/?retryWrites=true&w=majority")
            db = client.get_database(database)
            return db
        except Exception as e:
            print('Error getting database', e)

    @staticmethod
    def getConnection(collection_name):
        try:
            client = pymongo.MongoClient(
                "mongodb+srv://unip:aluno@cluster0.c2q6lgv.mongodb.net/?retryWrites=true&w=majority")
            db = client.get_database('TCC')
            collection = db.get_collection(collection_name)
            return collection
        except Exception as e:
            print('Error in mongo connection: ', e)

    @staticmethod
    def getCep(cep):
        endpoint = "https://viacep.com.br/ws/CEP/json/".replace('CEP', cep)
        try:
            response = requests.get(endpoint, timeout=5).json()
            if 'erro' in response:
                return 'Invalid'
            else:
                return response
        except requests.exceptions.HTTPError as errh:
            print('Error in the HTTP: ', errh)
        except requests.exceptions.ConnectionError as errc:
            print('Error in the Connection: ', errc)
        except requests.exceptions.Timeout as errt:
            print('Timeout Error: ', errt)
        except requests.exceptions.RequestException as err:
            print('Error in Request: ', err)
