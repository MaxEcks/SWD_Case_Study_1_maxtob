import threading
import os

# Eine Funktion, die in eine Datei schreibt
def write_to_file(thread_id):
    filepath = os.path.dirname(os.path.abspath(__file__))
    try:
        with open(os.path.join(filepath, 'example.txt'), 'a') as f:
            f.write(f"Thread {thread_id} started writing\n")
    except Exception as e:
        print(f"Error writing to file by thread {thread_id}: {e}")

# Erstelle mehrere Threads, die gleichzeitig schreiben
threads = []
for i in range(100):
    thread = threading.Thread(target=write_to_file, args=(i,))
    threads.append(thread)
    thread.start()

# Warten, bis alle Threads fertig sind
for thread in threads:
    thread.join()