import streamlit as st
st.title('Welcome to Calculator (Usama)')
first_number = st.number_input("Enter first number")
second_number = st.number_input("Enter second number")
status = st.radio('Select your operation: ',
                  ('Addition', 'Subtraction', 'Multiplication', 'Division'))
if(status == 'Addition'):
    Calculate = first_number + second_number
elif(status == 'Subtraction'):
    Calculate = first_number - second_number
elif(status == 'Multiplication'):
    Calculate = first_number * second_number
elif(status == 'Division'):
    Calculate = first_number / second_number
if (st.button('Calculate')):
    st.text(f'Your Answer is {Calculate}')
