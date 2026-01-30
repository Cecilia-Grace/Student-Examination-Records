Student Examination Records API

A Django-based backend system for managing and tracking student performance and course units. This project emphasizes robust API design, data management, and backend architecture.

Features

RESTful API endpoints for managing:

Students

Examinations

Course units

CRUD operations fully supported via the API

Data validation and error handling implemented

Designed for seamless integration with frontend applications or automated scripts

Technologies Used

Python 3.x

Django & Django REST Framework

MySQL (or any SQL-based database)

Environment variables for secure configuration (SECRET_KEY, DB credentials)

API Endpoints
Endpoint	Method	Description
/students/	GET, POST	List all students or add a new student
/students/<id>/	GET, PUT, DELETE	Retrieve, update, or delete a student
/examinations/	GET, POST	List or create examination records
/examinations/<id>/	GET, PUT, DELETE	Manage a specific examination record
/course-units/	GET, POST	List or create course units

All endpoints are authenticated and secured where necessary.

Live API

The backend API is hosted and accessible at: https://studentexaminationrecords.pythonanywhere.com/

Quick Start (test locally)
git clone <repo-url>
cd Student_Examination_Records
python -m venv venv
source venv/bin/activate  # Linux/macOS
# OR venv\Scripts\activate  # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver