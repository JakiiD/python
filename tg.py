def show_menu():
    print("""
    ==========================================
    SELAMAT DATANG DI RM. PADANG SIGIT RENDANG
    ==========================================
    1. Lihat Menu Makanan
    2. Ketersedian Makanan
    3. Beli Makanan
    4. Cetak Struk
    5. Exit
    """)

def lihat_makanan():
    print("\n List Menu Makanan: ")
    print("1. Nasi Rendang : Rp 23000 /porsi")
    print("2. Nasi Ayam Bakar : Rp 20000 /porsi ")
    print("3. Nasi Gulai Ayam: Rp 20000 /porsi")

def cek_ketersediaan(Rendang, Ayam_Bakar, Ayam_Gulai):
    print("\n List Ketersedian Makanan: ")
    print(f"1. Nasi Rendang : {Rendang}")
    print(f"2. Nasi Ayam Bakar : {Ayam_Bakar}")
    print(f"3. Nasi Gulai Ayam : {Ayam_Gulai}")

def Beli_Makanan(saldo, Rendang, Ayam_Bakar, Ayam_Gulai):
    lihat_makanan()
    nama_pembeli = input("Masukkan Nama Pembeli: ")
    pilihan = input("Pilih makanan yang akan dibeli: ")
    if pilihan == '1':
        saldo
        menu = "Nasi Rendang"
        harga = 23000
        jumlah = int(input('Berapa Porsi Nasi Rendang: '))
        total = harga * jumlah
        pembelian = saldo - total
        nama = nama_pembeli
        if Rendang < jumlah:
            print("maaf stok tak tersedia")
        else:
            print(f"Berhasil membeli {menu} seharga {total}")
            print(f"saldo anda sisa: {pembelian}")
            print(f"Terimakasih {nama_pembeli} telah berbelanja di RM.PADANG SIGIT RENDANG")
            try:
                with open('struk.txt','a') as struk:
                    struk.write("===============\n")
                    struk.write("STRUK PEMBELIAN\n")
                    struk.write("===============\n")
                    struk.write(f"Nama Makanan: {menu} \n")
                    struk.write(f"Harga Satuan: {harga} \n")
                    struk.write(f"Total: {total}\n")
                    struk.write(f"Saldo: {saldo}\n")
                    struk.write(f"Sisa saldo: {pembelian}\n")
                    struk.write(f"Nama Pembeli: {nama}\n")
            except Exception as e:
                print(e)

    elif pilihan == '2':
        saldo
        menu = "Nasi Ayam Bakar"
        harga = 20000
        jumlah = int(input('Berapa Porsi Nasi Ayam Bakar: '))
        total = harga * jumlah
        pembelian = saldo - total
        nama = nama_pembeli
        if Ayam_Bakar < jumlah:
            print("maaf stok tak tersedia")
        else:
            print(f"Berhasil membeli {menu} seharga {total}")
            print(f"saldo anda sisa: {pembelian}")
            print(f"Terimakasih {nama_pembeli} telah berbelanja di RM.PADANG SIGIT RENDANG")
            try:
                with open('struk.txt','a') as struk:
                    struk.write("===============\n")
                    struk.write("STRUK PEMBELIAN\n")
                    struk.write("===============\n")
                    struk.write(f"Nama Makanan: {menu} \n")
                    struk.write(f"Harga Satuan: {harga} \n")
                    struk.write(f"Total: {total}\n")
                    struk.write(f"Saldo: {saldo}\n")
                    struk.write(f"Sisa saldo: {pembelian}\n")
                    struk.write(f"Nama Pembeli: {nama}\n")
            except Exception as e:
                print(e)

    elif pilihan == '3':
        saldo
        menu = "Nasi Ayam Gulai"
        harga = 20000
        jumlah = int(input('Berapa Porsi Nasi Ayam Gulai: '))
        total = harga * jumlah
        pembelian = saldo - total
        nama = nama_pembeli
        if Ayam_Gulai < jumlah:
            print("maaf stok tak tersedia")
        else:
            print(f"Berhasil membeli {menu} seharga {total}")
            print(f"saldo anda sisa: {pembelian}")
            print(f"Terimakasih {nama_pembeli} telah berbelanja di RM.PADANG SIGIT RENDANG")
            try:
                with open('struk.txt','a') as struk:
                    struk.write("===============\n")
                    struk.write("STRUK PEMBELIAN\n")
                    struk.write("===============\n")
                    struk.write(f"Nama Makanan: {menu} \n")
                    struk.write(f"Harga Satuan: {harga} \n")
                    struk.write(f"Total: {total}\n")
                    struk.write(f"Saldo: {saldo}\n")
                    struk.write(f"Sisa saldo: {pembelian}\n")
                    struk.write(f"Nama Pembeli: {nama}\n")
            except Exception as e:
                print(e)


def exit():
    print("Terima kasih telah berbelanja disini")

def cetak_struk():
    try:
        with open("struk.txt","r") as strk:
            lihat = strk.read()
            print(lihat)
    except Exception as e:
        print(e)

def main():
    saldo = 100000
    Rendang = 20
    Ayam_Bakar = 20
    Ayam_Gulai = 20


    while True:

        show_menu()
        inputan = input("Pilih menu (1-5): ")
        if inputan == '1':
            lihat_makanan()
        elif inputan == '2':
            cek_ketersediaan(Rendang, Ayam_Bakar, Ayam_Gulai)
        elif inputan == '3':
            Beli_Makanan(saldo, Rendang, Ayam_Bakar, Ayam_Gulai)
        elif inputan == '4':
            cetak_struk()
        elif inputan == '5':
            exit()
            break
        else:
            print("maaf, inputan tidak tersedia")

if __name__ == "__main__":
    main()
