# WSGI configuration for PythonAnywhere
import sys
import os

# Add your project directory to the sys.path
project_home = '/home/YOUR_USERNAME/micah_highsprings_mobil'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Set environment variables
os.environ['ENVIRONMENT'] = 'production'

# Import the Flask app
from app import app as application
