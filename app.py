from flask import Flask, jsonify
import os
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route("/")
def home():
    app_name = os.getenv("APP_NAME", "Default App Name")
    environment = os.getenv("ENVIRONMENT", "dev")

    app.logger.info(
        "Home endpoint called | APP_NAME=%s | ENVIRONMENT=%s",
        app_name,
        environment
    )

    if environment == "prod":
        return f"✅ Welcome to {app_name}"
    else:
        return f"🧪 [{environment.upper()}] {app_name}"

@app.route("/health")
def health():
    return jsonify(status="OK")

if __name__ == "__main__":
    app.run()

