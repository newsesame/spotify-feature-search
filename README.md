# Spotify Feature Search API

A backend service built with FastAPI and Spotify API that provides playlist and track search functionality.

## 🚀 Features

- **Playlist Query**: Retrieve track information from Spotify playlists
- **Track Search**: Search for tracks on Spotify by keywords
- **Data Models**: Type-safe data validation using Pydantic
- **Async Support**: Full async/await support for non-blocking operations
- **Auto API Documentation**: Built-in Swagger UI and ReDoc

## 📁 Project Structure

```
spotify-feature-search/
├── app/                          # Main application code
│   ├── main.py                   # FastAPI application entry point
│   ├── models.py                 # Pydantic data models
│   ├── routes.py                 # API rgit qweoute definitions
│   ├── services.py               # Business logic services
│   └── spotify_service.py        # Spotify API service
├── scripts/                      # Script files
│   └── start.py                  # Startup script
├── main.py                       # Application main entry
├── pyproject.toml               # Project configuration and dependencies
└── README.md
```

## 🛠️ Installation and Setup

### 1. Clone the Project

```bash
git clone https://github.com/yourusername/spotify-feature-search.git
cd spotify-feature-search
```

### 2. Install Dependencies

```bash
# Using uv (recommended)
uv sync

# Or using pip
pip install -e .
```

### 3. Environment Configuration

Create a `.env` file:

```env
# Spotify API Configuration
SPOTIFY_CLIENT_ID=your_spotify_client_id
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
```

### 4. Start the Application

```bash
# Using startup script
python scripts/start.py

# Or directly using uvicorn
uvicorn main:app --reload

# Or using uv
uv run uvicorn main:app --reload
```

## 📚 API Documentation

After starting the application, you can access:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health

## 🔧 Main API Endpoints

### Playlist Related

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/v1/spotify/playlists/{playlist_id}/separated` | GET | Get playlist tracks (separated format) |

### Other Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Root path welcome message |
| `/health` | GET | Health check |
| `/items/{item_id}` | GET | Example endpoint |

## 🧪 Testing

```bash
# Run tests
uv run pytest

# Run tests with coverage report
uv run pytest --cov=app
```

## 🚀 Deployment

### Local Development

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Production

```bash
# Deploy using gunicorn
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker
```

## 📋 Tech Stack

- **FastAPI**: Modern, fast web framework
- **Pydantic**: Data validation and serialization
- **aiohttp**: Async HTTP client
- **uv**: Fast Python package manager
- **Spotify Web API**: Music data source

## 🤝 Contributing

1. Fork the project
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License.

## 📞 Contact

- Project Link: [https://github.com/yourusername/spotify-feature-search](https://github.com/yourusername/spotify-feature-search)
- Issue Tracker: [https://github.com/yourusername/spotify-feature-search/issues](https://github.com/yourusername/spotify-feature-search/issues)
