import threading
import queue
import time

class MessageQueue:
    def __init__(self):
        self._queue = queue.Queue()

    def put_message(self, message):
        self._queue.put(message)

    def get_message(self):
        return self._queue.get()

def producer(queue, messages):
    for message in messages:
        print(f"Producing: {message}")
        queue.put_message(message)
        time.sleep(1)

def consumer(queue):
    while True:
        message = queue.get_message()
        print(f"Consuming: {message}")
        time.sleep(1)

if __name__ == "__main__":
    my_queue = MessageQueue()

    # Membuat dua thread, satu untuk produsen dan satu untuk konsumen
    producer_thread = threading.Thread(target=producer, args=(my_queue, ["Message 1", "Message 2", "Message 3"]))
    consumer_thread = threading.Thread(target=consumer, args=(my_queue,))

    # Memulai thread
    producer_thread.start()
    consumer_thread.start()

    # Menunggu kedua thread selesai
    producer_thread.join()
    consumer_thread.join()
