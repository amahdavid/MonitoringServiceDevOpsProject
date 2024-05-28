import psutil
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    cpu_percent = psutil.cpu_percent()
    mem_percent = psutil.virtual_memory().percent
    Message = None

    if cpu_percent > 80:
        Message = "CPU usage is high"
    elif mem_percent > 80:
        Message = "Memory usage is high"
    else:
        Message = "Everything is fine"

    return f"CPU: {cpu_percent}%\nMemory: {mem_percent}%\n{Message}"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
