import queue
import threading
import time
import sys

class Logger:
    def __init__(self):
        self.lock = threading.Lock()

    def log(self, message):
        with self.lock:
            timestamp = time.strftime("[%Y-%m-%d %H:%M:%S] ")
            print(f"{timestamp}{message}")

class MessageQueue:
    def __init__(self, logger):
        self.message_queue = queue.Queue()
        self.lock = threading.Lock()
        self.logger = logger

    def send_message(self, message):
        with self.lock:
            self.message_queue.put(message)
            self.logger.log(f"Sent message: {message}")

    def receive_message(self):
        while True:
            with self.lock:
                try:
                    message = self.message_queue.get_nowait()
                    self.logger.log(f"Received message: {message}")
                except queue.Empty:
                    pass
            time.sleep(1)  # sleep for 1 second to avoid busy-waiting

class MessageSender(threading.Thread):
    def __init__(self, queue_instance, message, logger):
        super().__init__()
        self.queue_instance = queue_instance
        self.message = message
        self.logger = logger

    def run(self):
        while True:
            self.queue_instance.send_message(self.message)
            self.logger.log("Message sent")
            time.sleep(3)  # sleep for 3 seconds before sending the next message

class MessageReceiver(threading.Thread):
    def __init__(self, queue_instance, logger):
        super().__init__()
        self.queue_instance = queue_instance
        self.logger = logger

    def run(self):
        while True:
            self.queue_instance.receive_message()
            self.logger.log("Message received")

# Membuat instance dari kelas Logger dan MessageQueue
logger_instance = Logger()
message_queue_instance = MessageQueue(logger_instance)

# Membuat thread untuk mengirim dan menerima pesan
send_thread = MessageSender(message_queue_instance, "Hello from Sender", logger_instance)
receive_thread = MessageReceiver(message_queue_instance, logger_instance)

# Mulai kedua thread
send_thread.start()
receive_thread.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    # print("Program terminated by user.")
    sys.exit()
