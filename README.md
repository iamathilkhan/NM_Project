# Weather Dashboard - Flask Version

A beautiful, responsive weather dashboard built with Flask and Jinja2 templates. This application provides real-time weather information for any city using the OpenWeatherMap API.

## Features

- 🌤️ Real-time current weather data
- 📅 5-day weather forecast
- 🕐 Hourly forecast for today
- 🌡️ Temperature unit toggle (Celsius/Fahrenheit)
- 📱 Fully responsive design
- 🎨 Modern UI with glassmorphism effects
- 🔍 City search functionality
- 💾 Session-based data persistence

## Prerequisites

- Python 3.8 or higher
- OpenWeatherMap API key (free)

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd weather-dashboard-flask
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   - Create a `.env` file in the root directory and add your OpenWeatherMap API key:
   ```bash
   OPENWEATHER_API_KEY=your_actual_api_key_here
   SECRET_KEY=your_secret_key_here
   ```

5. **Get your OpenWeatherMap API key:**
   - Visit [OpenWeatherMap](https://openweathermap.org/api)
   - Sign up for a free account
   - Go to your account dashboard and generate an API key
   - Copy the API key and paste it as the value for `OPENWEATHER_API_KEY` in your `.env` file

## Running the Application

```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Project Structure

```
weather-dashboard-flask/
├── app.py                    # Main Flask application
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables
├── templates/
│   └── index.html           # Main template
├── static/
│   ├── css/
│   │   └── styles.css       # Custom styles
│   └── js/
│       └── app.js           # Client-side JavaScript
└── README.md
```

## API Endpoints

- `GET /` - Main dashboard page
- `POST /` - Search for weather data
- `POST /toggle_unit` - Toggle temperature units

## Technologies Used

- **Backend:** Flask, Python
- **Frontend:** HTML5, CSS3, JavaScript
- **Styling:** Tailwind CSS, Custom CSS
- **API:** OpenWeatherMap API
- **Icons:** Emoji (could be replaced with Heroicons)

## Features in Detail

### Current Weather
- Temperature (with feels-like)
- Weather condition and description
- Humidity, wind speed, visibility, pressure
- Sunrise and sunset times

### 5-Day Forecast
- Daily high temperatures
- Weather conditions
- Humidity and wind speed

### Hourly Forecast
- Next 8 hours of weather
- Temperature and conditions

### Responsive Design
- Mobile-first approach
- Optimized for all screen sizes
- Touch-friendly interface

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- Weather data provided by [OpenWeatherMap](https://openweathermap.org/)
- UI inspiration from modern weather apps
