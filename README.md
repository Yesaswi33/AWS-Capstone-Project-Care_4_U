# 🏥 Care_4_U Hospitals – Doctor Appointment Management System

### AWS Capstone Project

**Care_4_U Hospitals** is a full-stack, cloud-ready hospital appointment management system developed using **Flask, HTML, and CSS**.  
The application simplifies doctor appointment scheduling while demonstrating real-world **AWS cloud deployment concepts** as part of an academic capstone project.

---

## 📌 Project Description

The **Care_4_U Hospitals System** provides an intuitive platform for patients to:

* Browse doctors by department and specialization  
* Schedule and manage appointments digitally  
* Access a responsive and clean frontend interface

The backend is designed with scalability in mind and is ready for deployment on **AWS infrastructure**.  
This project emphasizes **cloud readiness, modular backend architecture, and deployment best practices**, making it ideal for learning and demonstrating AWS skills.

---

## ✨ Key Features

### 👤 Patient Module

* Patient registration and secure login  
* Browse doctors by specialization  
* Book doctor appointments  
* Appointment booking form includes:  
  * Patient personal details  
  * Department selection  
  * Doctor preference  
  * Date and time slot  
* Responsive, mobile-friendly UI

### 👨‍⚕️ Doctor Module

* Doctor listing page with profile cards  
* View specialization and experience  
* Book appointments directly from doctor profiles  

### 🛠️ Admin Dashboard

* Centralized admin dashboard for hospital management  
* View daily appointments  
* Monitor patient and doctor statistics  
* Revenue overview (static for demo)  
* Quick admin actions  
* *(Role-based admin authentication planned)*

---

## 🧑‍💻 Technology Stack

| Layer           | Technology                                           |
| --------------- | --------------------------------------------------- |
| Backend         | Python (Flask)                                      |
| Frontend        | HTML5, CSS3                                         |
| Styling         | Custom CSS (Healthcare Theme)                       |
| Authentication  | Flask Sessions                                      |
| Version Control | Git & GitHub                                        |
| Cloud Platform  | AWS (EC2, IAM, DynamoDB, SNS – planned/implemented)|

---

## 📂 Project Structure

Care_4_U-Hospitals/
│
├── app.py
├── README.md
├── .gitignore
│
├── templates/
│ ├── index.html
│ ├── login.html
│ ├── register.html
│ ├── doctors.html
│ ├── appointments.html
│ ├── admin_dashboard.html
│ ├── about.html
│ └── contact.html
│ ├── doctor_ananya.html
│ ├── doctor_aarav.html
│ ├── doctor_rohan.html
│ ├── doctor_priya.html
│ ├── doctor_aarohi.html
│ ├── doctor_kabir.html
│ ├── doctor_meera.html
│ ├── doctor_sameer.html
│ ├── doctor_anika.html
│ ├── doctor_arjun.html
│ ├── doctor_nisha.html
│ └── doctor_vikram.html
│
├── static/
│ └── css/
│ └── style.css
│
└── venv/ (ignored in Git)

yaml
Copy code

---

## 🔐 Authentication & Session Flow

* Users can register and log in securely  
* Flask sessions are used to maintain login state  
* Admin access control planned for future role-based functionality

---

## 🎯 Project Objectives

* Build a real-world hospital appointment system  
* Implement Flask routing, templates, and session management  
* Design professional UI without frontend frameworks  
* Prepare the application for AWS deployment  
* Follow industry-standard project structure and security practices

---

## ☁️ AWS Deployment Plan

* Deploy the Flask backend on **AWS EC2**  
* Configure **Gunicorn** and **Nginx** for production  
* Use environment variables for secure configuration  
* Assign **IAM roles** for secure service access  
* Integrate **DynamoDB** for data storage and **SNS** for notifications  

---

## 🔮 Future Enhancements

* Role-based admin authentication  
* Database integration (DynamoDB / RDS)  
* Full doctor management (CRUD operations)  
* Appointment rescheduling and cancellation  
* Email and SMS notifications  
* File/document storage using **AWS S3**  
* Monitoring and alerts with **AWS CloudWatch**  

---

## 👤 Author

**Yesaswi Madabattula**  
🎓 B.Tech – Artificial Intelligence & Machine Learning  
📍 Andhra Pradesh, India  
🔗 GitHub: [https://github.com/Yesaswi33](https://github.com/Yesaswi33)

---

## 📌 Note

This project is developed as part of an **AWS Capstone / Internship Project** to demonstrate cloud-based application deployment, modular backend development, and system design principles.  
It is a complete hospital management and appointment scheduling platform ready for future AWS deployment.
