from flask import Flask
import socket
import redis

app = Flask(__name__)

r = redis.Redis(host='redis', port=6379)

@app.route("/api/data")
def data():

    count = r.incr("hits")

    return {
        "service": "backend",
        "hostname": socket.gethostname(),
        "redis_hits": count,
        "text": "HIIII"
    }

@app.route("/health")
def health():
    return {"status":"healthy"}

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)
