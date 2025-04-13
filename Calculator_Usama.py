import streamlit as st
import emoji

# Initialize session state
if 'expression' not in st.session_state:
    st.session_state['expression'] = ""
if 'just_evaluated' not in st.session_state:
    st.session_state['just_evaluated'] = False

# Define functions
def update_display(value):
    if st.session_state['just_evaluated']:
        st.session_state['expression'] = ""
        st.session_state['just_evaluated'] = False
    st.session_state['expression'] += value

def calculate_result():
    try:
        st.session_state['expression'] = str(eval(st.session_state['expression']))
    except Exception:
        st.session_state['expression'] = "Error"
    st.session_state['just_evaluated'] = True

def set_operation(op):
    ops = {
        "Addition": "+",
        "Subtraction": "-",
        "Multiplication": "*",
        "Division": "/"
    }
    if st.session_state['expression'] and st.session_state['expression'][-1] not in "+-*/":
        st.session_state['expression'] += ops.get(op, "")
    st.session_state['just_evaluated'] = False

def clear_input():
    st.session_state['expression'] = ""
    st.session_state['just_evaluated'] = False

# Title
st.title("Calculator (Usama)")

# Hidden text input to allow keyboard typing + Enter
user_input = st.text_input(
    "Hidden",
    value=st.session_state['expression'],
    key="expression_input",
    label_visibility="collapsed"
)

# If the user pressed Enter (expression changed), evaluate it
if user_input != st.session_state['expression']:
    if st.session_state['just_evaluated']:
        st.session_state['expression'] = user_input  # fresh input overwrites result
        st.session_state['just_evaluated'] = False
    else:
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

# Button layout
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
    st.button("AC", on_click=clear_input)
