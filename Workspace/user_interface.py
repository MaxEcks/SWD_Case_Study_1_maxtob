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
        # Eingabefelder zum Gerät hinzufügen 
        device_id = st.number_input("Geräte-ID", min_value=0, step=1)
        device_name = st.text_input("Gerätename")
        maintenance_interval = st.number_input("Wartungsintervall in Tage", min_value=1, step=1)
        maintenance_cost = st.number_input("Wartungskosten in Euro", min_value=0.0, step=0.01)
        managed_by_user_id = st.text_input("Verantwortliche Person")
       
        if st.button("Gerät hinzufügen"):
            # Überprüfung ob Geräte-ID schon vorhanden ist
            existing_device = Device.find_by_attribute("device_id", device_id)
            if existing_device:             
                st.error("Geräte-ID ist bereits vorhanden!")

            elif device_id and device_name and managed_by_user_id:
                new_device = Device(
                    device_id = device_id,
                    device_name = device_name,
                    maintenance_interval = maintenance_interval,
                    maintenance_cost = maintenance_cost,
                    managed_by_user_id = managed_by_user_id
                )
                new_device.store_data()
                st.success("Gerät hinzugefügt!")
            else:
                st.error("Bitte alle Felder ausfüllen.")

    with tab2_2:
        # Bestehende Geräte ändern
        
        devices_in_db = Device.find_all()

        device_names = [device.device_name for device in devices_in_db]
        
        selected_device_name = st.selectbox("Wählen Sie ein Gerät aus", device_names)

        if selected_device_name:
            selected_device = Device.find_by_attribute("device_name", selected_device_name)
            
            if selected_device:
                st.write(f"Gerät: {selected_device.device_name}")
                new_device_name = st.text_input("Gerätename", selected_device.device_name)
                new_managed_by_user_id = st.text_input("Verantwortliche Person", selected_device.managed_by_user_id)
                new_maintenance_interval = st.number_input("Wartungsintervall in Tage", min_value=1, step=1, value=selected_device.maintenance_interval)
                new_maintenance_cost = st.number_input("Wartungskosten in Euro", min_value=0.0, step=0.01, value=selected_device.maintenance_cost)

                if st.button("Änderungen speichern"):
                    if new_device_name and new_managed_by_user_id:
                        selected_device.device_name = new_device_name
                        selected_device.managed_by_user_id = new_managed_by_user_id
                        selected_device.maintenance_interval = new_maintenance_interval
                        selected_device.maintenance_cost = new_maintenance_cost
                                     
                        selected_device.store_data()
                        st.success("Gerätedaten wurden aktualisiert!")
                    else: 
                        st.error("Fülle alle Felder aus!")
            else:
                st.error("Gerät nicht gefunden.")

# Konsolen Debugging:
users = User.find_all()
print("All users:")
for user in users:
    print(user)