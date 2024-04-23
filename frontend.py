import streamlit as st


st.image('./assets/Anurag.logo.webp', clamp="False", output_format="PNG")
st.title("Anurag University ChatBot")
st.page_link("https://t.me/@MyAnurag_ExamBot", label="AU ChatBot", help="Click Here to chat with Bot", icon="🔗")

tab1, tab2, tab3 = st.tabs(["Results Inquiry", "Syllabus Information", "General Inquiries"])

with tab1:
   st.header("***Results Inquiry***")
   st.markdown("Get instant access to your examination results.")

with tab2:
   st.header("***Syllabus Information***")
   st.markdown("Retrieve details about the current semester syllabus.")

with tab3:
   st.header("General Inquiries")
   st.markdown("Ask general questions about the college.")

st.subheader("**Steps to Follow**")
st.markdown("* To Start the Bot Greet Him! (e.g., Hey, Hello)")   
st.markdown("* Type your Query") 
st.markdown("* Give this Roll Numbers if you want to see _**Results**_:")
st.code("22eg112a01")
st.code("22eg112a02")


st.caption("Made By: Syed Arshad Ali, Manas, Bharath Ratna ", help="Made by this Brilliant students of IT :sunglasses:")