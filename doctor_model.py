from bson.objectid import ObjectId
from utils.db import doctors_collection

class Doctor:

    @staticmethod
    def get_doctor_by_id(doctor_id):
        return doctors_collection.find_one(
            {"_id": ObjectId(doctor_id)}
        )

    @staticmethod
    def create_doctor(data):
        doctor = {
            "name": data["name"],
            "specialization": data["specialization"],
            "experience": data["experience"],
            "available_slots": data["available_slots"],
            "rating": 0
        }

        return doctors_collection.insert_one(doctor)

    @staticmethod
    def get_all_doctors():
        return list(doctors_collection.find())

    @staticmethod
    def get_doctor_by_specialization(spec):
        return list(doctors_collection.find({"specialization": spec}))
    
    @staticmethod
    def count_doctors():
     return doctors_collection.count_documents({})
    
    @staticmethod
    def update_doctor(doctor_id, data):
        doctors_collection.update_one(
            {"_id": ObjectId(doctor_id)},
            {"$set": data}
        )

    @staticmethod
    def delete_doctor(doctor_id):
        doctors_collection.delete_one(
            {"_id": ObjectId(doctor_id)}
        )