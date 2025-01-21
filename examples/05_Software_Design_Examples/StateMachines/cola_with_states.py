import streamlit as st
import pandas as pd
import time

# Callback function to change state
def got_to_state_start():
    st.session_state["state"] = "state_start"

def got_to_state_auswahl_anfordern():
    st.session_state["state"] = "state_auswahl_anfordern"

def got_to_state_bezahlung_anfordern():
    st.session_state["state"] = "state_bezahlung_anfordern"

def got_to_state_rueckgeld_ausgeben():
    st.session_state["state"] = "state_rueckgeld_ausgeben"

def got_to_state_ware_ausgeben():
    st.session_state["state"] = "state_ware_ausgeben"

# Initialize state
if "state" not in st.session_state:
    st.text("I'm in start state")
    got_to_state_auswahl_anfordern()
    st.rerun()

elif st.session_state["state"] == "state_auswahl_anfordern":
    st.text("I'm in state_auswahl_anfordern")
    df = pd.DataFrame(
    [
       {"Getränk":"Cola", "Preis" : 4, "Auswahl" : False},
       {"Getränk":"Fanta","Preis" : 5, "Auswahl" : False},
       {"Getränk":"Beer", "Preis" : 5, "Auswahl" : False},
       {"Getränk":"Club Mate", "Preis" : 3, "Auswahl" : False}
    ]
    )

    edited_df = st.data_editor(df,disabled = ("Getränk","Preis"), hide_index = True, on_change=None)
    st.session_state["selected_drink"] = edited_df.loc[edited_df["Auswahl"].idxmax()]["Getränk"]
    st.session_state["selected_price"] = edited_df.loc[edited_df["Auswahl"].idxmax()]["Preis"]
    
    st.button(F"Order {st.session_state['selected_drink']}", type="primary",on_click=got_to_state_bezahlung_anfordern)

elif st.session_state["state"] == "state_bezahlung_anfordern":
    st.text("I'm in state state_bezahlung_anfordern")
    # Bitte Geld einwerfen
    st.markdown(f"You selected **{st.session_state['selected_drink']}**")
    st.markdown(f"Please throw in **{st.session_state['selected_price']} €**")

    # Geld einwerfen
    st.session_state["current_balance"] = st.number_input('Insert a Coin', min_value=0.0, max_value=10.0, step=0.5, format='%.2f')

    st.button("Return coins", type="primary",on_click=got_to_state_rueckgeld_ausgeben)
    
    if st.session_state["current_balance"] >= st.session_state["selected_price"]:
        got_to_state_ware_ausgeben()
        st.rerun()

elif st.session_state["state"] == "state_rueckgeld_ausgeben":
    st.text("I'm in state_rueckgeld_ausgeben")
    # Rückgeld
    st.text(f"Your change is {st.session_state['current_balance']} €")	
    
elif st.session_state["state"] == "state_ware_ausgeben":
    st.text("I'm in state_ware_ausgeben")
    st.text(f"**Have a refreshing {st.session_state['selected_drink']}!**")
    


