# IoT Dashboard Project

This is a simple IoT dashboard built with Flask, HTML, CSS, and JavaScript. It displays live CPU temperature and power consumption data, allows users to log in, view historical data, and save data manually. The project is designed with a 3D aesthetic for buttons, charts, and tables, providing an elegant user interface.

## Directory Structure

```
project/
├── app.py
├── readSensor.py
├── users.txt
├── data.txt (created at runtime)
├── static/
│   ├── style.css
│   ├── javascript.js
│   └── graph.js
└── templates/
    ├── index.html
    ├── login.html
    ├── dashboard.html
    └── data.html
```

## Dependencies

- [Python 3.x](https://www.python.org/downloads/)
- [Flask](https://flask.palletsprojects.com/) (install via pip)
- [Chart.js](https://www.chartjs.org/) (included via CDN in dashboard.html)

## Installation

1. Clone the repository or download the project files to your local machine.
2. Install Flask if not already installed:
   ```
   pip install flask
   ```
3. Ensure Python 3.x is installed on your system.

## Running the Application

1. Navigate to the project directory in your terminal.
2. Run the Flask application:
   ```
   python app.py
   ```
3. Open a web browser and go to `[invalid url, do not cite]

## Usage

- **Login**: From the index page (`index.html`), click "Login" and use `admin` as the username and `admin122` as the password. Incorrect credentials will display an error message.
- **Dashboard**: Access `dashboard.html` to view live CPU temperature and power consumption data, updated every second. Data is visualized in two line graphs (temperature vs. time and power vs. time). Click the "Save Data" button to manually save the current data to `data.txt`. Data is also automatically saved every second.
- **View Data**: Click "View Data" from the index page to access `data.html`, which displays historical data in a table format with columns for timestamp, temperature, and power consumption.
- **Logout**: Click "Logout" to end the session and return to the index page.

## Notes

- **Mock Data**: This project uses simulated data for temperature and power consumption, generated in `readSensor.py`. For a real IoT setup with a Raspberry Pi, modify `readSensor.py` to read from actual sensors (e.g., `/sys/class/thermal/thermal_zone0/temp` for CPU temperature).
- **File Creation**: The `data.txt` file is automatically created when the application starts if it does not already exist.
- **User Credentials**: The `users.txt` file contains the initial user credentials: `admin:admin122`.
- **Design**: The interface features a 3D look for buttons, charts, and tables, achieved through CSS box-shadows and styling in `style.css`.
- **JavaScript**: The `javascript.js` file handles live data updates and the save button functionality, while `graph.js` configures Chart.js for graphing.

## File Descriptions

| File | Description |
|------|-------------|
| `app.py` | Flask application handling routing and server-side logic. |
| `readSensor.py` | Python class simulating CPU temperature and power consumption data. |
| `users.txt` | Stores user credentials (`admin:admin122`). |
| `data.txt` | Stores timestamped temperature and power data (created at runtime). |
| `static/style.css` | CSS for 3D and elegant design of buttons, charts, and tables. |
| `static/javascript.js` | JavaScript for live data updates and save button functionality. |
| `static/graph.js` | JavaScript for initializing and configuring Chart.js graphs. |
| `templates/index.html` | Main page with navigation links (Login, Logout, View Data). |
| `templates/login.html` | Login page with form and error handling. |
| `templates/dashboard.html` | Dashboard displaying live data and graphs. |
| `templates/data.html` | Page displaying historical data in a table. |

## Extending the Project

To adapt this project for real IoT hardware:
1. Connect a temperature sensor to a Raspberry Pi.
2. Update `readSensor.py` to read from the sensor (e.g., using GPIO libraries).
3. Optionally, integrate with a MySQL database instead of `data.txt` for persistent storage.
4. Use IoT platforms like [ThingSpeak](https://thingspeak.com/) for cloud integration.

## Troubleshooting

- **Flask Not Found**: Ensure Flask is installed (`pip install flask`).
- **Port Conflict**: If port 5000 is in use, change the port in `app.py` (e.g., `app.run(port=5001)`).
- **No Data in Table**: Verify `data.txt` exists and contains valid data.
- **Graph Not Displaying**: Check the Chart.js CDN link in `dashboard.html` and ensure JavaScript is enabled in the browser.

## License

This project is licensed under the MIT License. See the [LICENSE.md](https://opensource.org/licenses/MIT) file for details.