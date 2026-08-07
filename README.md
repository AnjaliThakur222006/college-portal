# College Portal - Student Management System

A Django-based web application for managing students, courses, and enrollments with full CRUD operations.

## Features

- **Student Management** — Add, view, update, and delete student records (name, email, enrollment date)
- **Course Management** — Create, update, and delete courses with start/end dates and descriptions
- **Enrollment Tracking** — Many-to-many relationship between students and courses via enrollment model
- **Responsive UI** — Clean Bootstrap-based templates for all pages

## Tech Stack

- **Backend:** Django 5.x (Python)
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Database:** SQLite (development) / PostgreSQL (production-ready)
- **ORM:** Django ORM with model forms

## Project Structure

```
college-portal/
├── college_portal/          # Main project settings & URLs
├── myproject/               # Django app with student & course CRUD
│   ├── student/
│   │   ├── View.py          # All views (home, student, course CRUD)
│   │   ├── models.py        # Student, Course, Enrollment models
│   │   ├── forms.py         # Django ModelForm for Student
│   │   ├── urls.py          # URL routing
│   │   ├── admin.py         # Admin panel registration
│   │   └── templates/       # HTML templates
│   └── manage.py            # Django management script
├── student/                 # Secondary student app
└── manage.py                # Root management script
```

## Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/AnjaliThakur222006/college-portal.git
   cd college-portal
   ```

2. **Create & activate virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # Windows
   source .venv/bin/activate  # Linux/macOS
   ```

3. **Install dependencies**
   ```bash
   pip install django
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Start the server**
   ```bash
   python manage.py runserver
   ```

6. **Open in browser**
   - Home: http://127.0.0.1:8000/
   - Students: http://127.0.0.1:8000/student/
   - Courses: http://127.0.0.1:8000/course/
   - Admin: http://127.0.0.1:8000/admin/

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Home page with student list |
| `/student/` | GET | View all students |
| `/add_student/` | GET/POST | Add new student |
| `/update_student/<id>/` | GET/POST | Update student |
| `/delete_student/<id>/` | GET | Delete student |
| `/course/` | GET | View all courses |
| `/add_course/` | GET/POST | Add new course |
| `/update_course/<id>/` | GET/POST | Update course |
| `/delete_course/<id>/` | GET | Delete course |

## Author

**Anjali Thakur** — JG University

---

*Built with Django • 2025*
