import psutil
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    cpu_percent = psutil.cpu_percent()
    mem_percent = psutil.virtual_memory().percent
    message = None

    if cpu_percent > 80:
        message = "CPU usage is high"
    elif mem_percent > 80:
        message = "Memory usage is high"
    else:
        message = "Everything is fine"

    return render_template("index.html", cpu_metric=cpu_percent, mem_metric=mem_percent, message=message)


# if __name__ == "__main__":
#     app.run(debug=True, host="0.0.0.0", port=8000)
