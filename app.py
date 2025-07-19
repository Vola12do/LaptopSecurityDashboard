# backend/app.py
from flask import Flask, jsonify, request
from flask_cors import CORS
import datetime

app = Flask(__name__)
CORS(app)

# In-memory storage for the latest data received from a collector
latest_health_data = {
    "status": "No data received yet. Run the collector.py script on your machine."
}

@app.route('/')
def index():
    return "<h1>Live Security Dashboard Backend</h1><p>This server is waiting for data to be submitted to /api/submit.</p>"

@app.route('/api/health', methods=['GET'])
def get_health_data():
    """Returns the last data that was submitted by a collector."""
    print("Request for health data received. Serving latest data.")
    return jsonify(latest_health_data)

@app.route('/api/submit', methods=['POST'])
def submit_health_data():
    """Receives and stores health data from a collector script."""
    global latest_health_data
    new_data = request.get_json()
    if not new_data:
        return jsonify({"error": "No JSON data received"}), 400
    print(f"New data received at {datetime.datetime.now().isoformat()}")
    latest_health_data = new_data
    return jsonify({"message": "Data received successfully"}), 200

if __name__ == '__main__':
    # Runs the server. For local testing, it's fine.
    # Replit will manage the host/port automatically when deployed.
    app.run(host='0.0.0.0', port=5000, debug=True)
