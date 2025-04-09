from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self):
        self.client = MongoClient(os.getenv('MONGOURL'), tlsallowinvalidcertificates=True)
        self.db = self.client[os.getenv('MONGOCOLLECTION')]

    def get_collection(self, collection):
        return self.db[collection]

    def test_connection(self):
        # Lista las colecciones disponibles en la base de datos
        return self.db.list_collection_names()

Database = Database()