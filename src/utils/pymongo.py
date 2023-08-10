from dotenv import load_dotenv
import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()

def load_mongodb():
    
    client = MongoClient(os.environ['MONGO_PASS'], server_api=ServerApi('1'))
    
    return client