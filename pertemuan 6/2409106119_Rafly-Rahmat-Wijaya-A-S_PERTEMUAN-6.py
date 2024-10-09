# daftar_buku = {
# "Buku1" : "Harry Potter",
# "Buku2" : "Percy Jackson",
# "Buku3" : "Twillight"
# }
# print(daftar_buku["Buku1"])
# print(daftar_buku["Buku2"])
# print(daftar_buku["Buku3"])
# print(daftar_buku) #print key dan value

# Biodata = {
#     "Nama" : "Aldy Ramadhan Syahputra",
#     "NIM" : 2109106079,
#     "KRS" : ["Program Web", "Struktur Data", "Basis Data"],
#     "Mahasiswa_Aktif" :True,
#     "Social Media" : {
#         "Instagram" : "@aldyrmdhns_",
#         "Discord" : "\'Izanami#6848"
#     }
# }
# print(Biodata['Nama'])
# print(Biodata["Social Media"]["Instagram"])

# games = dict(section = "mobile legend", pokemon = "adventure", pubg = {"nama" : "rafly"})
# # print(games["pokemon"])
# # print(games['pubg'] ["nama"])
# print(games["pokemon"])

# Games = {
#     "Game1" : "Ml",
#     "Game2" : "Pubg",
#     "Game3" : {
#         "nama" : "rafly"
#         }
# }

# print(Games.get('Game1'))
# print((Games.get('Game3').get('nama'))) #manggil


# Nilai = {
#     "Matematika" : 80,
#     "B. Indonesia" : 90,
#     "B. Inggris" : 81,
#     "Kimia" : 78,
#     "Fisika" : 80
# }

# #tanpa menggunakan items
# for i in Nilai:
#     print(i)
#     print("")
# #menggunakan items
# for i, j in Nilai.items():
#     print(f"Nilai {i} anda adalah {j}")

#menambahkan 
# Film = {
#     "Avenger Endgame" : "Action",
#     "Sherlock Holmes" : "Mystery",
#     "The Conjuring" : "Horror"
# }
# #Sebelum Ditambah
# print(Film)

# Film["Zombieland"] = "Comedy" # metode 1 menambahkan dengan kurung siku
# Film.update({"Hours" : "Thriller", "Hajime no ippo" : "Action"}) # metode 2 menambahkan dengan update,bisa menambahkan langusng banyak
# #Setelah Ditambah

# # del Film['Avenger Endgame']
# # print(Film)

# # simpan = Film.pop('Avenger Endgame')
# # # print(Film)
# # # print(simpan)
# # Film['Avenger Endgame'] = simpan
# # print(Film)

# print("Jumlah Data = ", len(Film))

# Buku = {
# "No Longer Human" : "Osamu Dazai",
# "Harry Potter" : "J.K. Rowlings",
# "Hamlet" : "William Shakespeare"
# }
# pinjam = Buku.copy()
# print(Buku)
# print(pinjam)

# key = "apel","jeruk","mangga"
# value = 4

# buah = dict.fromkeys(key, value)
# print(buah)

# Nilai = {
#     "Matematika" : 80,
#     "B. Indonesia" : 90,
#     "B. Inggris" : 81
# }
# #sebelum Setdefault
# print(Nilai)
# print("")
# #menggunakan setdefault
# print("Nilai kimia: ", Nilai.setdefault("Kimia", 70))
# print("")
# #setelah menggunakan setdefault
# print(Nilai)

# Musik = {
#     "The Chainsmoker" : ["All we Know", "TheParis"],
#     "Alan Walker" : ["Alone", "Lily"],
#     "Neffex" : ["Best of Me", "Memories"]
# }
# for penyanyi, lagu in Musik.items():
#     print(f"Musik milik {penyanyi} adalah : ")
#     for song in lagu:
#         print(song)
# print("")

# mahasiswa = {
#     101 : {"Nama" : "Aldy", "Umur" : 19},
#     111 : {"Nama" : "Abdul", "Umur" : 18}
# }
# for key, value in mahasiswa.items():
#     print("ID Mahasiswa : ", key)
#     for key_a, value_a in value.items():
#         print (key_a, " : ", value_a)
# print("")

angkatan = {
    "nama" : "rafly",
    "umur" : "19",
    "nim" : "119",
    "jurusan" : "informatika",
    "angkatan" : "24"
}

angkatan["fakultas"] = input("fakultas:")
print(angkatan)
ubah = input("ubah key:")
angkatan[ubah] = input("value baru:")
print(angkatan)
hapus = input("hapus value:")
del angkatan[hapus]
print(angkatan)

# nilai = {
#     "math" : "rafly",
#     "fisika" : "19",
#     "biologi" : "119",
#     "kimia" : "informatika",
#     "angkatan" : "24"
# }