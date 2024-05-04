
print("GEROBAK FRIED CHICKEN")
print("="*80)
print("kode     jenis Potong        harga")
print("D        Dada                Rp.2500")
print("P        Paha                Rp.2000")
print("s        Sayap               Rp.1500")
print("="*80)
data_kode = []
data_banyak_beli = []
banyak_jenis = int(input("Banyak Input      :"))

for i  in range(banyak_jenis):
    print("Jenis ke  :" ,i+1)
    kode_potong = input("Kode potong [D/P/S]: ").upper()
    banyak_potong = int(input("Banyak Potong: "))
    data_kode.append(kode_potong)
    data_banyak_beli.append(banyak_potong)
    print("="*80)
    

print("GEROBAK FRIED CHICKEN")
print("="*80)
print("no   jenis Potong    harga Satuan    Banyak Beli     Jumlah  Harga")
print("="*80)   
total_bayar = 0
for i in range(banyak_jenis):
    harga_satuan = 0 
    nama_potongan = ""
    if data_kode[i]== "D":
        nama_potongan = "Dada"
        harga_satuan = 2500
    elif data_kode[i]== "P":
         nama_potongan = "Paha"
         harga_satuan = 2000
    elif data_kode[i]== "S":
         nama_potongan = "Sayap"
         harga_satuan = 1500
    else: 
        print("kode tidak di temukan")

    jumlah_harga = harga_satuan * data_banyak_beli[i] 
    total_bayar += jumlah_harga
    print(f"{i+1}   {nama_potongan}             {harga_satuan}              {data_banyak_beli[i]}             {jumlah_harga}")


pajak = int( 0.10 * total_bayar) 
print(" "* 52, "Jumlah Bayar Rp.", total_bayar)
print(" "* 52, "Pajak 10% Rp.", pajak)
print(" "* 52, "Total Bayar Rp.", total_bayar +pajak)
print("="*80)   
