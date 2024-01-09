class sample:
    def __init__(self, nama_objek):
        self.nama_objek = nama_objek

    def first(self):
        print(f"{self.nama_objek}: Ini adalah fungsi satu")

    def second(self):
        print(f"{self.nama_objek}: Ini adalah fungsi dua")

    def third(self):
        print(f"{self.nama_objek}: Ini adalah fungsi tiga")

    def run_oop(self):
        self.first()
        self.second()
        self.third()

# Input nama objek dari pengguna
nama_objek_input = input("Masukkan nama objek: ")

# Membuat objek dari class ContohClass dengan nama yang diinput
objek = sample(nama_objek_input)

# Memanggil fungsi-fungsi di dalam objek
objek.run_oop()
