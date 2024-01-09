import queue
import threading
import logging

# log configuration
logging.basicConfig(filename = '.example.log', level = logging.INFO, format = '%(asctime)s ; %(message)s')

# initialize message queue
message_queue = queue.Queue()

# function to send message queue
def send_message(message):
    try: 
        message_send = 'send'
        message_queue.put(message)

        # write into log
        logging.info(f'message send: {message_send}')

        print(f"Sent message: {message_send}")
    
    except Exception as e:
        # error read
        logging.error(f'An error occurred: {str(e)}')

# function to receive message queue
def receive_message():
    while True:
        try: 
            message = message_queue.get()

            # write into log
            logging.info(f'receive send: {message}')

            print(f"Received message: {message}")
        
        except Exception as e:
            logging.error(f'An error occurred: {str(e)}')

# initialize receive message queue
receive_thread = threading.Thread(target = receive_message)
receive_thread.start()

# input message queue
def input_thread():
    while True:
        try:     
            user_input = input("Enter message (or 'exit' to quit): ")
            # if user_input.lower() == 'exit':
            #     break
            
            # write into log
            logging.info(f'input send: {user_input}')

            send_message(user_input)
        
        except Exception as e: 
            logging.error(f'An error occurred: {str(e)}')

# initialize input message queue
input_thread = threading.Thread(target = input_thread)
input_thread.start()

# wait message queue before kill the app
receive_thread.join()
input_thread.join()