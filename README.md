# thinkhub-flask
from flask import Flask, render_template, request
from algorithm import get_optimal_slot
from dashboard import get_dashboard_data

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    optimal_slot = None

    if request.method == "POST":
        ev_x = float(request.form["x"])
        ev_y = float(request.form["y"])
        optimal_slot = get_optimal_slot(ev_x, ev_y)

    dashboard = get_dashboard_data()
    return render_template("index.html", optimal_slot=optimal_slot, dashboard=dashboard)

if __name__ == "__main__":
    app.run(debug=True)
