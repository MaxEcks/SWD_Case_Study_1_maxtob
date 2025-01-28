from tinydb import TinyDB, Query
from database_singleton import DatabaseConnector
from datetime import datetime
from datetime import timedelta
import uuid

class Device():
    # Class variable that is shared between all instances of the class
    db_connector = db_connector = DatabaseConnector().get_table('devices')

    # Constructor
    def __init__(self, device_name : str, managed_by_user_id : str, maintenance_interval : int, maintenance_cost : float, end_of_life : datetime, creation_date : datetime = None, last_update : datetime = None) -> None:
        self.device_id = str(uuid.uuid4())
        self.creation_date = creation_date if creation_date else datetime.today().date()
        self.last_update = last_update if last_update else datetime.today().date()
        # ---------------------------------------
        self.end_of_life = end_of_life
        self.device_name = device_name
        self.managed_by_user_id = managed_by_user_id
        self.maintenance_interval = maintenance_interval
        self.maintenance_cost = maintenance_cost
        self.is_active = True
        
    # String representation of the class
    def __str__(self):
        return f'Device: (Name: {self.device_name}, User: {self.managed_by_user_id}, Device ID: {self.device_id})'

    # String representation of the class
    def __repr__(self):
        return self.__str__()
    
    def store_data(self):
        print("Storing data...")
        # Check if the device already exists in the database (key is the device-name)
        DeviceQuery = Query()
        result = self.db_connector.search(DeviceQuery.device_name == self.device_name)
        if result:
            # Update the existing record with the current instance's data
            self.db_connector.update(self.__dict__, doc_ids=[result[0].doc_id])
            print("Data updated.")
        else:
            # If the device doesn't exist, insert a new record
            self.db_connector.insert(self.__dict__)
            print("Data inserted.")
    
    def delete(self):
        print("Deleting data...")
        # Check if the device exists in the database (key is the device-name)
        DeviceQuery = Query()
        result = self.db_connector.search(DeviceQuery.device_name == self.device_name)
        if result:
            # Delete the record from the database
            self.db_connector.remove(doc_ids=[result[0].doc_id])
            print("Data deleted.")
        else:
            print("Data not found.")

    def set_managed_by_user_id(self, managed_by_user_id: str):
        """Expects `managed_by_user_id` to be a valid user id that exists in the database."""
        self.managed_by_user_id = managed_by_user_id

    # Class method that can be called without an instance of the class to construct an instance of the class
    @classmethod
    def find_by_attribute(cls, by_attribute: str, attribute_value: str, num_to_return=-1):   # find_by_attribute should search for all records, therefore default value should be length of the table
        # Load data from the database and create an instance of the Device class
        DeviceQuery = Query()
        result = cls.db_connector.search(DeviceQuery[by_attribute] == attribute_value)

        if result:
            data = result[:num_to_return] if num_to_return > 0 else result
            device_results = []
            for d in data:
                device = cls(
                    device_name=d['device_name'],
                    managed_by_user_id=d['managed_by_user_id'],
                    maintenance_interval=d['maintenance_interval'],
                    maintenance_cost=d['maintenance_cost'],
                    end_of_life=d['end_of_life'],
                    creation_date=d['creation_date'],
                    last_update=d['last_update']
                )
                device.device_id = d['device_id']
                device_results.append(device)
            return device_results
        else:
            return []  # Keine Ergebnisse gefunden

    @classmethod
    def find_all(cls) -> list:
        # Load all data from the database and create instances of the Device class
        devices = []
        for device_data in cls.db_connector.all():
            device = cls(
                device_name=device_data['device_name'],
                managed_by_user_id=device_data['managed_by_user_id'],
                maintenance_interval=device_data['maintenance_interval'],
                maintenance_cost=device_data['maintenance_cost'],
                end_of_life=device_data['end_of_life'],
                creation_date=device_data['creation_date'],
                last_update=device_data['last_update']
            )
            device.device_id = device_data['device_id']
            devices.append(device)
        return devices

    def calculate_maintenance_in_period(self, start_date, end_date):
        """Berechnung aller Wartungen und den dazugehoerigen Kosten im ausgewählten Zeitintervall"""
        #current_date = max(self.creation_date, start_date)
        maintenances = []
        total_cost = 0

        end_of_life_date = min(self.end_of_life, end_date)
        current_date = current_date = self.creation_date + timedelta(days=self.maintenance_interval)
        while current_date <= end_of_life_date:
            if start_date <= current_date <= end_date:
                maintenances.append(current_date)
                total_cost = total_cost + self.maintenance_cost
            current_date = current_date + timedelta(days = self.maintenance_interval)
        
        return maintenances, total_cost

        
# Module testing:

if __name__ == "__main__":
    
    device1 = Device("Waschmaschine", "user1@mci.edu", 30, 10.0, datetime(2026, 12, 31).date())
    device2 = Device("3D-Drucker", "user2@mci.edu", 7, 5.0, datetime(2026, 12, 31).date())
    device3 = Device("PC 1", "user2@mci.edu", 365, 100.0, datetime(2026, 12, 31).date()) 
    device4 = Device("Lötstation", "user4@mci.edu", 90, 20.0, datetime(2026, 12, 31).date()) 
    device1.store_data()
    device2.store_data()
    device3.store_data()
    device4.store_data()

    # overwrite device3:
    device5 = Device("PC 1", "user3@mci.edu", 365, 100.0, datetime(2026, 12, 31).date()) 
    device5.store_data()

    # testing find_by_attribute method:
    # loaded_device = Device.find_by_attribute("device_name", "Device2")
    loaded_device = Device.find_by_attribute("managed_by_user_id", "user2@mci.edu")
    if loaded_device:
        print(f"Loaded Device: {loaded_device}")
    else:
        print("Device not found.")

    devices = Device.find_all()
    print("All devices:")
    for device in devices:
        print(device)

    # print(len(DatabaseConnector().get_table('devices')))
    
    