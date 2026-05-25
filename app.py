from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Hello from my first Flask app running on Azure!"

@app.route("/health")
def health():
    return "OK"

if __name__ == "__main__":
    app.run()
