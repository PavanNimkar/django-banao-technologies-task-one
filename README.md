# django-banao-technologies-task-one
## User Authentication and Dashboard Application

## Description
This is a web application built for an internship shortlisting task. The application enables **signup and login functionality** for multiple types of users and redirects them to their respective dashboards after login.  

Custom features include:  
- Website loader  
- Interactive GUI  
- Responsive design (mobile and desktop)  
- Django messages module for notifications 
- Page Not Found Page 

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






