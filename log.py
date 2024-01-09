import logging
import time
import sys

# Konfigurasi logging
logging.basicConfig(filename='.example.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# param
i = 1

# Contoh loop
def main(i): 
    while True:
        try: 
            logging.info(f'Iterasi ke-{i}: Proses berjalan...')
            i  = i + 1
            # Lakukan beberapa pekerjaan di dalam loop
            time.sleep(1)

            # Menutup file log saat iterasi selesai
            logging.shutdown()

            # Membuka file log kembali dalam mode 'a' (append)
            logging.basicConfig(filename='example.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filemode='a')

            # # Melanjutkan log setelah file log dibuka kembali
            # logging.info('Proses setelah membuka kembali file log')

            if (i == 30):
                # break
                sys.exit()

        except Exception as e: 
            logging.error(f'An error occurred: {str(e)}')

if __name__ == "__main__":
    main(2) # parameter must define in function