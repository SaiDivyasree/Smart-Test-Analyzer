from flask import Flask, render_template
import pandas as pd
import os

def get_severity_color(suggestion):
    suggestion = suggestion.lower()
    if any(word in suggestion for word in ["timeout", "wait", "delay"]):
        return "text-warning"  # yellow
    elif any(word in suggestion for word in ["popup", "intercepted", "flaky"]):
        return "text-primary"  # blue
    elif any(word in suggestion for word in ["not found", "locator", "missing"]):
        return "text-danger"  # red
    elif any(word in suggestion for word in ["environment", "webdriver", "session"]):
        return "text-muted"  # gray
    else:
        return "text-success"  # green or low severity

app = Flask(__name__)

@app.route("/")
def dashboard():
    file_path = "../output/classified_results.csv"
    if not os.path.exists(file_path):
        return "<h2>No classified results found. Run the test and ML pipeline first.</h2>"

    df = pd.read_csv(file_path)
    df["severity_class"] = df["suggestion"].apply(get_severity_color)
    table_html = df.to_dict(orient="records")
    return render_template("dashboard.html", table=table_html)


if __name__ == "__main__":
    app.run(debug=True)
