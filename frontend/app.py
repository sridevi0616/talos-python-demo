from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def home():

    response = requests.get("http://backend/api/data")

    return {
        "frontend": "running",
        "backend_response": response.json()
    }

@app.route("/health")
def health():
    return {"status":"healthy"}

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)
