from pymongo import MongoClient
from config import Config

client = MongoClient(Config.MONGO_URI)
db = client.get_database()

users_collection = db["users"]
doctors_collection = db["doctors"]
appointments_collection = db["appointments"]