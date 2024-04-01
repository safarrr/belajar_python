# NIM     : 19235176
# Nama    : Safarudin
# Kelas   : 19.1A.24
# Sistem informasi

b1 = 60
b2 = 20
b3 = 100
b4 = 40

max = b1
bil_terbesar = "b1"
if b2 > max:
    max= b2
    bil_terbesar = "b2"

if b3 > max:
    max =b3
    bil_terbesar = "b3"
if b4 > max:
    max = b4
    bil_terbesar = "b4"

print("bilangan terbesar adalah {} dangan jumlah: {}".format(bil_terbesar,max))
