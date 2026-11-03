
print("====================================")
print("       PROGRAM NILAI SISWA TKA")
print("====================================")

nama = input("Masukkan nama siswa: ")

# Memasukkan nilai setiap mata pelajaran
nilai_indonesia = int(input("Masukkan nilai TKA Bahasa Indonesia (200-800): "))
nilai_inggris = int(input("Masukkan nilai TKA Bahasa Inggris (200-800): "))
nilai_matematika = int(input("Masukkan nilai TKA Matematika (200-800): "))


def keterangan(nilai):

    if nilai < 200 or nilai > 800:
        return "NILAI TIDAK VALID"

    elif nilai >= 725:
        return "NILAI ISTIMEWA"

    elif nilai >= 600:
        return "SANGAT BAIK"

    elif nilai >= 500:
        return "MEMADAI"

    elif nilai >= 200:
        return "KURANG MEMADAI"


print("\n====================================")
print("          HASIL NILAI TKA")
print("====================================")

print("Nama Siswa :", nama)

print("------------------------------------")
print("Bahasa Indonesia :", nilai_indonesia)
print("Keterangan       :", keterangan(nilai_indonesia))

print("------------------------------------")
print("Bahasa Inggris   :", nilai_inggris)
print("Keterangan       :", keterangan(nilai_inggris))

print("------------------------------------")
print("Matematika       :", nilai_matematika)
print("Keterangan       :", keterangan(nilai_matematika))

print("====================================")

