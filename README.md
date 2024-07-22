# Urban Traffic Monitoring System

## Table of Contents

- [Introduction](#introduction)
- [Backend](#backend)
  - [Technologies Used](#technologies-used)
  - [Installation](#installation)
  - [Running the Server](#running-the-server)
  - [API Endpoints](#api-endpoints)
- [Frontend](#frontend)
  - [Technologies Used](#technologies-used-1)
  - [Installation](#installation-1)
  - [Running the Application](#running-the-application)
- [Data Visualization](#data-visualization)
  - [Power BI Dashboards](#power-bi-dashboards)
  - [React Native Charts](#react-native-charts)
- [Screenshots](#screenshots)
- [Conclusion](#conclusion)
- [License](#license)

## Introduction

The Urban Traffic Monitoring System is a comprehensive solution designed to help urban authorities monitor and manage traffic in real-time. It consists of a backend API built with Django and a mobile client application developed using React Native. The system integrates data visualization through Power BI to provide detailed analytics and insights.

## Backend

### Technologies Used

- Python
- Django
- Django REST Framework
- Django REST Framework SimpleJWT
- drf-yasg for API documentation
- SQLite (for development)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/dcosodev/urban_traffic_monitoring.git
   cd urban_traffic_monitoring/backend
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

### Running the Server

1. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

2. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

### API Endpoints

| Endpoint              | Method | Description                           |
|-----------------------|--------|---------------------------------------|
| /api/trafficflow/     | GET    | Get all traffic flows                 |
| /api/trafficflow/     | POST   | Create a new traffic flow             |
| /api/trafficflow/{id}/| GET    | Get a specific traffic flow           |
| /api/trafficflow/{id}/| PUT    | Update a specific traffic flow        |
| /api/trafficflow/{id}/| DELETE | Delete a specific traffic flow        |
| /api/trafficincident/ | GET    | Get all traffic incidents             |
| /api/trafficincident/ | POST   | Create a new traffic incident         |
| /api/trafficincident/{id}/| GET    | Get a specific traffic incident       |
| /api/trafficincident/{id}/| PUT    | Update a specific traffic incident    |
| /api/trafficincident/{id}/| DELETE | Delete a specific traffic incident    |
| /api/trafficsensor/   | GET    | Get all traffic sensors               |
| /api/trafficsensor/   | POST   | Create a new traffic sensor           |
| /api/trafficsensor/{id}/| GET    | Get a specific traffic sensor         |
| /api/trafficsensor/{id}/| PUT    | Update a specific traffic sensor      |
| /api/trafficsensor/{id}/| DELETE | Delete a specific traffic sensor      |

## Frontend

### Technologies Used

- React Native
- Expo
- React Navigation
- Axios
- React Native Chart Kit

### Installation

1. **Navigate to the mobile app directory:**

   ```bash
   cd ../mobile_app_new_version
   ```

2. **Install the dependencies:**

   ```bash
   npm install
   ```

### Running the Application

1. **Start the Expo development server:**

   ```bash
   npx expo start
   ```

2. **Open the app:**
   - For web: Press `w` to open in a web browser.
   - For Android: Press `a` to open in an Android emulator or scan the QR code with the Expo Go app.

## Data Visualization

### Power BI Dashboards

Power BI is used to create interactive and detailed dashboards for analyzing traffic data. Below are examples of visualizations created using Power BI:

- **Traffic Flow by Hour**: A line chart showing the number of vehicles detected per hour on different streets.
- **Traffic Incidents and Response Times**: A bar chart showing the number of incidents and average response times.
- **Traffic Sensor Status**: A column chart displaying the status of different traffic sensors.
- **Heat Map of Traffic Incidents**: A heat map showing the density of traffic incidents in various areas of the city.

### React Native Charts

The mobile app includes various charts to visualize traffic data in real-time. These charts are implemented using the `react-native-chart-kit` library.

- **Line Chart**: Displays traffic flow over time.
- **Bar Chart**: Shows the number of traffic incidents.
- **Pie Chart**: Visualizes the distribution of traffic sensor statuses.

## Screenshots

### Power BI Charts

![Gráfico de Power BI](./captures/Captura.PNG)

### React Native Charts

![Gráfico de React Native](./captures/Captura_frontend.PNG)

## Conclusion

The Urban Traffic Monitoring System provides a robust solution for urban authorities to monitor and manage traffic effectively. By combining a powerful backend, a user-friendly mobile app, and advanced data visualization techniques, this system aims to improve traffic flow and reduce incidents in urban areas.

## License

This project is licensed under the MIT License.
```
