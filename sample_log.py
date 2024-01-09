import logging

# Konfigurasi logging
logging.basicConfig(filename = 'example.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def main():
    try:
        # Mendapatkan input dari pengguna
        user_input = input("Enter something: ")

        # Menuliskan input ke dalam log
        logging.info(f'User entered: {user_input}')

        # Lakukan operasi lainnya di sini sesuai kebutuhan
        # ...

    except Exception as e:
        # Tangkap dan log pengecualian (jika ada)
        logging.error(f'An error occurred: {str(e)}')

if __name__ == "__main__":
    main()
