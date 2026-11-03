
print("================================")
print("     TOKO PEMBELIAN BARANG")
print("================================")

nama = input("Masukkan nama pembeli: ")
barang = input("Masukkan nama barang: ")
harga = int(input("Masukkan harga barang: "))
jumlah = int(input("Masukkan jumlah barang: "))

total = harga * jumlah

if total >= 100000 and jumlah >= 2:
    diskon = 10
    print_diskon = "10%"

elif total >= 100000 or jumlah >= 5:
    diskon = 5
    print_diskon = "5%"

else:
    diskon = 0
    print_diskon = "Tidak ada"

potongan = total * diskon / 100
total_akhir = total - potongan

print("\n================================")
print("       STRUK PEMBELIAN")
print("================================")

print("Nama pembeli :", nama)
print("Nama barang  :", barang)
print("Harga barang : Rp", harga)
print("Jumlah       :", jumlah)
print("--------------------------------")
print("Total harga  : Rp", total)
print("Diskon       :", print_diskon)
print("Potongan     : Rp", int(potongan))
print("--------------------------------")
print("Total bayar  : Rp", int(total_akhir))

if not (total >= 100000):
    print("Keterangan   : Belanja di bawah Rp100.000")

print("================================")
