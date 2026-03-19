from flask import Flask, render_template, request, redirect
import sqlite3

def init_db():
    conn = sqlite3.connect('login.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS user (username TEXT, password TEXT)')
    cursor.execute('SELECT count(*) FROM user')
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO user (username, password) VALUES ('admin', 'admin')")
        cursor.execute("INSERT INTO user (username, password) VALUES ('guest', 'guest')")
        conn.commit()
    conn.close()

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    username = None
    password = None
    message = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username and password:
            conn = sqlite3.connect('login.db')
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM user WHERE username = '{username}' AND password = '{password}'")
            result = cursor.fetchone()
            conn.close()
            if username == 'admin' and result:
                    message = "ZLCSC{????h0w_u_Log1n_As_Adm1nistrAt0r????}"
            elif result:
                    message = "Login Successful!! But U R Not Admin..."
            else:
                message = "fail."
    return render_template('index.html', username=username, password=password, message=message)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)