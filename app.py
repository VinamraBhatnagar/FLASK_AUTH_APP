from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'super_secret_key')

DATABASE = 'database.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Initialize the database when the app starts
init_db()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')

        # Task 1: Backend Validation
        
        # 1. Name should not be empty
        if not name:
            flash('Name should not be empty', 'danger')
            return render_template('register.html', name=name, email=email)
        
        # 2. Email should not be empty
        if not email:
            flash('Email should not be empty', 'danger')
            return render_template('register.html', name=name, email=email)
        
        # 3. Password should not be empty
        if not password:
            flash('Password should not be empty', 'danger')
            return render_template('register.html', name=name, email=email)
        
        # 5. Password should be at least 6 characters
        if len(password) < 6:
            flash('Password should be at least 6 characters', 'danger')
            return render_template('register.html', name=name, email=email)

        conn = get_db_connection()
        
        # 4. Email should be unique
        existing_user = conn.execute('SELECT * FROM users WHERE email = ?', (email,)).fetchone()
        if existing_user:
            flash('Email is already registered', 'danger')
            conn.close()
            return render_template('register.html', name=name, email=email)

        # If all validations pass, hash password and save user
        hashed_password = generate_password_hash(password)
        conn.execute('INSERT INTO users (name, email, password) VALUES (?, ?, ?)', (name, email, hashed_password))
        conn.commit()
        conn.close()

        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port, debug=True)
