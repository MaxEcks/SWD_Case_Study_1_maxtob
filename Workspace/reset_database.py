from users import User
from devices import Device

def clear_database():
    # Lösche alle Benutzer
    users = User.find_all()
    for user in users:
        user.delete()

    # Lösche alle Geräte
    devices = Device.find_all()
    for device in devices:
        device.delete()

if __name__ == "__main__":
    clear_database()
    print("Datenbank wurde geleert.")