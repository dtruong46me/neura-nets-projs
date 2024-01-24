import streamlit as st

st.title("Deep Learning Projects")
st.caption("For Computer Vision Tasks")

st.write("**In this system, I focus on some projects of Computer Vision tasks:**")
st.write("- Cat vs Dog Classification")
st.write("- Car Detection")
st.write("- Facial Verification")
st.write("- Counting Objects")
st.write("- Pneumonia Detection")
st.write("- Art Generation")
st.write("- CAPCHA Recognition")

st.write("For each Deep Learning Project, I will provide you a guideline to test the model. I also provide some information of the **dataset**, **method**, **model(s)**,... and the accuracy of trained model. I hope I will recieve the feedback from you guys to increase the accuracy of the model.")
st.write("Thank you!")

message = st.text_area("Message", placeholder="Your message...", )
if st.button("Submit"):
    st.write("Thank you for your feedback!")
