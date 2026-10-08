from utils.db import users_collection
from flask_bcrypt import Bcrypt
from bson.objectid import ObjectId

bcrypt = Bcrypt()

class User:

    @staticmethod
    def create_user(data):
        hashed_password = bcrypt.generate_password_hash(
            data["password"]
        ).decode("utf-8")

        user = {
            "name": data["name"],
            "email": data["email"],
            "password": hashed_password,
            "role": "patient"   # 🔒 Always patient
        }

        users_collection.insert_one(user)

    @staticmethod
    def find_by_email(email):
        return users_collection.find_one({"email": email})

    @staticmethod
    def get_all_users():
        return list(users_collection.find())

    @staticmethod
    def count_users_by_role(role):
        return users_collection.count_documents({"role": role})

    @staticmethod
    def promote_to_admin(email):
        return users_collection.update_one(
            {"email": email},
            {"$set": {"role": "admin"}}
        )