# 🏥 Patient Appointment Management System

A web-based **Patient Appointment Management System** developed using **Python Flask, MongoDB, HTML, CSS, JavaScript, and Jinja2 templates**.

The system provides a simple and efficient platform for patients to find doctors, select available appointment slots, book appointments, and manage their bookings. Administrators can manage doctors, monitor all appointments, and view appointment analytics through an admin dashboard.

---

## 📌 Project Overview

The Patient Appointment Management System is designed to reduce the difficulties associated with traditional hospital appointment systems.

In a traditional appointment system, patients may need to visit the hospital or call the reception desk to book an appointment. This can result in:

- Long waiting times
- Manual record keeping
- Appointment conflicts
- Difficulty managing doctor schedules
- Difficulty tracking appointments
- Increased administrative workload

This project provides a centralized web application that digitizes the appointment booking and management process.

---

## 🎯 Objectives

The main objectives of this project are:

- To provide an online appointment booking system.
- To reduce patient waiting time.
- To provide available doctor time slots dynamically.
- To prevent double booking of appointment slots.
- To provide secure user authentication.
- To implement role-based access for patients and administrators.
- To allow administrators to manage doctors.
- To allow administrators to view all appointments.
- To provide appointment analytics.
- To provide a simple and user-friendly interface.

---

## ✨ Features

### 👤 Patient Features

- Patient registration
- Secure patient login
- Patient dashboard
- View available doctors
- View doctor specialization
- Select appointment date
- View available time slots
- Book an appointment
- View booked appointments
- Cancel appointments
- Book a new appointment after cancellation
- Logout

---

### 👨‍💼 Admin Features

- Secure admin login
- Admin dashboard
- Manage doctors
- Add doctors
- Edit doctor information
- Delete doctors
- View all appointments
- View patient names
- View doctor names
- Monitor appointment status
- Appointment analytics
- Doctor-wise appointment statistics
- Logout

---

## 📊 Analytics Dashboard

The administrator can access an analytics dashboard containing information such as:

- Total number of doctors
- Total number of patients
- Total number of appointments
- Doctor-wise appointment statistics
- Graphical appointment analysis

The analytics dashboard helps administrators understand appointment activity and system usage.

---

## 🔐 Authentication and Authorization

The system uses authentication and role-based authorization.

There are two types of users:

### Patient

Patients can:

- View doctors
- Book appointments
- View their appointments
- Cancel appointments

### Admin

Administrators can:

- Manage doctors
- View all appointments
- Access analytics
- Monitor the system

Unauthorized users are prevented from accessing protected pages using Flask decorators and session-based authentication.

---

## 🛡️ Security

The project includes basic security mechanisms such as:

- Password hashing using `bcrypt`
- Session-based authentication
- Login-required routes
- Admin-only protected routes
- Role-based access control
- Appointment ownership through patient IDs
- MongoDB ObjectId-based references

Passwords are never stored as plain text.

---

# 🛠️ Technologies Used

## Frontend

- HTML5
- CSS3
- Jinja2 Templates

## Backend

- Python
- Flask

## Database

- MongoDB
- PyMongo

## Authentication

- Flask Session
- Flask-Bcrypt / bcrypt

## Development Tools

- Visual Studio Code
- Google Chrome
- MongoDB
- MongoDB Compass

---

# 🏗️ System Architecture

The application follows a simple web application architecture:

```text
                 ┌─────────────────────┐
                 │       User          │
                 │ Patient / Admin     │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │      Frontend       │
                 │ HTML / CSS          │
                 │ Jinja2 Templates    │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │       Flask        │
                 │     Backend        │
                 │ Routes + Logic     │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │      MongoDB        │
                 │      Database       │
                 └─────────────────────┘
