from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
        return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():

    machine_id = request.form["machine_id"]
    machine_type = request.form["machine_type"]

    temp = int(request.form["temp"])
    vib = int(request.form["vib"])
    pressure = int(request.form["pressure"])
    speed = int(request.form["speed"])
    usage = int(request.form["usage"])

    health_score = 100

    if temp > 80:
        health_score -= 20

    if vib > 7:
        health_score -= 20

    if pressure > 80:
        health_score -= 20

    if speed > 1500:
        health_score -= 20

    if usage > 12:
        health_score -= 20
    
    
    issues = []
    solutions = []

    if temp > 80:
        issues.append("🔥 High Temperature")
        solutions.append("❄ Check cooling system")

    if vib > 7:
        issues.append("📳 High Vibration")
        solutions.append("🔩 Tighten loose parts")

    if pressure > 80:
        issues.append("⚙ High Pressure")
        solutions.append("🛠 Release pressure safely")

    if speed > 1500:
        issues.append("🏎 High Speed")
        solutions.append("⬇ Reduce machine speed")

    if usage > 12:
        issues.append("⏳ Over Usage")
        solutions.append("☕ Give machine rest time")

    if issues:
        result = "🚨 Machine in Danger!"
    else:
        result = "✅ Machine is Healthy"

    if health_score >= 80:
        status = "🟢 Healthy"
        color = "green"
        message = "Machine operating normally."

    elif health_score >= 50:
        status = "🟡 Warning"
        color = "orange"
        message = "Maintenance recommended soon."

    else:
        status = "🔴 Critical"
        color = "red"
        message = "Immediate maintenance required!"

    
    failure_risk = 100 - health_score

    if failure_risk <= 20:
        risk_color = "green"
    elif failure_risk <= 50:
        risk_color = "orange"
    else:
        risk_color = "red"

    
    
    current_time = datetime.now().strftime("%d-%m-%Y %H:%M")
    

    return render_template(
    "index.html",
    result=result,
    health_score=health_score,
    status=status,
    color=color,
    issues=issues,
    solutions=solutions,
    failure_risk=failure_risk,
    risk_color=risk_color,
    message=message,
    machine_id=machine_id,
    machine_type=machine_type,
    temp=temp,
    vib=vib,
    pressure=pressure,
    speed=speed,
    usage=usage,
    current_time=current_time
)

if __name__ == "__main__":
    app.run(debug=True)