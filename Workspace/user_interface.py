import streamlit as st

st.write("# Gerätemanagement")

tab1, tab2, tab3, tab4 = st.tabs(["Nutzerverwaltung", "Geräteverwaltung", "Reservierung", "Wartungsmanagement"])

with tab1:
    #Nutzer anlegen
    email = st.text_input("E-Mail Adresse eingeben")
    name = st.text_input("Name eingeben")

    st.button("Hinzufügen")

with tab2:
    #Geräteverwaltung
    tab2_1, tab2_2 = st.tabs(["Gerät anlegen", "Gerät ändern"])
    with tab2_1:
        device_id = st.number_input("Geräte-ID", min_value=0, step=1)
        device_name = st.text_input("Gerätename")
        maintenance_interval = st.number_input("Wartungsintervall in Tage", min_value=1, step=1)
        maintenance_cost = st.number_input("Wartungskosten in Euro", min_value=0.0, step=0.01)
        responsible_user = st.text_input("Verantwortliche Person") #Besser mit einer selectbox? (kann erst nach der Implementierung der Datenbank implementiert werden)
        st.button("Gerät hinzufügen")
    
    with tab2_2:
        pass #Hier (Gerät ändern) muss man noch den Aufruf eines bestehenden Gerätes implementieren (z.B. selectbox). Kann aber erst nach der Implementierung der
             #Datenbank gemacht werden

with tab3:
    #Reservierung
    """
    user_email = st.selectbox("E-Mail-Adresse des Nutzers")
    device_id = st.selectbox("Wähle das Gerät")

    """
    start_date = st.date_input("Startdatum")
    end_date = st.date_input("Enddatum")

    st.button("Reservierung hinzufügen")

with tab4:
    st.write("### Nächsten Wartungstermine")

    st.write("### Wartungskosten für das Quartal")


