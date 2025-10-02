# AI Calculator Backend 🧠

A powerful FastAPI-based backend that processes hand-drawn mathematical expressions using Google's Gemini AI for recognition and calculation.

## 🌟 Overview

This backend service receives base64-encoded images of hand-drawn mathematical expressions, processes them using Google's Gemini AI model for recognition, evaluates the expressions, and returns calculated results. Built with FastAPI for high performance and easy API development.

## ✨ Key Features

- **AI-Powered Recognition**: Leverages Google Gemini API for accurate handwriting recognition
- **Mathematical Expression Evaluation**: Safely evaluates recognized mathematical expressions
- **Variable Assignment Support**: Handles variable assignments and maintains state
- **Image Processing**: Efficient handling of base64-encoded images using Pillow
- **CORS Enabled**: Configured for seamless frontend integration
- **Fast & Async**: Built on FastAPI for high-performance asynchronous operations
- **Type Safety**: Uses Pydantic for request/response validation
- **Error Handling**: Comprehensive error handling and validation

## 🛠️ Tech Stack

- **FastAPI** - Modern, fast web framework for building APIs
- **Uvicorn** - Lightning-fast ASGI server
- **Python 3.8+** - Core programming language
- **Google Generative AI** - Gemini API for AI-powered recognition
- **Pillow (PIL)** - Image processing library
- **Pydantic** - Data validation and settings management
- **python-dotenv** - Environment variable management

## 📋 Prerequisites

