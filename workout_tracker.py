import streamlit as st

st.title('George Dean III Workout Tracker Dashboard')
question = st.text_input("Enter the workouts for today: ")
if(st.button('Submit')):
    result = question.title()
    st.success(result)

