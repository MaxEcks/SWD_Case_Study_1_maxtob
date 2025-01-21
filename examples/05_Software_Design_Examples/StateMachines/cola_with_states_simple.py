import streamlit as st
import time

# Initialize state
if "state" not in st.session_state:
    st.session_state["state"] = "state_start"

if "getraenk" not in st.session_state:
    st.session_state["getraenk"] = None

if "price" not in st.session_state:
    st.session_state["price"] = "0.0"

# Callback function to change state
# Callback function are triggered when the button is clicked

def go_to_state_start():
    st.session_state["state"] = "state_start"

def go_to_state_zahlen_via_cola():
    st.session_state["state"] = "state_zahlen"
    st.session_state["getraenk"] = "Cola"
    st.session_state["price"] = 4.0

def go_to_state_zahlen_via_mate():
    st.session_state["state"] = "state_zahlen"
    st.session_state["getraenk"] = "Club Mate"
    st.session_state["price"] = 3.0

def go_to_state_ausgabe():
    st.session_state["state"] = "state_ausgabe"

def go_to_state_rueckgeld():
    st.session_state["state"] = "state_rueckgeld"

def go_to_state_exit():
    st.session_state["state"] = "state_exit"

if st.session_state["state"] == "state_start":
    st.text("Bitte Getränk auswählen")   
    st.button("Cola - 4 €",      type="primary", on_click=go_to_state_zahlen_via_cola)
    st.button("Club Mate - 3 €", type="primary", on_click=go_to_state_zahlen_via_mate)    

elif st.session_state["state"] == "state_zahlen":
    st.text("Bitte Bezahlen")
    st.button("Bezahlen!", type="primary", on_click=go_to_state_ausgabe)
    st.button("Rückgeld!", type="primary", on_click=go_to_state_rueckgeld)

elif st.session_state["state"] == "state_ausgabe":
    st.text(F"Have a refreshing {st.session_state['getraenk']}")
    go_to_state_exit()
    time.sleep(3)
    st.rerun()

elif st.session_state["state"] == "state_rueckgeld":
    st.text(F"Your change is {st.session_state['price']} €")
    go_to_state_exit()
    time.sleep(3)
    st.rerun()

elif st.session_state["state"] == "state_exit":
    st.text("I'm in exit state")
    st.button("Restart!", type="primary", on_click=go_to_state_start)
