from flask import Flask, jsonify
import os
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route("/")
def home():
    app_name = os.getenv("APP_NAME", "Default App Name")
    app.logger.info("Home endpoint called, APP_NAME=%s", app_name)
    return f"✅ Hello from {app_name}!"

@app.route("/health")
def health():
    return jsonify(status="OK")

if __name__ == "__main__":
    app.run()
