import streamlit as st

st.title("AI Problem Solving System")

option = st.selectbox("Choose System", ["Insurance", "Student Predictor"])

if option == "Insurance":
    st.subheader("Insurance Decision")

    policy = st.checkbox("Policy Active")
    docs = st.checkbox("Documents Valid")
    accident = st.checkbox("Accident Reported")

    if st.button("Check Decision"):
        if not accident:
            st.error("Claim Rejected")
        elif policy and docs:
            st.success("Claim Approved")
        else:
            st.error("Claim Rejected")

elif option == "Student Predictor":
    st.subheader("Student Performance")

    hours = st.number_input("Study Hours", min_value=0.0)
    attendance = st.number_input("Attendance %", min_value=0.0, max_value=100.0)

    if st.button("Predict"):
        score = (hours * 10) + (attendance * 0.5)
        st.write("Predicted Score:", round(score, 2))
        if score >= 50:
            st.success("Result: Pass")
        else:
            st.error("Result: Fail")
