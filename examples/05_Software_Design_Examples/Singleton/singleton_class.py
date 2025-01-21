from typing import Self

class Singleton:
    
    # Class variable
    __instance = None

    def __new__(cls) -> Self:
        # If the class variable is None, create a new instance
        if cls.__instance is None:
            # We can use super() to to call the original __new__ method
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def print(self):
        """
        Prints the id(...) of the objects instance 
        """
        print(F"This singleton's id is {id(self.__instance)}")

if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()

    s1.print()
    s2.print()

    s3 = Singleton()
    s3.print()

    Singleton().print()

    if id(s1) == id(s2) == id(s3):
        print("Our Singleton did it's job!")
    else:
        print("Something went wrong!")