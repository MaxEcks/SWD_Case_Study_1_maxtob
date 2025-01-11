import streamlit as st
from users import User
from devices import Device

st.write("# Gerätemanagement")

tab1, tab2 = st.tabs(["Nutzerverwaltung", "Geräteverwaltung"])

with tab1:
    #Nutzer anlegen
    email = st.text_input("E-Mail Adresse eingeben")
    name = st.text_input("Name eingeben")

    st.button("Hinzufügen")
    
    st.button("Nutzer entfernen")

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
