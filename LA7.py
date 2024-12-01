class Laptop:
    def __init__(self, merk, processor, harga):
        self.merk = merk
        self.processor = processor
        self.harga = harga
        print(f"Laptop {self.merk} processor {self.processor} dengan harga {self.harga}")

merk_= input("Masukkan merk laptop: ")
spesifikasi_ = input("Masukkan spek laptop: ")
harga_ = input("Masukkan harga laptop: ")
print("=" * 90)

Laptop1 = Laptop(merk_, spesifikasi_, harga_)
