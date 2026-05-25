from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route("/")
def home():
    app.logger.info("Home endpoint was called")
    1 / 0   # intentional error
    return "This will never run"

@app.route("/health")
def health():
    app.logger.info("Health check called from %s", request.remote_addr)
    return jsonify(status="OK", service="flask-app")

if __name__ == "__main__":
    app.run()
