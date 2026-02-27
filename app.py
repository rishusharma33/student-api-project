from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Database connection
def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root123@",  # 🔴 change this
        database="users_db"
    )
    return connection


# 1️⃣ Hello Route
@app.route('/hello')
def hello():
    return "Hello World!"


# 2️⃣ Show all users
@app.route('/users')
def users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM users")
    all_users = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return render_template('users.html', users=all_users)


# 3️⃣ Add user
@app.route('/users/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        role = request.form['role']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute(
            "INSERT INTO users (name, email, role) VALUES (%s, %s, %s)",
            (name, email, role)
        )
        conn.commit()
        
        cursor.close()
        conn.close()
        
        return redirect(url_for('users'))
    
    return render_template('add_user.html')


# 4️⃣ User by ID
@app.route('/users/<int:user_id>')
def user_detail(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user = cursor.fetchone()
    
    cursor.close()
    conn.close()
    
    if user:
        return render_template('user_detail.html', user=user)
    else:
        return "User not found", 404


if __name__ == '__main__':
    app.run(debug=True)