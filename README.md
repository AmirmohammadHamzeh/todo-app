# 🚀 Todo Manager -- Django REST API

> **A clean, modern, and fully documented Todo Management API** built
> with **Django**, **Django REST Framework**, **JWT Authentication**,
> and **PostgreSQL Full-Text Search**.\
> Designed for efficient task management with labels, priorities,
> validations, and secure user-specific access control.

## 📋 Table of Contents

-   [About the Project](#-about-the-project)
-   [Features](#-features)
-   [API Overview](#-api-overview)
-   [Tech Stack](#-tech-stack)
-   [Project Structure](#-project-structure)
-   [Installation](#-installation)
-   [Environment Variables](#-environment-variables)
-   [Usage](#-usage)
-   [Screenshots](#-screenshots)
-   [Contributing](#-contributing)
-   [License](#-license)
-   [Contact](#-contact)

## 💡 About the Project

**Todo Manager** is a fully-featured REST API designed to provide a
clean, scalable, and production-ready backend for managing personal or
team tasks.

The system includes:

-   A **custom user model** with JWT authentication\
-   Full CRUD operations for **todos**\
-   Support for **labels**, **priorities**, and **task statuses**\
-   **PostgreSQL Full-Text Search** for fast, weighted querying\
-   Clean, auto-generated API documentation using **Swagger** &
    **Redoc**\
-   Data validation at both **serializer** and **model** levels

## ✨ Features

### 🔐 Authentication & User Management

-   Custom User model (email-based)
-   JWT Authentication (Access + Refresh tokens)
-   User registration & login
-   Retrieve current authenticated user (`/users/me/`)

### 📝 Todo Features

-   Create, update, delete, and list todos
-   Priority system: **low / medium / high**
-   Connect labels to todos (Many-to-Many)
-   Automatic fields such as:
    -   `status`\
    -   `is_overdue`\
    -   `days_until_due`
-   User-specific task isolation

### 🏷 Label Features

-   Create, update, delete labels
-   Assign multiple labels to each todo

### 🔎 Advanced Features

-   Weighted Full-Text Search on title & description\
-   Swagger & Redoc documentation\
-   Built-in validation for dates and business rules

## 🔌 API Overview

Swagger UI:\
`http://localhost:8000/swagger/`

Redoc:\
`http://localhost:8000/redoc/`

## 🧰 Tech Stack

Backend: Django, DRF\
Database: PostgreSQL\
Auth: JWT (SimpleJWT)\
Search: PostgreSQL FTS\
Docs: Swagger / Redoc

## 📁 Project Structure

    .
    ├── authentication
    ├── todos
    ├── todolist
    ├── docker-compose.yml
    └── manage.py

## ⚙️ Installation

``` bash
git clone https://github.com/AmirmohammadHamzeh/todo-app.git
cd todo-app
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 🔧 Environment Variables

Create a `.env` file:

    SECRET_KEY="your-secret-key"
    DEBUG=True
    POSTGRES_DB="todo_db"
    POSTGRES_USER="admin"
    POSTGRES_PASSWORD="password"
    POSTGRES_HOST="localhost"
    POSTGRES_PORT=5432

## 🚀 Usage

``` bash
python manage.py migrate
python manage.py runserver
```

## 🖼 Screenshots

Coming soon...

## 🤝 Contributing

Fork → Branch → Commit → PR

## 📜 License

MIT License

## 📬 Contact

Author: **Amir Mohammad Hamzeh**\
Email: **amirmohammadhamzeh@outlook.com**\
GitHub: https://github.com/AmirmohammadHamzeh
