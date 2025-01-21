import streamlit as st
import pandas as pd

# Start
selected_drink = None
selected_price = 0


# https://docs.streamlit.io/library/api-reference/data/st.data_editor
df = pd.DataFrame(
    [
       {"Getränk":"Cola", "Preis" : 4, "Auswahl" : False},
       {"Getränk":"Fanta","Preis" : 5, "Auswahl" : False},
       {"Getränk":"Beer", "Preis" : 5, "Auswahl" : False},
   ]
)

edited_df = st.data_editor(df,disabled = ("Getränk","Preis"), hide_index = True, on_change=None)

selected_drink = edited_df.loc[edited_df["Auswahl"].idxmax()]["Getränk"]
selected_price = edited_df.loc[edited_df["Auswahl"].idxmax()]["Preis"]


# Bitte Geld einwerfen
st.markdown(f"You selected **{selected_drink}**")
st.markdown(f"Please throw in **{selected_price} €**")


# Geld einwerfen
current_balance = st.number_input('Insert a Coin', min_value=0.0, max_value=5.0, step=0.25, format='%.2f')

# Rückgeld

st.text(f"Your change is {current_balance} €")	
st.button("Return coins", type="primary")

# Ausgabe des Getränks

st.text(f"Have a refreshing {selected_drink} €")
current_balance = current_balance - selected_price
st.text(f"Your change is {current_balance} €")	
