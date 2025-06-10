from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/api/device-info', methods=['POST'])
def receive_device_info():
    data = request.json
    print("Received Device Info:", data)

    # Save to file (optional)
    with open("received_devices.txt", "a") as f:
        f.write(str(data) + "\n")

    return jsonify({"status": "success"})

# Use port assigned by Render, fallback to 5000
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
