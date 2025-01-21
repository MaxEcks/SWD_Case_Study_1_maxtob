from tinydb import TinyDB, Query
from database_singleton import DatabaseConnector

class User:
    # Class variable that is shared between all instances of the class
    db_connector = DatabaseConnector().get_table('users')

    # Constructor
    def __init__(self, id : str, name : str) -> None:
        """Create a new user based on the given name and id"""
        self.name = name
        self.id = id

    def store_data(self) -> None:
        """Save the user to the database"""
        print("Storing data...")
        # Check if the user already exists in the database (key is the user-id)
        UserQuery = Query()
        result = self.db_connector.search(UserQuery.id == self.id)
        if result:
            # Update the existing record with the current instance's data
            self.db_connector.update(self.__dict__, doc_ids=[result[0].doc_id])
            print("Data updated.")
        else:
            # If the user doesn't exist, insert a new record
            self.db_connector.insert(self.__dict__)
            print("Data inserted.")

    def delete(self) -> None:
        """Delete the user from the database"""
        print("Deleting data...")
        # Check if the user exists in the database (key is the user-id)
        UserQuery = Query()
        result = self.db_connector.search(UserQuery.id == self.id)
        if result:
            # Delete the record from the database
            self.db_connector.remove(doc_ids=[result[0].doc_id])
            print("Data deleted.")
        else:
            print("Data not found.")
    
    # String representation of the class
    def __str__(self):
        return f"{self.name} - {self.id}"
    
    # String representation of the class
    def __repr__(self):
        return self.__str__()
    
    @classmethod
    def find_all(cls) -> list:
        """Find all users in the database"""
        users = []
        for user_data in User.db_connector.all():
            users.append(User(user_data['id'], user_data['name']))
        return users    # return list of User-Objects
    
    @classmethod
    def find_by_attribute(cls, by_attribute: str, attribute_value: str) -> 'User':
        # Load data from the database and create an instance of the User class
        UserQuery = Query()
        result = cls.db_connector.search(UserQuery[by_attribute] == attribute_value)

        if result:
            user_data = result[0]
            return User(user_data['id'], user_data['name']) # return User-Object
        
        return None # return None, if User does not exist

# Module testing:

if __name__ == "__main__":

    user1 = User("user1@mci.edu", "Max Eckstein")
    user2 = User("user2@mci.edu", "Tobias Czermak") 
    user3 = User("user3@mci.edu", "Simon Gleirscher") 
    user4 = User("user4@mci.edu", "Lukas Heiss") 
    
    user1.store_data()
    user2.store_data()
    user3.store_data()
    user4.store_data()
    
    # overwrite user3:
    user5 = User("user3@mci.edu", "Kevin Holzmann") 
    user5.store_data()

    # delete user5 and store data of user3 to database:
    user5.delete()
    user3.store_data()

    # testing find_by_attribute method:
    loaded_user = User.find_by_attribute("name", "Tobias Czermak")
    # loaded_user = User.find_by_attribute("id", "user1@mci.edu")
    if loaded_user:
        print(f"Loaded User: {loaded_user}")
    else:
        print("User not found.")

    users = User.find_all()
    print("All users:")
    for user in users:
        print(user)
    