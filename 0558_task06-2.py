import random

def main():
    print("Selamat datang di Permainan Tebak Angka!")
    print("Saya telah memilih sebuah angka antara 1 dan 100.")

    angka_rahasia = random.randint(1, 100)
    percobaan = 0

    while True:
        tebakan = input("Tebak angka (1-100): ")
        percobaan += 1

        if not tebakan.isdigit():
            print("Masukkan harus berupa angka. Coba lagi.")
            continue

        tebakan = int(tebakan)

        if tebakan < angka_rahasia:
            print("Angka terlalu kecil. Coba lagi.")
        elif tebakan > angka_rahasia:
            print("Angka terlalu besar. Coba lagi.")
        else:
            print(f"Selamat! Anda berhasil menebak angka {angka_rahasia} dalam {percobaan} percobaan.")
            break

    print("Terima kasih telah bermain!")

if __name__ == "__main__":
    main()
