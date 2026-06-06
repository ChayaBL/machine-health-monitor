from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello Chaya! 🚀</h1>"

@app.route("/analyze", methods=["POST"])
def analyze():

    temp = int(request.form["temp"])
    vib = int(request.form["vib"])
    pressure = int(request.form["pressure"])

    issues = []

    if temp > 80:
        issues.append("High Temperature")

    if vib > 7:
        issues.append("High Vibration")

    if pressure > 80:
        issues.append("High Pressure")

    if issues:
        result = "🚨 Machine in Danger! " + ", ".join(issues)
    else:
        result = "✅ Machine is Healthy"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)