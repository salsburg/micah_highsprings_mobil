# High Springs Mobil - Business Analysis App

Flask application for analyzing the High Springs Mobil gas station investment opportunity.

## Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Access the app at: `http://localhost:5000`

## API Endpoints

- `GET /` - Home page with project information
- `GET /api/health` - Health check endpoint
- `GET /api/status` - Application status

## Deployment

**Deployed on PythonAnywhere**

See [PYTHONANYWHERE_DEPLOY.md](PYTHONANYWHERE_DEPLOY.md) for detailed deployment instructions.

**Live URL**: `https://salsburg.pythonanywhere.com` (after deployment)

## Project Files

- `app.py` - Main Flask application
- `requirements.txt` - Python dependencies
- `wsgi.py` - PythonAnywhere WSGI configuration
- `PYTHONANYWHERE_DEPLOY.md` - Deployment guide
- `context.md` - Business analysis context
- Cash flow and financial documents
