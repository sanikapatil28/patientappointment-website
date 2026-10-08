from utils.db import appointments_collection
from bson.objectid import ObjectId
from datetime import datetime


class Appointment:

    @staticmethod
    def is_slot_available(doctor_id, date, time):
        existing = appointments_collection.find_one({
            "doctor_id": ObjectId(doctor_id),
            "date": date,
            "time": time,
            "status": "Booked"
        })
        return existing is None

    @staticmethod
    def book_appointment(data):

        if not Appointment.is_slot_available(
            data["doctor_id"], data["date"], data["time"]
        ):
            return False

        appointment = {
            "patient_id": ObjectId(data["patient_id"]),
            "doctor_id": ObjectId(data["doctor_id"]),
            "date": data["date"],
            "time": data["time"],
            "status": "Booked",
            "created_at": datetime.utcnow()
        }

        appointments_collection.insert_one(appointment)
        return True

    @staticmethod
    def get_patient_appointments(patient_id):
        return list(
            appointments_collection.find(
                {"patient_id": ObjectId(patient_id)}
            )
        )

    @staticmethod
    def cancel_appointment(appointment_id):
        appointments_collection.update_one(
            {"_id": ObjectId(appointment_id)},
            {"$set": {"status": "Cancelled"}}
        )

    @staticmethod
    def get_booked_slots(doctor_id, date):
        bookings = appointments_collection.find({
            "doctor_id": ObjectId(doctor_id),
            "date": date,
            "status": "Booked"
        })

        return [b["time"] for b in bookings]

    @staticmethod
    def get_all_appointments():
        return list(appointments_collection.find())

    @staticmethod
    def count_appointments():
        return appointments_collection.count_documents({})

    @staticmethod
    def appointments_per_doctor():
        pipeline = [
            {
                "$group": {
                    "_id": "$doctor_id",
                    "count": {"$sum": 1}
                }
            },
            {
                "$lookup": {
                    "from": "doctors",
                    "localField": "_id",
                    "foreignField": "_id",
                    "as": "doctor_info"
                }
            },
            {
                "$unwind": "$doctor_info"
            },
            {
                "$project": {
                    "_id": 0,
                    "doctor_name": "$doctor_info.name",
                    "count": 1
                }
            }
        ]

        return list(appointments_collection.aggregate(pipeline))