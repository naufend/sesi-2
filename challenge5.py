age =  int(input("Masukan Umur Kamu: "))
passed_test = str(input("Sudahkah lulus ujian tertulis?(True/False): "))

if age >= 17 and passed_test == True:
    print("Selamat, kamu sudah boleh punya SIM")
else:
    print("Maaf, Kamu belum bisa punya SIM")