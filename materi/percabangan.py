# angka = int(input("masukan angka: "))
# if angka > 0:
#     print(angka,"adalah bilangan positif.")
# else:
#     print(angka,"adalah bialangan negative") 

# Studi Kasus : Penjualan Tiket

pembeli = input("masukan nama pembeli : ")
nomer_hp = input("masukan nomer hp : ")
jurusan = input("masukan kode jurusan [SBY/BL/LMP] : ").upper()
jumlah_beli = int(input("masukan jemulah tiket yg di beli :"))
uang_masuk = int(input("uang masuk :"))
nama_kota = ""
harga_jurusan = 0
if jurusan == "SBY":
    harga_jurusan = 300000
    nama_kota = "Surabaya"
elif jurusan == "BL":
    harga_jurusan = 350000
    nama_kota = "Bali"
elif jurusan == "LMP":
    nama_kota = "lampung"
    harga_jurusan = 500000
else:
    print("juruan tidak ada")
    exit()

diskon = 0
if jumlah_beli >=3:
    diskon = 0.1 * (jumlah_beli * harga_jurusan)  

total = (jumlah_beli * harga_jurusan) - diskon
if total > uang_masuk:
    print("uang tidak cukup")
    exit()
 
uang_kembali = uang_masuk - total 
print("""
=======================================
        PENJUALAN TIKET BUS
                XYZ
======================================= 
""")
print("nama        : ",pembeli)
print("NO Handphone: ", nomer_hp)
print("kode Jurusan: ", jurusan)
print("Nama Kota   : ", nama_kota)
print("harga       : ", harga_jurusan)
print("jumlah beli : ", jumlah_beli)
print("=======================================")
print("potongan    : ", diskon)
print("Total Bayar : ", total)
print("uang masuk  : ", uang_masuk)
print("uang kembali: ", uang_kembali)
print("=======================================")
     
     



    


