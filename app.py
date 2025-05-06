from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import os
from readSensor import SensorReader

app = Flask(__name__)
app.secret_key = 'some_secret_key'  # Required for session management

# Initialize data.txt if it doesn't exist
if not os.path.exists('data.txt'):
    open('data.txt', 'w').close()

sensor = SensorReader()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        with open('users.txt', 'r') as f:
            for line in f:
                user, pwd = line.strip().split(':')
                if user == username and pwd == password:
                    session['logged_in'] = True
                    return redirect(url_for('dashboard'))
        return render_template('login.html', error='Invalid credentials')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session['logged_in'] = False
    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('dashboard.html')

@app.route('/data')
def data():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    data = []
    if os.path.exists('data.txt'):
        with open('data.txt', 'r') as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    timestamp, temp, power = parts
                    data.append({'timestamp': timestamp, 'temperature': float(temp), 'power': float(power)})
    return render_template('data.html', data=data)

@app.route('/get_data')
def get_data():
    data = sensor.get_current_data()
    with open('data.txt', 'a') as f:
        f.write(f"{data['timestamp']},{data['temperature']},{data['power']}\n")
    return jsonify(data)

@app.route('/save_data', methods=['POST'])
def save_data():
    data = sensor.get_current_data()
    with open('data.txt', 'a') as f:
        f.write(f"{data['timestamp']},{data['temperature']},{data['power']}\n")
    return 'Data saved'

if __name__ == '__main__':
    app.run(debug=True)