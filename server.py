from flask import Flask, request

app = Flask(__name__)

@app.route('/api/device-info', methods=['POST'])
def device_info():
    device_info = request.json
    print(device_info)  # Logs device info to Render logs
    
    # Save received data to file
    with open("received_devices.txt", "a") as f:
        f.write(str(device_info) + "\n")
    
    return "Data received", 200

@app.route('/api/view-data', methods=['GET'])
def view_data():
    try:
        with open("received_devices.txt", "r") as f:
            content = f.read()
        return "<pre>" + content + "</pre>"
    except FileNotFoundError:
        return "No data received yet.", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
