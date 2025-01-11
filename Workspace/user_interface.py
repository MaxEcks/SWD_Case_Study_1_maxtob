import streamlit as st
from users import User
from devices import Device
import time

st.write("# Gerätemanagement")

tab1, tab2, tab3, tab4 = st.tabs(["Nutzerverwaltung", "Geräteverwaltung", "Reservierung", "Wartungsmanagement"])

with tab1:
    # Untertabs für Nutzerverwaltung:
    tab1_1, tab1_2, tab1_3 = st.tabs(["Nutzer anlegen", "Nutzer anzeigen", "Nutzer ändern"])

    # Nutzer anlegen:
    with tab1_1:
        st.write("### Neuen Nutzer anlegen:")
        name = st.text_input("Name eingeben")
        email = st.text_input("E-Mail Adresse eingeben")

        if st.button("Hinzufügen"):
            existing_user = User.find_by_attribute("id", email)
            
            if existing_user:
                st.error(f"Benutzer mit dieser Email-Adresse existiert bereits: {existing_user}")
                time.sleep(3)
                st.rerun()

            else:
                new_user = User(email, name)
                new_user.store_data()
                st.success(f"Neuer Benutzer hinzugefügt: {new_user}")
                time.sleep(3)
                st.rerun()

    # Nutzer anzeigen:
    with tab1_2:
        st.write("### Liste aller Nutzer:")
        users = User.find_all()
        for user in users:
            st.write(f"Name: {user.name}, E-Mail: {user.id}")

        if st.button("Aktualisieren"):
            st.success("Aktualisieren erfolgreich.")
            time.sleep(3)
            st.rerun()

    # Nutzer ändern:
    with tab1_3:
        st.write("### Nutzer ändern:")

        users = User.find_all()
        user_options = {f"{user.name} ({user.id})": user for user in users}
        selected_user = st.selectbox("Wählen Sie einen Nutzer aus", list(user_options.keys()))

        if selected_user:
            user_to_edit = user_options[selected_user]
            new_name = st.text_input("Name ändern", value=user_to_edit.name, key="edit_name")
            new_email = st.text_input("E-Mail ändern", value=user_to_edit.id, key="edit_email")

            if st.button("Änderungen speichern"):
                # User Daten ändern:
                user_to_edit.name = new_name
                user_to_edit.id = new_email
                user_to_edit.store_data()
                st.success(f"Benutzerdaten aktualisiert: {user_to_edit}")
                time.sleep(3)
                st.rerun()

            if st.button("Benutzer löschen"):
                user_to_edit.delete()
                st.success(f"Benutzer gelöscht.")
                time.sleep(3)
                st.rerun()

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

# Konsolen Debugging:
users = User.find_all()
print("All users:")
for user in users:
    print(user)