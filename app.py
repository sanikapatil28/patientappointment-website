from flask import Flask, render_template, session, redirect, url_for
from config import Config
from routes.auth_routes import auth_bp
from routes.appointment_routes import appointment_bp
from routes.doctor_routes import doctor_bp

app = Flask(__name__)
app.config.from_object(Config)

app.secret_key = Config.SECRET_KEY

app.register_blueprint(auth_bp)
app.register_blueprint(appointment_bp)
app.register_blueprint(doctor_bp)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    return render_template("dashboard.html", name=session["name"])

if __name__ == "__main__":
    app.run(debug=True)