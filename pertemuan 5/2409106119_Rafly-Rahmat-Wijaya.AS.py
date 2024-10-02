akuns = []

while True:
    print("halo")
    print("halo")
    print("daftar")
    print("login")
    print("exit")
    print("-----")
    opsi = input("pilih opsi")
    print(" ")

    if opsi == "1":
        print("halo pengguna baru")
        Username = input('username')
        akuna = False
        for akun in akuns:
            if akun[0] == Username: #memeriksa apakah username sduah ada
                akuna = True 
                break
            if akuna:
                print("nama sudah terpakai")
            else:
                Password = input("password")
                akuns.append([Username,Password, []])#simpan usr pw catatan sebagai list kkosong
                print(f"akun anda berhasil terdaftar dengan id: {Username}")
            
# list 
# nama = ["shandy",106,True,3.96]
# print(nama[2])

# nested list
# nama = ["shandy",106,True,3.96[123,"Rafly",False]]
# print(nama[3][2])

# list kebawah
# matkul = ["shandy",
#           "APL",
#           'WEB',
#           'APD',
#           'JARKOM',
#           'STRUKDAT',
#           'BASDAT'
# ]
# print(matkul[2])

# append 
# makanan = ['baskso','sate','gulai']
# print("sebelum ")
# print(makanan)

# append menambahkan langsung di ujung
# makanan = ['baskso','sate','gulai']
# print("sesudah")
# print.append('nasi goreng')

# insert supaya bisa taro data sesuai keinginan
# makanan.insert(1,"nasi goreng")
# print(makanan)

# mengubah  data
# makanan[0] = ["ayam",123]
# print(makanan)

# menghapus data
# del makanan[1:]
# print(makanan)

# pop / memindahkan data ke variabel baru
# data = makanan.pop(2)
# print(makanan)
# print(data)

# makanan.clear()
# print(makanan)

# studi kasus
# minuman = ["matcha","coklat","apel",'josu','esteh','greentea']
# # print sebelum
# print('sebelum')
# print(minuman)
# # proses
# del minuman [2]
# minuman.insert(0,"jus tomat")
# minuman[5] = "air putih"
# # hasil
# print('sesudah')
# print(minuman)

# memanggil tanpa menggunakan kurung siku []
# makanan = ['bakso','ikan','mie ayam',]

# for i in makanan:
#     print(i, end=" ")

# nested 
makanan = ["ayam","bakso",["bakso","ikan","mie ayam",],["teh","air","kopi"]]

for i in makanan:
    if isinstance(i, list):
        for j in i:
            print(j)
    else:
        print(i)
