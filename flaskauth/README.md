

# Flask-Login Authentication

This project demonstrates how to implement user authentication using Flask-Login in a Flask web application.

## Introduction

Flask-Login provides user session management for Flask. It handles the common tasks of logging in, logging out, and remembering your users' sessions over extended periods of time.

## Features

Flask-Login will:
- Store the active user’s ID in the Flask Session, and let you easily log them in and out.
- Let you restrict views to logged-in (or logged-out) users using `login_required`.
- Handle the normally-tricky “remember me” functionality.
- Help protect your users’ sessions from being stolen by cookie thieves.

However, it does not:
- Impose a particular database or other storage method on you. You are entirely in charge of how the user is loaded.
- Restrict you to using usernames and passwords, OpenIDs, or any other method of authenticating.
- Handle permissions beyond “logged in or not.”
- Handle user registration or account recovery.

## Installation

1. **Create and activate a virtual environment**:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

2. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Run the application**:
    ```sh
    export FLASK_APP=app.py
    export FLASK_ENV=development
    flask run
    ```

2. **Open your browser and navigate to**:
    ```
    http://127.0.0.1:5000/
    ```

## Project Structure

```
flask-login-authentication/
│
├── app.py                  # Main application file
├── models.py               # Database models
├── forms.py                # Forms for user input
├── routes.py               # Application routes
├── templates/              # HTML templates
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   └── home.html
├── static/                 # Static files (CSS, JS, images)
│   └── style.css
├── requirements.txt        # Python dependencies
└── README.md               # Project README file
```


