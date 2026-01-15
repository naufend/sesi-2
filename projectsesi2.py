# aplikasi gunting batu kertas

import random

bgk = ["batu", "gunting", "kertas"]

player = input("Pilih salah satu dari batu, gunting, atau kertas: ").lower()

if not (player == "batu" or player == "gunting" or player == "kertas"):
    print("Pilihan apa itu? TIDAK TERSEDIA!!!!!")
else:
    com = random.choice(bgk)

    print(f"Kamu memilih: {player}")
    print(f"Komputer memilih: {com}")

    # Menentukan pemenang
    if player == com:
        print("Seri!")
    elif (
        (player == "batu" and com == "gunting") or
        (player == "gunting" and com == "kertas") or
        (player == "kertas" and com == "batu")
    ):
        print("YEAYY!!! Kamu menang!")
    else:
        print("HADUH, Kamu kalah!")
