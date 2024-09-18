# cuaca = "cerah"

# if cuaca == "cerah":
#     print("bisa keluar rumah")
# else :
#     print("diam dirumah saja")


# Umur = int(input("Masukkan umur Anda : "))

# # if Umur > 0 :
# if Umur <= 10:
#         print( "Umur Anda termasuk kategori anak-anak")
# elif Umur <= 18:
#         print( "Umur Anda termasuk kategori remaja")
# elif Umur <=35:
#         print("Umur Anda termasuk kategori dewasa")
# elif Umur <=65:
#         print("Umur Anda termasuk kategori paruh baya")
# else:
#         print("Umur Anda termasuk kategori Tua")
    
# else:
#     print ("input usia harus bilangan positif")

# nim = int(input("masukkan nim :"))

# if nim >= 1 and nim <= 50 :
#     if nim >=1 and nim <= 25:
#         print("kelas a1")
#     else : 
#         print("kelas a2")

# elif nim >= 51 and nim <= 100:
#     if nim >= 51 and nim <= 75:
#         print("kelas b1")
#     else :
#         print("kelas b2")
        
# elif nim >= 101 and nim <= 120:
#     if nim >= 101 and nim <= 110:
#         print("kelas c1")
#     else :
#         print("kelas c2")

# else :
#     print("anda bukan mahasiswa")

# angka = int(input("Masukkan angka: "))
# result = "Genap" if angka % 2 == 0 else "Ganjil"
# print(angka, "adalah angka",result)

# nim = int(input("Masukkan Nim : "))
# hasil = "kelas a" if nim >= 1 and nim <= 50 else "kelas b" if nim >=51 and nim <= 100 else "kelas c" if nim >= 101 and nim <= 120 else "mahasiswa siluman"
# print(hasil)

membeli_buku = int(input("Mau membeli berapa buku?"))
buku = 25000

harga_buku = membeli_buku * buku
print(f"Harga Buku {harga_buku}")