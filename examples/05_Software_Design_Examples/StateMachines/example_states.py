import streamlit as st
import time

# Initialize state
if "state" not in st.session_state:
    st.session_state["state"] = "state_start"

# Callback function to change state
# Callback function are triggered when the button is clicked
def go_to_state_start():
    st.session_state["state"] = "state_start"

def go_to_state_a():
    st.session_state["state"] = "state_a"

def go_to_state_b():
    st.session_state["state"] = "state_b"

def go_to_state_exit():
    st.session_state["state"] = "state_exit"

if st.session_state["state"] == "state_start":
    st.text("I'm in start state")   
    st.button("Go to state A!", type="primary", on_click=go_to_state_a)
    st.button("Go to state B!", type="primary", on_click=go_to_state_b)    

elif st.session_state["state"] == "state_a":
    st.text("I'm in state A")
    st.button("Go to exit state!", type="primary", on_click=go_to_state_exit)

elif st.session_state["state"] == "state_b":
    st.text("I'm in state B")
    time.sleep(3)
    go_to_state_exit()
    st.rerun()

elif st.session_state["state"] == "state_exit":
    st.text("I'm in exit state")
    st.button("Restart!", type="primary", on_click=go_to_state_start)
