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