import threading
import os

# The Logger class is a Singleton class that writes log messages to a file
class Logger:
    __instance = None

    # The lock ensures that only one thread can create the instance by checking if it is None
    __lock = threading.Lock()

    def __new__(cls, log_file):
        # Here we use the lock additionally to ensure that only one thread can create the instance
        with cls.__lock:
            if cls.__instance is None:
                cls.__instance = super().__new__(cls) 
                cls.__instance.log_file = log_file
        return cls.__instance

    def log(self, message):
        # Here we use the lock to ensure that only one thread can write to the file at a time
        with self.__lock:
            with open(self.log_file, "a") as f:
                f.write(message + "\n")

if __name__ == "__main__":
    def log_from_thread(thread_id):
        filepath = os.path.dirname(os.path.abspath(__file__))
        logfile = os.path.join(filepath, "log.txt")  
        
        logger = Logger(logfile)
        logger.log(f"Hello from thread {thread_id}")

    threads = []
    for i in range(100):
        thread = threading.Thread(target=log_from_thread, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
