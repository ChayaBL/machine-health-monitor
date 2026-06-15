from flask import send_file
from reportlab.pdfgen import canvas
import csv
from flask import make_response
import sqlite3
from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

history = []


@app.route("/")
def home():

    conn = sqlite3.connect("machines.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT time, machine_id, machine_type,
           health_score, status, grade
    FROM history
    ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    history_data = []

    for row in rows:
        history_data.append({
            "time": row[0],
            "machine_id": row[1],
            "machine_type": row[2],
            "health_score": row[3],
            "status": row[4],
            "grade": row[5]
        })

    return render_template(
        "index.html",
        history=history_data
    )

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

    issue_count = len(issues)

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

    if health_score >= 80:
        grade = "A"
    elif health_score >= 60:
        grade = "B"
    elif health_score >= 40:
        grade = "C"
    else:
        grade = "D"

    if health_score >= 80:
        score_color = "green"
    elif health_score >= 50:
        score_color = "orange"
    else:
        score_color = "red"

    if health_score >= 80:
        badge = "Excellent 🏆"
    elif health_score >= 60:
        badge = "Good 👍"
    elif health_score >= 40:
        badge = "Average ⚠️"
    else:
        badge = "Poor 🚨"

    if health_score >= 80:
        summary = "Machine is performing excellently."
    elif health_score >= 50:
        summary = "Machine needs attention soon."
    else:
        summary = "Machine requires immediate maintenance."

    if health_score >= 80:
        maintenance = "Next maintenance after 30 days"
    elif health_score >= 50:
        maintenance = "Schedule maintenance within 7 days"
    else:
        maintenance = "Immediate maintenance required"
    
    efficiency = 100

    if temp > 80:
        efficiency -= 10

    if vib > 7:
        efficiency -= 10

    if pressure > 80:
        efficiency -= 10

    if speed > 1500:
        efficiency -= 10

    if usage > 12:
        efficiency -= 10

    
    failure_risk = 100 - health_score

    if failure_risk <= 20:
        risk_color = "green"
    elif failure_risk <= 50:
        risk_color = "orange"
    else:
        risk_color = "red"

    
    
    current_time = datetime.now().strftime("%d-%m-%Y %H:%M")

    history.append({
    "time": current_time,
    "machine_id": machine_id,
    "machine_type": machine_type,
    "health_score": health_score,
    "status": status,
    "grade": grade
})
    conn = sqlite3.connect("machines.db")

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO history (
        time,
        machine_id,
        machine_type,
        health_score,
        status,
        grade
    )
    VALUES (?, ?, ?, ?, ?, ?)
    """, (
        current_time,
        machine_id,
        machine_type,
        health_score,
        status,
        grade
    ))

    conn.commit()
    conn.close()
    total_machines = len(history)

    scores = [item["health_score"] for item in history]

    best_score = max(scores)
    lowest_score = min(scores)
    average_score = round(sum(scores) / len(scores), 1)
    

    return render_template(
    "index.html",
    result=result,
    health_score=health_score,
    status=status,
    color=color,
    issues=issues,
    grade=grade,
    solutions=solutions,
    issue_count=issue_count,
    failure_risk=failure_risk,
    best_score=best_score,
    lowest_score=lowest_score,
    average_score=average_score,
    summary=summary,
    efficiency=efficiency,
    maintenance=maintenance,
    risk_color=risk_color,
    score_color=score_color,
    badge=badge,
    message=message,
    total_machines=total_machines,
    machine_id=machine_id,
    machine_type=machine_type,
    temp=temp,
    vib=vib,
    pressure=pressure,
    speed=speed,
    usage=usage,
    current_time=current_time,
    history=history
)
@app.route("/search", methods=["POST"])
def search():

    search_date = request.form["search_date"]

    date_obj = datetime.strptime(
        search_date,
        "%Y-%m-%d"
    )

    formatted_date = date_obj.strftime(
        "%d-%m-%Y"
    )

    conn = sqlite3.connect("machines.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT time, machine_id, machine_type,
        health_score, status, grade
    FROM history
    WHERE time LIKE ?
    """, (f"%{formatted_date}%",))

    rows = cursor.fetchall()

    conn.close()

    filtered_history = []

    for row in rows:
        filtered_history.append({
            "time": row[0],
            "machine_id": row[1],
            "machine_type": row[2],
            "health_score": row[3],
            "status": row[4],
            "grade": row[5]
        })

    return render_template(
    "index.html",
    history=filtered_history,
    message=f"Found {len(filtered_history)} record(s)"
)
@app.route("/search_machine", methods=["POST"])
def search_machine():

    machine_id = request.form["machine_id"]

    conn = sqlite3.connect("machines.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT time, machine_id, machine_type,
        health_score, status, grade
    FROM history
    WHERE machine_id = ?
    ORDER BY id DESC
    """, (machine_id,))

    rows = cursor.fetchall()

    conn.close()

    filtered_history = []

    for row in rows:
        filtered_history.append({
            "time": row[0],
            "machine_id": row[1],
            "machine_type": row[2],
            "health_score": row[3],
            "status": row[4],
            "grade": row[5]
        })

    return render_template(
        "index.html",
        history=filtered_history,
        message=f"Found {len(filtered_history)} record(s)"
    )
@app.route("/export")
def export():

    conn = sqlite3.connect("machines.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT time, machine_id, machine_type,
           health_score, status, grade
    FROM history
    ORDER BY id DESC
    """)

    rows = cursor.fetchall()
    conn.close()

    csv_data = "Time,Machine ID,Machine Type,Health Score,Status,Grade\n"

    for row in rows:
        csv_data += f"{row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]}\n"

    response = make_response(csv_data)

    response.headers["Content-Disposition"] = \
        "attachment; filename=machine_history.csv"

    response.headers["Content-Type"] = "text/csv"

    return response
@app.route("/export_pdf")
def export_pdf():

    conn = sqlite3.connect("machines.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT time, machine_id, machine_type,
           health_score, status, grade
    FROM history
    ORDER BY id DESC
    """)

    rows = cursor.fetchall()
    conn.close()

    pdf = canvas.Canvas("machine_report.pdf")

    pdf.setTitle("Machine Report")

    pdf.drawString(
        100,
        800,
        "Smart Predictive Maintenance Report"
    )

    y = 760

    for row in rows:
        pdf.drawString(
            50,
            y,
            f"{row[0]} | {row[1]} | {row[2]} | {row[3]}%"
        )
        y -= 20
        if y < 50:
            pdf.showPage()
            y = 800

    pdf.save()

    return send_file(
    "machine_report.pdf",
    as_attachment=True,
    download_name="machine_report.pdf"
)
if __name__ == "__main__":
    app.run(debug=True)