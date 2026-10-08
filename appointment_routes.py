from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models.appointment_model import Appointment
from utils.decorators import login_required
from bson.objectid import ObjectId
from models.doctor_model import Doctor
from utils.decorators import admin_required
from models.user_model import User
from models.doctor_model import Doctor


appointment_bp = Blueprint("appointment", __name__)

@appointment_bp.route("/book/<doctor_id>", methods=["GET", "POST"])
@login_required
def book_appointment(doctor_id):

    doctor = Doctor.get_doctor_by_id(doctor_id)

    if not doctor:
        flash("Doctor not found!")
        return redirect(url_for("doctor.view_doctors"))

    selected_date = request.args.get("date")

    available_slots = doctor["available_slots"]

    if selected_date:
        booked_slots = Appointment.get_booked_slots(
            doctor_id, selected_date
        )

        available_slots = [
            slot for slot in doctor["available_slots"]
            if slot not in booked_slots
        ]

    if request.method == "POST":

        data = {
            "patient_id": session["user_id"],
            "doctor_id": doctor_id,
            "date": request.form["date"],
            "time": request.form["time"]
        }

        success = Appointment.book_appointment(data)

        if not success:
            flash("❌ Slot already booked!")
            return redirect(request.url)

        flash("✅ Appointment booked!")
        return redirect(url_for("appointment.my_appointments"))

    return render_template(
        "book_appointment.html",
        doctor=doctor,
        available_slots=available_slots
    )

@appointment_bp.route("/my-appointments")
@login_required
def my_appointments():

    appointments = Appointment.get_patient_appointments(
        session["user_id"]
    )

    return render_template(
        "my_appointments.html",
        appointments=appointments
    )

@appointment_bp.route("/cancel/<appointment_id>")
@login_required
def cancel_appointment(appointment_id):

    Appointment.cancel_appointment(appointment_id)
    flash("❌ Appointment cancelled successfully!")

    return redirect(url_for("appointment.my_appointments"))

@appointment_bp.route("/admin/appointments")
@login_required
def admin_all_appointments():

    appointments = Appointment.get_all_appointments()
    doctors = Doctor.get_all_doctors()
    users = User.get_all_users()

    # Create lookup maps
    doctor_map = {str(doc["_id"]): doc["name"] for doc in doctors}
    user_map = {str(user["_id"]): user["name"] for user in users}

    # Attach readable names
    for appt in appointments:
        appt["doctor_name"] = doctor_map.get(str(appt["doctor_id"]), "Unknown Doctor")
        appt["patient_name"] = user_map.get(str(appt["patient_id"]), "Unknown Patient")

    return render_template(
        "admin_appointments.html",   # keep your template name
        appointments=appointments
    )

@appointment_bp.route("/admin/dashboard")
@login_required
@admin_required
def admin_dashboard():

    total_doctors = Doctor.count_doctors()
    total_patients = User.count_users_by_role("patient")
    total_appointments = Appointment.count_appointments()
    doctor_stats = Appointment.appointments_per_doctor()

    # Prepare chart data
    doctor_names = [doc["doctor_name"] for doc in doctor_stats]
    appointment_counts = [doc["count"] for doc in doctor_stats]

    return render_template(
        "admin_dashboard.html",
        total_doctors=total_doctors,
        total_patients=total_patients,
        total_appointments=total_appointments,
        doctor_names=doctor_names,
        appointment_counts=appointment_counts
    )