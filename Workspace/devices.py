from tinydb import TinyDB, Query
from database_singleton import DatabaseConnector
import uuid

class Device():
    # Class variable that is shared between all instances of the class
    db_connector = db_connector = DatabaseConnector().get_table('devices')

    # Constructor
    def __init__(self, device_name : str, managed_by_user_id : str, maintenance_interval : int, maintenance_cost : float) -> None:
        self.device_id = str(uuid.uuid4())
        self.device_name = device_name
        # The user id of the user that manages the device
        # We don't store the user object itself, but only the id (as a key)
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
                    maintenance_cost=d['maintenance_cost']
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
                maintenance_interval=device_data.get('maintenance_interval'),
                maintenance_cost=device_data.get('maintenance_cost')
            )
            device.device_id = device_data['device_id']
            devices.append(device)
        return devices

# Module testing:

if __name__ == "__main__":
    
    device1 = Device("Waschmaschine", "user1@mci.edu", 30, 10.0)
    device2 = Device("3D-Drucker", "user2@mci.edu", 7, 5.0) 
    device3 = Device("PC 1", "user2@mci.edu", 365, 100.0) 
    device4 = Device("Lötstation", "user4@mci.edu", 90, 20.0) 
    device1.store_data()
    device2.store_data()
    device3.store_data()
    device4.store_data()

    # overwrite device3:
    device5 = Device("PC 1", "user3@mci.edu", 365, 100.0) 
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
    
    