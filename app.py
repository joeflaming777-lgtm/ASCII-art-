from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return send_from_directory(current_dir, 'index.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", "5000"))
    url = f"http://127.0.0.1:{port}"
    print("=" * 50)
    print(" Server started!")
    print(f" Open your browser and go to: {url}")
    print("=" * 50)
    # Accessible on the local network if needed
    app.run(host='0.0.0.0', port=port, debug=True)
