<<<<<<< HEAD
# app.py
from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3, os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'subhi123'
UPLOAD_FOLDER = 'static/docs'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ---------- DB Initialization ----------
def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT,
                        password TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS posts (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT,
                        category TEXT,
                        title TEXT,
                        content TEXT,
                        link TEXT,
                        doc_path TEXT)''')
    conn.commit()
    conn.close()

# ---------- Routes ----------
@app.route('/')
def home():
    return render_template('login.html')

@app.route('/register')
def register_page():
    return render_template('register.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    conn.close()
    if user:
        session['username'] = username
        return redirect(url_for('dashboard'))
    else:
        return "Invalid credentials"

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()
    return redirect(url_for('home'))

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('home'))
    search = request.args.get('search', '').lower()
    category = request.args.get('category', '')
    query = "SELECT * FROM posts WHERE 1=1"
    params = []
    if category:
        query += " AND category = ?"
        params.append(category)
    if search:
        query += " AND (LOWER(username) LIKE ? OR LOWER(title) LIKE ? OR LOWER(content) LIKE ?)"
        term = f"%{search}%"
        params += [term, term, term]
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query, params)
    posts = cursor.fetchall()
    conn.close()
    return render_template('dashboard.html', posts=posts)

@app.route('/add_post', methods=['POST'])
def add_post():
    if 'username' not in session:
        return redirect(url_for('home'))
    title = request.form['title']
    category = request.form['category']
    content = request.form['content']
    link = request.form['link']
    doc_file = request.files['doc']
    doc_path = ''
    if doc_file and doc_file.filename:
        filename = secure_filename(doc_file.filename)
        doc_path = os.path.join(UPLOAD_FOLDER, filename)
        doc_file.save(doc_path)
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO posts (username, category, title, content, link, doc_path) VALUES (?, ?, ?, ?, ?, ?)",
                   (session['username'], category, title, content, link, doc_path))
    conn.commit()
    conn.close()
    return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    init_db()
    import os
    port = int(os.environ.get('PORT', 5000))
=======
# app.py
from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3, os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'subhi123'
UPLOAD_FOLDER = 'static/docs'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ---------- DB Initialization ----------
def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT,
                        password TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS posts (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT,
                        category TEXT,
                        title TEXT,
                        content TEXT,
                        link TEXT,
                        doc_path TEXT)''')
    conn.commit()
    conn.close()

# ---------- Routes ----------
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')


@app.route('/register')
def register_page():
    return render_template('register.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    conn.close()
    if user:
        session['username'] = username
        return redirect(url_for('dashboard'))
    else:
        return "Invalid credentials"

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()
    return redirect(url_for('home'))

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('home'))
    search = request.args.get('search', '').lower()
    category = request.args.get('category', '')
    query = "SELECT * FROM posts WHERE 1=1"
    params = []
    if category:
        query += " AND category = ?"
        params.append(category)
    if search:
        query += " AND (LOWER(username) LIKE ? OR LOWER(title) LIKE ? OR LOWER(content) LIKE ?)"
        term = f"%{search}%"
        params += [term, term, term]
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query, params)
    posts = cursor.fetchall()
    conn.close()
    return render_template('dashboard.html', posts=posts)

@app.route('/add_post', methods=['POST'])
def add_post():
    if 'username' not in session:
        return redirect(url_for('home'))
    title = request.form['title']
    category = request.form['category']
    content = request.form['content']
    link = request.form['link']
    doc_file = request.files['doc']
    doc_path = ''
    if doc_file and doc_file.filename:
        filename = secure_filename(doc_file.filename)
        doc_path = os.path.join(UPLOAD_FOLDER, filename)
        doc_file.save(doc_path)
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO posts (username, category, title, content, link, doc_path) VALUES (?, ?, ?, ?, ?, ?)",
                   (session['username'], category, title, content, link, doc_path))
    conn.commit()
    conn.close()
    return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    init_db()
    import os
    port = int(os.environ.get('PORT', 5000))
>>>>>>> 852146f (Initial commit with all project files)
    app.run(host='0.0.0.0', port=port)