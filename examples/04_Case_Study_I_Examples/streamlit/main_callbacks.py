import streamlit as st

st.write("## Wartungskosten")

if "price_euro" not in st.session_state:
    st.session_state.price_euro = 0
if "price_dollar" not in st.session_state:
    st.session_state.price_dollar = 0

# Callbacks for the number inputs
def update_price_from_euro():
    st.session_state.price_dollar = st.session_state.price_euro * 1.1
def update_price_from_dollar():
    st.session_state.price_euro = st.session_state.price_dollar * 0.9

# Number inputs for the maintenance costs
st.number_input(label="Wartungskosten in Euro", 
                             key = "price_euro",                # the key is used to store the value in the session state
                             on_change=update_price_from_euro)
st.number_input(label="Wartungskosten in Dollar", 
                               key = "price_dollar",
                               on_change=update_price_from_dollar)


# Show the current state
st.session_state