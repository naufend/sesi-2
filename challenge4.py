jam = int(input("Masukkan Jam saat ini (0-23): "))

if jam < 12:
    print("Selamat Pagi!")
elif jam <= 17:
    print("Selamat Siang!")
else:
    print("Selamat Malam!")