# django-banao-technologies-task-one
## User Authentication and Dashboard Application

## Superuser Credentials

username: admin
password: admin@123

## Description
This is a web application built for an internship shortlisting task. The application enables **signup and login functionality** for multiple types of users and redirects them to their respective dashboards after login.  

Custom features include:  
- Website loader  
- Interactive GUI  
- Responsive design (mobile and desktop)  
- Django messages module for notifications  

Built using **Django**, **Tailwind CSS**, and **JavaScript**.  

---

## Features

### Types of Users
- **Patient**  
- **Doctor**  

### Signup Form
- First Name, Last Name, Profile Picture  
- Username, Email ID  
- Password, Confirm Password  
- Address (Line 1, City, State, Pincode)  

**Validation:** Password and Confirm Password must match.  

### Login
- Users log in with username and password  
- Redirects to respective dashboards  

### Dashboards
- Displays user details from signup  
- Simple and functional  

### Custom Features
- Website loader on page load  
- Interactive GUI with smooth transitions  
- Fully responsive design  
- Django messages module for notifications  

---

## Technology Stack
- **Backend:** Django  
- **Frontend:** HTML, Tailwind CSS, JavaScript  
- **Database:** SQLite  

---

## Snapshots
- **Home Page**
- <img width="1366" height="768" alt="Medi_homepage" src="https://github.com/user-attachments/assets/12640bd8-4653-4039-bdd9-4a0af1f8b4dd" />

- **SignUp Page**
- <img width="1366" height="768" alt="Medi_signup" src="https://github.com/user-attachments/assets/fbb9777f-989a-4b74-afb2-0ac14b3c680e" />

- **Login Page**
- <img width="1366" height="768" alt="Medi_login" src="https://github.com/user-attachments/assets/bb845c9e-717b-4dca-bd23-8a6dcc997e44" />

- **Dashboard of Patient**
- <img width="1366" height="768" alt="Medi_patient_dashboard" src="https://github.com/user-attachments/assets/934b1608-180d-471a-8288-421e54a39733" />

- **Dashboard of Doctors**
- <img width="1362" height="570" alt="Medi_doctor_dashboard" src="https://github.com/user-attachments/assets/a1e81e6a-74a6-4550-97d1-1670a51b5e9b" />

## Commands to Run the Project

**Run the project:**  

### 1. Run Project
```bash
# Create virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run database migrations
python manage.py makemigrations
python manage.py migrate

# Start servers

# Start Django server
python manage.py runserver

# Start Tailwind CSS server
python manage.py tailwind start






