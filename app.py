from flask import Flask, jsonify, render_template_string
import os

app = Flask(__name__)

# HTML template for the home page
HOME_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>High Springs Mobil - Business Analysis</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .container {
            background-color: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        h1 {
            color: #333;
            border-bottom: 3px solid #007bff;
            padding-bottom: 10px;
        }
        .status {
            background-color: #28a745;
            color: white;
            padding: 10px 20px;
            border-radius: 5px;
            display: inline-block;
            margin: 20px 0;
        }
        .info {
            background-color: #f8f9fa;
            padding: 15px;
            border-left: 4px solid #007bff;
            margin: 20px 0;
        }
        .endpoint {
            background-color: #e9ecef;
            padding: 10px;
            margin: 10px 0;
            border-radius: 4px;
            font-family: monospace;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>High Springs Mobil - Business Analysis App</h1>
        <div class="status">✓ Application Running Successfully</div>

        <div class="info">
            <h2>About This Project</h2>
            <p>This Flask application is designed to support the analysis of the High Springs Mobil gas station investment opportunity.</p>
            <p><strong>Location:</strong> 19531 US HWY 441, High Springs, FL 32643</p>
        </div>

        <h2>Available Endpoints</h2>
        <div class="endpoint">GET / - This home page</div>
        <div class="endpoint">GET /api/health - Health check endpoint</div>
        <div class="endpoint">GET /api/status - Application status</div>

        <div class="info">
            <p><strong>Environment:</strong> {{ env }}</p>
            <p><strong>Port:</strong> {{ port }}</p>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    """Home page with project information"""
    return render_template_string(
        HOME_PAGE,
        env=os.getenv('ENVIRONMENT', 'development'),
        port=os.getenv('PORT', '5000')
    )

@app.route('/api/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'message': 'Application is running'
    }), 200

@app.route('/api/status')
def status():
    """Application status endpoint"""
    return jsonify({
        'application': 'micah_highsprings_mobil',
        'version': '1.0.0',
        'environment': os.getenv('ENVIRONMENT', 'development'),
        'status': 'running'
    }), 200

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
