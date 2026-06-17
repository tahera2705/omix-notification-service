# Omix Notification Service

A FastAPI-based Notification Service with JWT Authentication, SQLite, and SQLAlchemy.

## Features

- User Registration
- User Login
- JWT Authentication
- Create Notification
- View All Notifications
- View Notification By ID
- Update Notification Status
- Delete Notification
- Search Notifications by Title
- Filter Notifications by Status
- Swagger API Documentation

## Tech Stack

- FastAPI
- SQLAlchemy
- SQLite
- JWT Authentication
- Pydantic
- Uvicorn

## Installation

```bash
git clone https://github.com/tahera2705/omix-notification-service.git
cd omix-notification-service
```

Create virtual environment:

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
uvicorn app.main:app --reload
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

## API Endpoints

### Authentication

- POST /register
- POST /login

### Notifications

- GET /notifications
- POST /notifications
- GET /notifications/{id}
- PUT /notifications/{id}
- DELETE /notifications/{id}
- ## Live Demo

Base URL:
https://omix-notification-service.onrender.com

Swagger Documentation:
https://omix-notification-service.onrender.com/docs

GitHub Repository:
https://github.com/tahera2705/omix-notification-service

## Features

* User Registration
* User Login with JWT Authentication
* Create Notification
* View All Notifications
* View Notification By ID
* Search Notifications By Title
* Filter Notifications By Status
* Update Notification Status
* Delete Notification
* SQLite Database
* FastAPI + SQLAlchemy
* Swagger/OpenAPI Documentation
* Render Deployment

- GET /notifications/search
- GET /notifications/status

## Author

Tahera Singaporewala
