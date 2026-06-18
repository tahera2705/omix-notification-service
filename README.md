# Omix Notification Service

A production-ready Notification Service built with FastAPI, SQLAlchemy, SQLite, and JWT Authentication.

## Live Demo

**Base URL**

https://omix-notification-service.onrender.com

**Swagger Documentation**

https://omix-notification-service.onrender.com/docs

**GitHub Repository**

https://github.com/tahera2705/omix-notification-service

---

## Features

### Authentication

* User Registration
* User Login
* JWT Authentication
* Protected Routes

### Notifications

* Create Notification
* View All Notifications
* View Notification By ID
* Update Notification Status
* Delete Notification
* Search Notifications By Title
* Filter Notifications By Status

### Notification Fields

* Title
* Message
* Channel (EMAIL / SMS / PUSH)
* Status (pending / sent / failed)
* Created At Timestamp

---

## Tech Stack

* FastAPI
* SQLAlchemy
* SQLite
* JWT Authentication
* Pydantic
* Uvicorn
* Docker
* Render

---

## Installation

### Clone Repository

```bash
git clone https://github.com/tahera2705/omix-notification-service.git
cd omix-notification-service
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
DATABASE_URL=sqlite:///./omix.db
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Run Application

```bash
uvicorn app.main:app --reload
```

Application:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### Authentication

| Method | Endpoint  |
| ------ | --------- |
| POST   | /register |
| POST   | /login    |

### Notifications

| Method | Endpoint              |
| ------ | --------------------- |
| GET    | /notifications        |
| POST   | /notifications        |
| GET    | /notifications/{id}   |
| PUT    | /notifications/{id}   |
| DELETE | /notifications/{id}   |
| GET    | /notifications/search |
| GET    | /notifications/status |

---

## Docker Support

Build Docker Image:

```bash
docker build -t omix-notification-service .
```

Run Container:

```bash
docker run -p 8000:8000 omix-notification-service
```

---

## Deployment

The application is deployed on Render and automatically redeploys when changes are pushed to the GitHub repository.

Live URL:

https://omix-notification-service.onrender.com

---

## Project Structure

```text
app/
├── api/
├── core/
├── db/
├── models/
├── schemas/
├── main.py

tests/
├── test_auth.py
├── test_notifications.py
```

---

## Author

Tahera Singaporewala


