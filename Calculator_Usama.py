import streamlit as st
import emoji

# Initialize expression state
if 'expression' not in st.session_state:
    st.session_state['expression'] = ""

# Define functions
def update_display(value):
    st.session_state['expression'] += value

def calculate_result():
    try:
        st.session_state['expression'] = str(eval(st.session_state['expression']))
    except Exception:
        st.session_state['expression'] = "Error"

def set_operation(op):
    ops = {
        "Addition": "+",
        "Subtraction": "-",
        "Multiplication": "*",
        "Division": "/"
    }
    st.session_state['expression'] += ops.get(op, "")

def clear_input():
    st.session_state['expression'] = ""

# Title
st.title("Calculator_Assignment By (Usama)")

# Hidden text input to allow keyboard typing + Enter
user_input = st.text_input(
    "Hidden",
    value=st.session_state['expression'],
    key="expression_input",
    label_visibility="collapsed"
)

# If the user pressed Enter (i.e., user_input has changed), evaluate it
if user_input != st.session_state['expression']:
    st.session_state['expression'] = user_input
    calculate_result()

# Display current expression or result
st.markdown(f"<h2>{st.session_state['expression']}</h2>", unsafe_allow_html=True)

# Custom CSS for larger buttons
st.markdown("""
    <style>
    div.stButton > button {
        height: 60px;
        width: 100%;
        font-size: 24px;
        margin: 5px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Layout for buttons
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.button("1", on_click=update_display, args=("1",))
    st.button("4", on_click=update_display, args=("4",))
    st.button("7", on_click=update_display, args=("7",))
    st.button(".", on_click=update_display, args=(".",))

with col2:
    st.button("2", on_click=update_display, args=("2",))
    st.button("5", on_click=update_display, args=("5",))
    st.button("8", on_click=update_display, args=("8",))
    st.button("0", on_click=update_display, args=("0",))

with col3:
    st.button("3", on_click=update_display, args=("3",))
    st.button("6", on_click=update_display, args=("6",))
    st.button("9", on_click=update_display, args=("9",))
    st.button("=", on_click=calculate_result)

with col4:
    st.button(emoji.emojize(":heavy_plus_sign:"), on_click=set_operation, args=("Addition",))
    st.button(emoji.emojize(":heavy_minus_sign:"), on_click=set_operation, args=("Subtraction",))
    st.button(emoji.emojize(":heavy_multiplication_x:"), on_click=set_operation, args=("Multiplication",))
    st.button(emoji.emojize(":heavy_division_sign:"), on_click=set_operation, args=("Division",))
    st.button("C", on_click=clear_input)