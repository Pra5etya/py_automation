import queue
import threading

# Membuat objek queue
message_queue = queue.Queue()

# Fungsi untuk mengirim pesan ke queue
def send_message(message):
    message_queue.put(message)
    print(f"Sent message: {message}")

# Fungsi untuk menerima pesan dari queue
def receive_message():
    while True:
        message = message_queue.get()
        print(f"Received message: {message}")

# Membuat thread untuk menerima pesan
receive_thread = threading.Thread(target=receive_message)
receive_thread.start()

# Thread input untuk mengirim pesan
def input_thread():
    while True:
        user_input = input("Enter message (or 'exit' to quit): ")
        # if user_input.lower() == 'exit':
        #     break
        send_message(user_input)

# Membuat thread input
input_thread = threading.Thread(target=input_thread)
input_thread.start()

# Menunggu thread menerima pesan sebelum program berakhir
receive_thread.join()
# Menunggu thread input selesai sebelum program berakhir
input_thread.join()
