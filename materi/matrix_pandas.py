import pandas as pd

list_nim=[]
list_nama=[]
list_uts=[]
list_uas=[]
list_total=[]

ulang = 3

for i in range(ulang):
    print("data ke - ", i+1)
    list_nim.append(input("Nim: "))
    list_nama.append(input("nama: "))
    list_uts.append(int(input("niali uts: ")))
    list_uas.append(int(input("niali uas: ")))

for i in range(ulang):
    list_total.append((list_uas[i]+list_uts[i])/2)

tamu = {
    "Nim :": list_nim,
    "nama lengkap:": list_nama,
    "nilai uts:": list_uts,
    "nilai uas:": list_uas,
    "rata rata:": list_total,
}

data_tamu = pd.DataFrame(tamu)

print("="*5 +"daftar Nilai"+"="*5 )
print(data_tamu)
print("="*100 )