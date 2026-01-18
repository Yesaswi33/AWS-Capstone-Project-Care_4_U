# 🏥 Care_4_U Hospitals – Doctor Appointment Management System

### AWS Capstone Project

Care_4_U Hospitals is a full-stack, cloud-oriented hospital appointment management system developed using **Flask, HTML, and CSS**.
The application focuses on simplifying the doctor appointment process while demonstrating real-world **AWS cloud deployment concepts** as part of an academic capstone project.

---

## 📌 Project Description

The **Care_4_U Hospitals System** provides a simple and intuitive platform for patients to view doctors, schedule appointments, and manage bookings digitally.
The system is designed with a clean frontend interface and a scalable backend architecture, making it suitable for deployment on AWS infrastructure.

This project emphasizes **cloud readiness, modular backend design, and deployment best practices**, making it ideal for learning and demonstrating AWS fundamentals.

---

## ✨ Key Features

### 👤 Patient Functionalities

* Patient registration and secure login
* Browse doctors by department/specialization
* Book doctor appointments
* Appointment booking form including:

  * Patient details
  * Department selection
  * Doctor preference
  * Date and time slot
* Responsive and user-friendly UI

### 👨‍⚕️ Doctor Features

* Doctor listing page
* Doctor profile cards with specialization
* Direct appointment booking option

### 🛠️ Admin Dashboard

* Centralized admin dashboard
* View daily appointment records
* Patient and doctor statistics overview
* Revenue summary (static demo)
* Administrative quick actions
* *(Role-based admin authentication planned)*

---

## 🧑‍💻 Technology Stack

| Layer           | Technology                                          |
| --------------- | --------------------------------------------------- |
| Backend         | Python (Flask)                                      |
| Frontend        | HTML5, CSS3                                         |
| Styling         | Custom CSS (Healthcare Theme)                       |
| Authentication  | Flask Sessions                                      |
| Version Control | Git & GitHub                                        |
| Cloud Platform  | AWS (EC2, IAM, DynamoDB, SNS – planned/implemented) |

---

## 📂 Project Structure

```
Care_4_U-Hospitals/
│
├── app.py
├── README.md
├── .gitignore
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── doctors.html
│   ├── appointments.html
│   ├── admin_dashboard.html
│   ├── about.html
│   └── contact.html
│
├── static/
│   └── css/
│       └── style.css
│
└── venv/   (ignored in Git)
```

---

## 🔐 Authentication & Session Flow

* Users can register and log in securely
* Flask sessions are used to maintain login state
* Admin access control is planned for future enhancement

---

## 🎯 Project Objectives

* Develop a real-world hospital appointment system
* Implement Flask routing, templates, and session handling
* Design a professional UI without frontend frameworks
* Prepare the application for AWS deployment
* Follow industry-standard project organization and security practices

---

## ☁️ AWS Deployment Plan

* Deploy Flask application on **AWS EC2**
* Configure **Gunicorn** and **Nginx**
* Use environment variables for secure configuration
* Implement IAM roles for service access
* Integrate DynamoDB and SNS for data storage and notifications

---

## 🔮 Future Enhancements

* Role-based admin authentication
* Database integration (DynamoDB / RDS)
* Doctor management (CRUD operations)
* Appointment rescheduling and cancellation
* Email/SMS notifications
* AWS S3 for document storage
* Monitoring using AWS CloudWatch

---

## 👤 Author

**Yesaswi Madabattula**
🎓 B.Tech – Artificial Intelligence & Machine Learning
📍 Andhra Pradesh India
🔗 GitHub: [https://github.com/Yesaswi33](https://github.com/Yesaswi33)

---

## 📌 Note

This project is developed as part of an **AWS Capstone / Internship Project** to demonstrate cloud-based application deployment, backend development, and system design principles.
