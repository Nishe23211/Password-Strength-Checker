
import streamlit as st
from password_analyzer import analyze_password
from password_generator import generate_password

st.set_page_config(
    page_title="Password Security Analyzer",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ Password Security Analyzer")
st.caption("Cybersecurity Project 2 | Python + Streamlit + zxcvbn")

st.info(
    "Privacy Notice: Use fictional test passwords only. "
    "Do not enter real passwords."
)

password = st.text_input(
    "Enter a sample password",
    type="password"
)

if password:
    result = analyze_password(password)
    score = result["score"]

    colors = {
        0: "red",
        1: "red",
        2: "orange",
        3: "blue",
        4: "green"
    }

    st.subheader("Security Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric("Password Length", len(password))
    col2.metric("Strength", result["strength"])
    col3.metric("Estimated Guesses", f"{result['guesses']:,}")

    st.subheader("Password Strength")

    st.progress(
        (score + 1) / 5,
        text=f"Strength Level: {result['strength']} ({score}/4)"
    )

    st.subheader("Password Composition")

    checks = {
        "Uppercase Letters": any(c.isupper() for c in password),
        "Lowercase Letters": any(c.islower() for c in password),
        "Numbers": any(c.isdigit() for c in password),
        "Special Characters": any(not c.isalnum() for c in password),
        "12+ Characters": len(password) >= 12,
        "16+ Characters": len(password) >= 16
    }

    for check, passed in checks.items():
        if passed:
            st.success(f"✓ {check}")
        else:
            st.warning(f"– {check}: Not present")

    st.subheader("Security Recommendations")

    if result["warning"]:
        st.warning(result["warning"])

    if result["suggestions"]:
        for suggestion in result["suggestions"]:
            st.write("•", suggestion)
    else:
        st.write("No additional suggestions from the analyzer.")

    if score == 4:
        st.success(
            "High estimated resistance to guessing. "
            "This does not guarantee password security."
        )
    elif score <= 1:
        st.error("This sample password is highly predictable.")
    else:
        st.info("Consider a longer, less predictable passphrase.")

else:
    st.write("Enter a fictional sample password to begin analysis.")


st.divider()

st.header("🔐 Secure Password Generator")

password_length = st.slider(
    "Select Password Length",
    min_value=12,
    max_value=32,
    value=16
)

if st.button("Generate Secure Password"):
    generated_password = generate_password(password_length)

    st.code(generated_password, language=None)

    st.info(
        "Use a trusted password manager to store generated passwords."
    )
