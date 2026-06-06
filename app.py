<<<<<<< HEAD
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():

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

    elif health_score >= 50:
        status = "🟡 Warning"
        color = "orange"

    else:
        status = "🔴 Critical"
        color = "red"

    if health_score >= 80:
        message = "Machine operating normally."

    elif health_score >= 50:
        message = "Maintenance recommended soon."

    else:
        message = "Immediate maintenance required!"

    failure_risk = 100 - health_score
    

    return render_template(
    "index.html",
    result=result,
    health_score=health_score,
    status=status,
    color=color,
    issues=issues,
    solutions=solutions,
    failure_risk=failure_risk,
    message=message,

    temp=temp,
    vib=vib,
    pressure=pressure,
    speed=speed,
    usage=usage
)

if __name__ == "__main__":
    app.run(debug=True)
=======
import streamlit as st

st.set_page_config(page_title="Smart Maintenance", page_icon="🔧", layout="centered")

# 🎨 Title
st.title("🔧 Smart Predictive Maintenance System")
st.markdown("### 🚀 Real-Time Machine Health Monitoring")

# 📊 Inputs
st.subheader("📥 Enter Machine Parameters")

temp = st.slider("🌡 Temperature (°C)", 30, 120, 50)
vib = st.slider("📳 Vibration Level", 1, 10, 5)
pres = st.slider("⚙ Pressure", 20, 100, 40)
speed = st.slider("🏎 Working Speed", 0, 2000, 800)
usage = st.slider("⏳ Usage Time (hours)", 0, 24, 5)

# 🔊 Auto Sound Function (FIXED)
def play_alert():
    st.markdown("""
    <audio autoplay>
        <source src="https://www.soundjay.com/buttons/beep-01a.mp3" type="audio/mp3">
    </audio>
    """, unsafe_allow_html=True)

# 🔍 Button
if st.button("🔍 Analyze Machine"):

    issues = []

    # 🚨 Detect Problems
    if temp > 80:
        issues.append("🔥 High Temperature")
    if vib > 7:
        issues.append("📳 High Vibration")
    if pres > 80:
        issues.append("⚙ High Pressure")
    if speed > 1500:
        issues.append("🏎 Excessive Speed")
    if usage > 12:
        issues.append("⏳ Over Usage")

    # 🚨 DANGER CASE
    if issues:
        st.error("🚨 MACHINE IN DANGER!")

        # 🔊 Play Sound
        play_alert()

        st.markdown("### 🚨 Problems Detected:")
        for issue in issues:
            st.write(f"👉 {issue}")

        # 💡 Suggestions
        st.markdown("### 💡 Suggestions:")
        if "🔥 High Temperature" in issues:
            st.write("👉 Check cooling system ❄")
        if "📳 High Vibration" in issues:
            st.write("👉 Tighten loose parts 🔩")
        if "⚙ High Pressure" in issues:
            st.write("👉 Release pressure safely")
        if "🏎 Excessive Speed" in issues:
            st.write("👉 Reduce machine speed")
        if "⏳ Over Usage" in issues:
            st.write("👉 Allow machine to rest")

    # ⚠ WARNING CASE
    elif temp > 50 or vib > 5:
        st.warning("⚠ Machine needs attention")
        st.write("👉 Schedule maintenance soon")

    # ✅ SAFE CASE
    else:
        st.success("👍 Machine is in PERFECT condition")
        st.markdown("## 👍 ALL SYSTEMS NORMAL")

# Footer
st.markdown("---")
st.caption("🚀 Built during Hackathon | Smart Monitoring System")
>>>>>>> 7cde2d8d7479511cd00454fca2b521143dd250a3
