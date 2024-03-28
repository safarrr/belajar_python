'''
Nim         : 19235176
Nama        : Safarudin
Kelas       : 19.1A.24
'''
# buat perhitungan
# luas segiempat, luas segitiga,luas lingkaran
# Luas Segiempat
print("========== Luas Segiempat ==========")
segiempat_panjang = int(input("masukan Panjang  :"))
segiempat_lebar = int(input("masukan Lebar  :"))
luas_segiempat = segiempat_lebar * segiempat_panjang
print(f"Panjang segiempat   : {segiempat_panjang}")
print(f"Lebar segiempat     : {segiempat_lebar}")
print(f"Luas segiempat      : {luas_segiempat}")
print("====================================")

# Luas Segiempat
print("========== Luas Segitiga ==========")
segitiga_alas = int(input("masukan alas  :"))
segitiga_tinggi = int(input("masukan tinggi  :"))
luas_segitiga = 0.5 * segitiga_alas * segitiga_alas
print(f"Alas segitiga       : {segitiga_alas}")
print(f"Tinggi segiempat    : {segitiga_tinggi}")
print(f"Luas segitiga       : {luas_segitiga}")
print("===================================")


# Luas Lingkaran
print("========== Luas Lingkaran ==========")
lingkaran_jari_jari = int(input("masukan jari jari  :"))
luas_lingkaran = 3.14 * lingkaran_jari_jari **2
print(f"jari jari lingkaran       : {lingkaran_jari_jari}") 
print(f"Luas lingkaran       : {luas_lingkaran}")
print("====================================") 