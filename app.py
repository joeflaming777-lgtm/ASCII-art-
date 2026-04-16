from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    # We serve the ascii_camera_1.html directly from the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return send_from_directory(current_dir, 'ascii_camera_1.html')

if __name__ == '__main__':
    print("=" * 50)
    print(" Server started!")
    print(" Open your browser and go to: http://127.0.0.1:5000")
    print("=" * 50)
    # Accessible on the local network if needed
    app.run(host='0.0.0.0', port=5000, debug=True)
