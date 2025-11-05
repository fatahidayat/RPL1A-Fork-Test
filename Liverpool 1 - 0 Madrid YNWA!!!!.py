# LOGIN USER
username_benar = "fatah"
password_benar = "joestar123"
maks_percobaan = 3
percobaan = 0

while (percobaan < maks_percobaan):
    username = input("username: ")
    password = input("password: ")

    if (username == username_benar and password == password_benar):
        print("login berhasil")
        break
    else:
        percobaan += 1
        sisa = 3 - percobaan
        print(f"login gagal, kesempatan tersisa: {sisa}")

    if (percobaan == maks_percobaan):
        print("gagal login 3 kali, silahkan hubungi CS.")
        break

# GANJIL GENAP
while True:
    angka = int(input("masukkan angka (angka negatif untuk keluar): "))

    if (angka < 0):
        print(f"angka {angka} adalah NEGATIF, program dihentikan")
        break

    if (angka % 2 == 0):
        print(f"angka {angka} adalah GENAP  ")
    else:   
        print(f"angka {angka} adalah GANJIL")


# Input Produk dan Total Belanja
produk = {}
jumlah_produk = int(input("jumlah produk yang ingin diinput: "))

for i in range(jumlah_produk):
    print(f"produk ke {i+1}")
    nama = input("nama produk: ")
    total = float(input("harga produk (Rp): "))
    produk[nama] = total

for nama, total in produk.items():  
    print(f"{nama} : Rp{total:}")

total_semua = sum(produk.values())
print("total keseluruhan belanja: Rp{:}".format(total_semua))

