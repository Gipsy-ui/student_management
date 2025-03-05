# Student Management System or student_management

This is a Django-based Student Management System that allows users to manage student records with CRUD (Create, Read, Update, Delete) functionalities.

## Features
- Add, edit, and delete student records
- View student details
- User-friendly interface with Django templates
- Database integration using SQLite (default) or MySQL/PostgreSQL

## Prerequisites
Make sure you have the following installed:
- Python (>=3.8)
- Django (>=4.0)
- Git
- Virtual Environment (optional but recommended)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Gipsy-ui/student_management.git
cd student_management/StudentManagement
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply Migrations
```bash
python manage.py migrate
```

### 5. Create a Superuser (For Admin Access)
```bash
python manage.py createsuperuser
```
Follow the prompts to set up an admin username and password.

### 6. Run the Server
```bash
python manage.py runserver
```
Access the app at: `http://127.0.0.1:8000/`

## Database Configuration (Optional)
By default, the project uses SQLite. To use MySQL or PostgreSQL, update `settings.py` with the appropriate database credentials.

## Contributing
1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m "Added new feature"`)
4. Push to GitHub (`git push origin feature-branch`)
5. Create a Pull Request

## License
This project is licensed under the MIT License.

