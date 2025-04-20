# Youtube Link = https://www.youtube.com/watch?v=J6wzj-z6i7Q
# import streamlit as st
# import pandas as pd
# # st.title("Jai Guru Ji")
# # st.header("Welcome to my Website")
# # st.subheader("Hello World")
# st.header("Welcome to my website")
# # st.markdown("""Hello World
# # My Name is Reetesh Kumar Shukla""")
# dataset = pd.read_excel("Log Book.xlsx")
# st.dataframe(dataset)

# ********************************** Website Making Project **************************************
import streamlit as st
st.subheader("Welcome to My Website")
st.title("This is a basic input website")
name = st.text_input("Enter your name: ")
dropdown = st.selectbox("Select your Gender: ", ("Male", "Female"))
email = st.text_input("Enter your Email: ")
p_number = st.text_input("Enter your Phone Number: ")
text = st.text_area("Write your Message Here: ")

button = st.button("Done")

if button == True:
    st.markdown(f"""
    Your Name = {name}\n
    Your Gender = {dropdown}\n
    Your Email = {email}\n
    Your Phone Number = {p_number}\n
    Your Message = {text}
    """)
