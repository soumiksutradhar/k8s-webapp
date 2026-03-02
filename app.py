from flask import Flask
import socket
import os

app = Flask(__name__)

APP_VERSION = os.getenv("VERSION", "v1")
IN_K8S = os.getenv("KUBERNETES_SERVICE_HOST") is not None

@app.route("/")
def home():
    return f"""
    <h2>ClusterVitals - Kubernetes Deployment Monitor</h2>
    <p><b>Hostname:</b> {socket.gethostname()}</p>
    <p><b>Environment:</b> {os.getenv('ENV','dev')}</p>
    <p><b>Version:</b> {APP_VERSION}</p>
    <p><b>Running Inside Kubernetes:</b> {"Yes" if IN_K8S else "No"}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
