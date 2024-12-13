import streamlit as st

def update_name_tab_1():
    st.session_state.name = st.session_state.ti_tab1_name
    st.session_state.ti_tab2_name = st.session_state.ti_tab1_name

def run():
    st.title("Tab 1")
    # key erstellt eine eindeutige ID für das Element gleichzeitig wird der Wert in der Session gespeichert
    # on_change wird ausgeführt, wenn sich der Wert ändert
    st.text_input("Enter animal name", key="ti_tab1_name", on_change=update_name_tab_1)
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)