- **Python** 3.8 or higher
- **pip** (Python package manager)
- **Google Gemini API Key** - Get yours at [Google AI Studio](https://makersuite.google.com/app/apikey)

## 🚀 Getting Started

### Installation

1. **Navigate to the backend directory**:
```bash
cd ai-powered-calculator/backend
```

2. **Create a virtual environment**:
```bash
# Windows
python -m venv venv

# macOS/Linux
python3 -m venv venv
```

3. **Activate the virtual environment**:
```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

4. **Install dependencies**:
```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install fastapi uvicorn pydantic pillow google-generativeai python-dotenv
```

### Configuration

Create a `.env` file in the backend directory:
```env
GEMINI_API_KEY=your_gemini_api_key_here
PORT=8000
```

### Running the Server

**Development mode** (with auto-reload):
```bash
uvicorn main:app --reload
```

**Production mode**:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

**With custom port**:
```bash
uvicorn main:app --reload --port 8080
```

The API will be available at `http://localhost:8000`

## 📁 Project Structure

```
backend/
├── main.py              # Main application file
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (create this)
├── .gitignore          # Git ignore file
├── constants.py        # Application constants (if any)
└── utils/              # Utility functions (optional)
```

## 🔌 API Endpoints

### Health Check
```http
GET /
```

Response:
```json
{
  "message": "AI Calculator API is running",
  "status": "healthy"
}
```

### Calculate Expression
```http
POST /calculate
Content-Type: application/json
```

Request Body:
```json
{
  "image": "data:image/png;base64,iVBORw0KGgoAAAANS...",
  "dict_of_vars": {
    "x": 5,
    "y": 10
  }
}
```

Response (Success):
```json
{
  "expr": "2 + 2",
  "result": "4",
  "assign": false
}
```

Response (Variable Assignment):
```json
{
  "expr": "x = 5",
  "result": "5",
  "assign": true
}
```

Response (Error):
```json
{
  "error": "Error message here"
}
```

## 🧮 Supported Mathematical Operations

- **Basic Arithmetic**: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- **Algebraic Functions**: Variables, equations
- **Mathematical Functions**: `sqrt()`, `sin()`, `cos()`, `tan()`, `log()`, `exp()`
- **Constants**: `pi`, `e`
- **Parentheses**: For grouping expressions
- **Variable Assignment**: `x = 5`, `result = a + b`

## 🔒 Security Features

- **Input Validation**: Pydantic models validate all inputs
- **Safe Evaluation**: Expressions are evaluated in a controlled environment
- **CORS Configuration**: Configured to accept requests only from trusted origins
- **Environment Variables**: Sensitive data stored securely in `.env`
- **Error Sanitization**: Detailed errors not exposed to clients

## ⚙️ Configuration Options

### CORS Settings

Modify CORS settings in `main.py`:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Add your frontend URLs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Gemini AI Configuration

Adjust AI model settings:
```python
generation_config = {
    "temperature": 0.7,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}
```

### Image Processing

Configure image processing parameters in the image handling function:
```python
# Adjust image size, format, quality
image = Image.open(BytesIO(image_data))
image = image.resize((800, 600))
```

## 🔧 Troubleshooting

### API Key Issues
- Verify your Gemini API key is correct in `.env`
- Check if the API key has proper permissions
- Ensure you haven't exceeded API quota limits

### CORS Errors
- Add your frontend URL to `allow_origins` in CORS middleware
- Ensure the backend is running before starting frontend
- Check if the frontend is using the correct API URL

### Import Errors
- Verify all dependencies are installed: `pip list`
- Reinstall requirements: `pip install -r requirements.txt --upgrade`
- Check Python version compatibility

### Image Processing Errors
- Verify the image data is properly base64 encoded
- Check image format is supported (PNG, JPEG)
- Ensure image size is reasonable (not too large)

### Expression Evaluation Errors
- Check if the expression syntax is valid
- Verify all variables are defined in `dict_of_vars`
- Look for unsupported mathematical operations

## 📦 Dependencies

```txt
fastapi>=0.104.0
uvicorn[standard]>=0.24.0
pydantic>=2.4.0
pillow>=10.0.0
google-generativeai>=0.3.0
python-dotenv>=1.0.0
```

## 🧪 Testing

### Manual Testing with cURL

Test the health endpoint:
```bash
curl http://localhost:8000/
```

Test the calculate endpoint:
```bash
curl -X POST http://localhost:8000/calculate \
  -H "Content-Type: application/json" \
  -d '{
    "image": "data:image/png;base64,iVBORw0KGg...",
    "dict_of_vars": {}
  }'
```

### Using Python Requests

```python
import requests
import base64

# Read and encode image
with open("math_expression.png", "rb") as f:
    image_data = base64.b64encode(f.read()).decode()

# Make request
response = requests.post(
    "http://localhost:8000/calculate",
    json={
        "image": f"data:image/png;base64,{image_data}",
        "dict_of_vars": {}
    }
)

print(response.json())
```

## 🚀 Deployment

### Deploy to Heroku

1. Create `Procfile`:
```
web: uvicorn main:app --host 0.0.0.0 --port $PORT
```

2. Deploy:
```bash
heroku create your-app-name
git push heroku main
heroku config:set GEMINI_API_KEY=your_key_here
```

### Deploy to Railway

1. Connect your GitHub repository
2. Add environment variables in Railway dashboard
3. Railway will auto-detect and deploy FastAPI app

### Deploy to Google Cloud Run

```bash
gcloud run deploy ai-calculator-backend \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

## 📊 Performance Optimization

- **Async Operations**: FastAPI handles requests asynchronously
- **Image Optimization**: Process images efficiently before sending to AI
- **Caching**: Consider implementing response caching for repeated expressions
- **Rate Limiting**: Add rate limiting to prevent API abuse
- **Connection Pooling**: Optimize database/API connections

## 🔐 Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GEMINI_API_KEY` | Google Gemini API key | Yes |
| `PORT` | Server port (default: 8000) | No |
| `ALLOWED_ORIGINS` | CORS allowed origins | No |
| `LOG_LEVEL` | Logging level (INFO, DEBUG, etc.) | No |

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-feature`
3. Make your changes
4. Write tests for new functionality
5. Commit: `git commit -m 'Add new feature'`
6. Push: `git push origin feature/new-feature`
7. Open a Pull Request

## 📄 License

This project is for educational purposes only.

## 💡 Best Practices

- Always use virtual environments
- Keep your API key secure and never commit it
- Handle errors gracefully
- Log important events for debugging
- Validate all inputs
- Use type hints for better code quality
- Write docstrings for functions
- Keep dependencies updated

## 📚 API Documentation

FastAPI provides automatic interactive API documentation:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`
- **OpenAPI Schema**: `http://localhost:8000/openapi.json`

## 📞 Support

For issues or questions:
- Check existing GitHub issues
- Open a new issue with:
  - Python version
  - Error messages
  - Steps to reproduce
  - Environment details

---

**Built with ⚡ FastAPI and 🤖 Google Gemini AI**

*Part of the AI-Powered Calculator project by Shuvom Dhar*