from dotenv import load_dotenv
from pymongo import MongoClient
import os


def get_collection():
    load_dotenv()

    uri = os.environ['DB_URI']

    client = MongoClient(uri)
    db = client['rosen']

    return db['big_data_2']
