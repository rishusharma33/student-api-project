# Flask User Management System

## Overview
This project is a simple Flask web application that connects with MySQL to perform basic user management operations.

## Features
- /hello → Displays Hello World
- /users → View all users
- /users/add → Add new user
- /users/<id> → View individual user

## Tech Stack
- Python
- Flask
- MySQL
- HTML

## Database Setup

### Create Database
CREATE DATABASE users_db;

### Create Table
USE users_db;

CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100),
    role VARCHAR(50)
);

### Insert Sample Data
INSERT INTO users (name, email, role)
VALUES ('Rishi', 'rishi@gmail.com', 'Developer');

## How to Run

1. Install dependencies:
pip install -r requirements.txt

2. Update MySQL password in app.py

3. Run:
python app.py

4. Open:
http://127.0.0.1:5000/users