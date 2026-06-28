from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'portfolio_secret'

def init_db():
    conn = sqlite3.connect('accounts.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users 
                 (id INTEGER PRIMARY KEY, name TEXT, email TEXT UNIQUE, password TEXT)''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    try:
        conn = sqlite3.connect('accounts.db')
        c = conn.cursor()
        c.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", 
                  (name, email, password))
        conn.commit()
        conn.close()
        flash('Account created! You can login now.')
        return redirect(url_for('home'))
    except:
        flash('Email already exists.')
        return redirect(url_for('home'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)