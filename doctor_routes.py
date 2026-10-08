from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.doctor_model import Doctor
from utils.decorators import login_required, admin_required
from bson.objectid import ObjectId

doctor_bp = Blueprint("doctor", __name__)


# ===============================
# View Doctors (Admin + Patient)
# ===============================
@doctor_bp.route("/doctors")
@login_required
def view_doctors():
    doctors = Doctor.get_all_doctors()
    return render_template("view_doctors.html", doctors=doctors)


# ===============================
# Add Doctor (Admin Only)
# ===============================
@doctor_bp.route("/add-doctor", methods=["GET", "POST"])
@login_required
@admin_required
def add_doctor():

    if request.method == "POST":
        data = {
            "name": request.form["name"],
            "specialization": request.form["specialization"],
            "experience": request.form["experience"],
            "available_slots": request.form["available_slots"].split(","),
            "rating": 0
        }

        Doctor.create_doctor(data)
        flash("Doctor added successfully!")
        return redirect(url_for("doctor.view_doctors"))

    return render_template("add_doctor.html")


# ===============================
# Edit Doctor (Admin Only)
# ===============================
@doctor_bp.route("/edit-doctor/<doctor_id>", methods=["GET", "POST"])
@login_required
@admin_required
def edit_doctor(doctor_id):

    doctor = Doctor.get_doctor_by_id(doctor_id)

    if not doctor:
        flash("Doctor not found!")
        return redirect(url_for("doctor.view_doctors"))

    if request.method == "POST":
        updated_data = {
            "name": request.form["name"],
            "specialization": request.form["specialization"],
            "experience": request.form["experience"],
            "available_slots": request.form["available_slots"].split(",")
        }

        Doctor.update_doctor(doctor_id, updated_data)
        flash("Doctor updated successfully!")
        return redirect(url_for("doctor.view_doctors"))

    return render_template("edit_doctor.html", doctor=doctor)


# ===============================
# Delete Doctor (Admin Only)
# ===============================
@doctor_bp.route("/delete-doctor/<doctor_id>")
@login_required
@admin_required
def delete_doctor(doctor_id):

    doctor = Doctor.get_doctor_by_id(doctor_id)

    if not doctor:
        flash("Doctor not found!")
        return redirect(url_for("doctor.view_doctors"))

    Doctor.delete_doctor(doctor_id)
    flash("Doctor deleted successfully!")
    return redirect(url_for("doctor.view_doctors"))