# Student REST API

A simple Django REST Framework project for managing student records.  
This API uses token-based authentication and provides protected endpoints to list and create students.

## Features

- Built with Django and Django REST Framework
- Token authentication using `rest_framework.authtoken`
- Protected API endpoints
- SQLite database for local development
- Django admin support for managing students
- Serializer-based validation for API input

## Student Model

The project includes a `Students` model with the following fields:

- `id`: Auto-generated primary key
- `name`: Student name
- `age`: Student age
- `description`: Short description about the student
- `enrolled_date`: Automatically set when the record is created

## API Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `GET` | `/` | List all students | Yes |
| `POST` | `/` | Create a new student | Yes |
| `POST` | `/api/auth/` | Generate an authentication token | No |
| `GET` | `/api/login/` | Browsable API login page | No |
| `GET` | `/admin/` | Django admin panel | Yes |

## Sample Student Payload

```json
{
  "name": "Rahul Sharma",
  "age": 21,
  "description": "Computer science student"
}
```

## Setup Instructions

### 1. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install django djangorestframework
```

### 3. Apply migrations

```bash
python3 manage.py migrate
```

### 4. Create an admin user

```bash
python3 manage.py createsuperuser
```

### 5. Start the development server

```bash
python3 manage.py runserver
```

The project will be available at:

```text
http://127.0.0.1:8000/
```

## Authentication

This project uses token authentication for the main API endpoint.

To get a token, send a `POST` request to:

```text
http://127.0.0.1:8000/api/auth/
```

Example:

```bash
curl -X POST http://127.0.0.1:8000/api/auth/ \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"yourpassword"}'
```

Example response:

```json
{
  "token": "your_generated_token"
}
```

Use the token in the `Authorization` header:

```text
Authorization: Token your_generated_token
```

## Example API Requests

### Get all students

```bash
curl http://127.0.0.1:8000/ \
  -H "Authorization: Token your_generated_token"
```

### Create a student

```bash
curl -X POST http://127.0.0.1:8000/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Token your_generated_token" \
  -d '{
    "name": "Ananya Patel",
    "age": 20,
    "description": "First-year engineering student"
  }'
```

## Admin Panel

You can manage student records through the Django admin panel:

```text
http://127.0.0.1:8000/admin/
```

Log in with the superuser account created using `createsuperuser`.

## Project Structure

```text
RESTAPI/
├── manage.py
├── README.md
├── restapp/
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   └── views.py
└── restapipro/
    ├── settings.py
    ├── urls.py
    └── views.py
```

## Current Scope

At the moment, the API supports:

- Listing all students
- Creating new students
- Token-based authentication
- Admin management

Update, delete, and automated test coverage have not been added yet.
