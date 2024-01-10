class sample():
    # inisialisasi variabel
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    # masukan param self pada setiap fungsi yang akan dibuat
    def sample1(self): 
        print(f"sample pertama yakni: {self.param1}")

    def sample2(self): 
        print(f"sample kedua yakni: {self.param2}")

    def run_sample(self): 
        self.sample1()
        self.sample2()

# input
input1 = input("Masukan sampel parameter: ")
input2 = input("Masukan sampel parameter: ")

# membuat object dari class
obj1 = sample(param1 = input1, param2 = input2)

# memanggil fungsi dari objek
obj1.run_sample()