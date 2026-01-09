# Simple CRUD Application

## Project Overview
This is a simple web application developed using **Python (Flask)** and **SQLite**.
The application allows users to **Sign Up, Login**, and perform **CRUD operations**
(Create, View, Update/Rename, Delete) on items.

This project is created as part of a software developer assessment.

---

## Features
- User Sign Up
- User Login
- Authentication using sessions
- Create an item
- View list of items
- Rename (Edit) an item
- Delete an item
- Logout

---

## Technology Used
- Python
- Flask
- SQLite
- SQLAlchemy
- HTML (basic)

---

## Database
- SQLite is used as the database
- Data is stored in a local file named `app.db`
- Tables:
  - `user`
  - `item`

---

## Setup Steps

1. Install Python (version 3 or above)

2. Clone the repository:
```bash
git clone <your-github-repository-link>
cd simple-crud-app

3. Install required libraries:
pip install flask flask-sqlalchemy werkzeug

4. Run the application:

python app.py

5. Open the application in browser:
http://127.0.0.1:5000

## How to Use the Application

1. Sign up with a username and password

2. Login using the registered credentials

3. After login, you will see the dashboard

4. You can:

    *Add a new item

    *View all items

    *Rename an item by clicking the Rename button

    *Delete an item

5. Logout from the application

## Basic Input Validation

> Empty username or password is not allowed

> Empty item cannot be added

> Empty item name cannot be saved during rename

> Validation is handled on frontend and backend

## Test Cases

1. User can register successfully

2. User can login with valid credentials

3. User cannot submit empty login or signup form

4. User can add an item

5. User can view list of items

6. User can rename an item

7. User can delete an item

8. User can logout successfully

