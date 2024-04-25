# tugas tanggal 2024-04-20
print("PROGRAM HITUNG GAJIH KARYAWAN")
nama = input("masukan nama :")
jabatan = int(input("masukan jabatan :"))
pendidikan = input("masukan pendidikan :").upper()
jam_kerja = int(input("masukan jam Kerja :"))
gaji_pokok = 300000
tjn_jabatan = 0
tjn_pendidikan = 0
honor_Lembur = 0
if jabatan == 1:
    tjn_jabatan = 0.05 * gaji_pokok
elif jabatan == 2:
    tjn_jabatan = 0.10 * gaji_pokok
elif jabatan == 3:
    tjn_jabatan = 0.15 * gaji_pokok
else:
    print("Golongan jabatan tidak ada")
    exit()

if pendidikan == "SMA":
    tjn_pendidikan = 0.025 * gaji_pokok
elif pendidikan == "D1":
    tjn_pendidikan = 0.5 * gaji_pokok
elif pendidikan == "D3":
    tjn_pendidikan = 0.20 * gaji_pokok
elif pendidikan == "S1":
    tjn_pendidikan = 0.30 * gaji_pokok
else:
    print("pendidikan tidak ada")
    exit()

if jam_kerja > 8:
    honor_Lembur = (jam_kerja -8) * 3500
else:
    honor_Lembur = 0

total = gaji_pokok + tjn_pendidikan + tjn_jabatan +honor_Lembur

print("==============================")
print("Karyawan yang bernama    :", nama)
print("Honor yang di terima")
print(" Tunjangan jabatan       :", tjn_jabatan)
print(" Tunjangan Pendidikan    :", tjn_pendidikan)
print(" Honor Lembur            :", honor_Lembur)
print("                         -----------------+")
print("                         ", total )
print("==============================")
print("Total Gajih")
print(total)