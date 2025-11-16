# Weather Dashboard

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0%2B-lightgrey.svg)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenWeatherMap](https://img.shields.io/badge/API-OpenWeatherMap-orange.svg)](https://openweathermap.org/)

A modern, responsive weather dashboard built with Flask and Jinja2 templates. This application delivers real-time weather information for any city worldwide, leveraging the OpenWeatherMap API to provide accurate and up-to-date meteorological data.

## 🌟 Features

- **Real-Time Weather Data**: Instant access to current weather conditions including temperature, humidity, wind speed, and more.
- **5-Day Forecast**: Comprehensive daily weather predictions with high/low temperatures and conditions.
- **Hourly Forecast**: Detailed hourly breakdown for the next 8 hours.
- **Unit Conversion**: Seamless toggle between Celsius and Fahrenheit.
- **Responsive Design**: Optimized for desktop, tablet, and mobile devices with a sleek glassmorphism UI.
- **City Search**: Intuitive search functionality with session-based persistence.
- **Modern UI**: Clean, professional interface inspired by contemporary weather applications.

## 📋 Prerequisites

- Python 3.8 or higher
- OpenWeatherMap API key (free tier available)

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/weather-dashboard-flask.git
cd weather-dashboard-flask
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory:
```env
OPENWEATHER_API_KEY=your_actual_api_key_here
SECRET_KEY=your_secret_key_here
```

### 5. Obtain OpenWeatherMap API Key
1. Visit [OpenWeatherMap API](https://openweathermap.org/api)
2. Create a free account
3. Navigate to your dashboard and generate an API key
4. Replace `your_actual_api_key_here` in `.env` with your key

## ▶️ Running the Application

```bash
python app.py
```

Access the dashboard at: `http://localhost:5000`

## 📁 Project Structure

```
weather-dashboard-flask/
├── app.py                    # Main Flask application with API endpoints
├── requirements.txt          # Python dependencies
├── .env                      # Environment configuration (not committed)
├── templates/
│   └── index.html           # Jinja2 template for the dashboard
├── static/
│   ├── css/
│   │   └── styles.css       # Custom CSS with glassmorphism effects
│   └── js/
│       └── app.js           # Client-side JavaScript for interactivity
└── README.md                # Project documentation
```

## 🔌 API Endpoints

| Method | Endpoint       | Description                  |
|--------|----------------|------------------------------|
| GET    | `/`           | Main dashboard page         |
| POST   | `/`           | Search for weather data     |
| POST   | `/toggle_unit`| Toggle temperature units    |
| POST   | `/search`     | AJAX search endpoint        |

## 🛠️ Technologies & Dependencies

- **Backend**: Flask, Python Requests
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Styling**: Tailwind CSS, Custom CSS
- **API Integration**: OpenWeatherMap API
- **Environment Management**: python-dotenv

## 📱 Screenshots

*Add screenshots here to showcase the application's interface and features.*

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guidelines
- Write clear, concise commit messages
- Test thoroughly before submitting PRs
- Update documentation as needed

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Weather data courtesy of [OpenWeatherMap](https://openweathermap.org/)
- UI design inspired by modern weather applications
- Icons provided via Unicode emojis

## 📞 Support

If you encounter any issues or have questions, please open an issue on GitHub.

---

*Built with ❤️ using Flask, HTML , CSS  and a passion for Technology*
