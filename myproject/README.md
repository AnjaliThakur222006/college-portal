# College Portal - Student Management System

A Django-based web application for managing students, courses, and enrollments with full CRUD operations.

## Features

- **Student Management** — Add, view, update, and delete student records (name, email, enrollment date)
- **Course Management** — Create, update, and delete courses with start/end dates and descriptions
- **Enrollment Tracking** — Many-to-many relationship between students and courses via enrollment model
- **Responsive UI** — Clean Bootstrap-based templates for all pages

## Quick Start

```bash
# Clone & setup
git clone https://github.com/AnjaliThakur222006/college-portal.git
cd college-portal
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # Linux/macOS

# Install & run
pip install django
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## Author

**Anjali Thakur** — JG University

---

*Built with Django • 2025*

