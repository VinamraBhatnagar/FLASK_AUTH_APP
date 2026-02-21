# FlaskAuthApp

This is a simple Flask application with a registration system that includes server-side validation.

## Features

- User Registration with validation:
  - Name, Email, and Password cannot be empty.
  - Email must be unique.
  - Password must be at least 6 characters.
- SQLite Database for storing users.
- Flash messages for validation errors and success notifications.

## Local Setup

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd FlaskAuthApp
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Open your browser and go to `http://127.0.0.1:5000`

## Deployment on Render

1. Push this code to a public GitHub repository.
2. Go to [Render](https://render.com/) and create a new **Web Service**.
3. Connect your GitHub repository.
4. Use the following settings:
   - **Environment**: Python
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
5. Click **Create Web Service**.
