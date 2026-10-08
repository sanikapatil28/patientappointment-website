from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models.user_model import User, bcrypt
from utils.decorators import login_required, admin_required

auth_bp = Blueprint("auth", __name__)


# ================= REGISTER =================
@auth_bp.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        if User.find_by_email(email):
            flash("User already exists!")
            return redirect(url_for("auth.register"))

        user_data = {
            "name": name,
            "email": email,
            "password": password
        }

        User.create_user(user_data)

        flash("Registration successful! Please login.")
        return redirect(url_for("auth.login"))

    return render_template("register.html")


# ================= LOGIN =================
@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = User.find_by_email(email)

        if user and bcrypt.check_password_hash(user["password"], password):
            session["user_id"] = str(user["_id"])
            session["name"] = user["name"]
            session["role"] = user["role"]

            return redirect(url_for("dashboard"))

        flash("Invalid Credentials")

    return render_template("login.html")


# ================= LOGOUT =================
@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))


# ================= PROMOTE USER =================
@auth_bp.route("/admin/promote", methods=["GET", "POST"])
@login_required
@admin_required
def promote_user():

    if request.method == "POST":

        email = request.form["email"]

        result = User.promote_to_admin(email)

        if result.modified_count > 0:
            flash("User promoted to Admin successfully!")
        else:
            flash("User not found!")

        return redirect(url_for("auth.promote_user"))

    return render_template("promote_user.html")