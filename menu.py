import os
import sys
import time

# Definisi Warna (ANSI)
R = '\033[31m'  # Merah
G = '\033[32m'  # Hijau
Y = '\033[33m'  # Kuning
B = '\033[34m'  # Biru
P = '\033[35m'  # Ungu
C = '\033[36m'  # Cyan
W = '\033[37m'  # Putih
N = '\033[0m'   # Reset

# ===============================
# LOGIN
# ===============================
USERS = {
    "admin": "Loke5567",
    "loke": "securepass"
}

def clear():
    os.system('clear')

def header():
    clear()
    print(f"{C}==========================================")
    print(f"{Y}                Tools Menu         ")
    print(f"{C}==========================================")
    print(f"{W}            Author   : Loke At Me")
    print(f"{W}            Status   : {G}Active")
    print(f"{C}==========================================")
    print(f"{Y} Dengan adanya kalian berdonasi itu sangat ")
    print(f"{Y} Berarti Bagi Saya ")
    print(f"{R} [💲]Donasi : https://saweria.co/LokeAtMe/")
    print(f"{C}=========================================={N}")

def menu():
    header()
    print(f"{G}[1]{W} Jalankan Tools single Scanner")
    print(f"{G}[2]{W} Jalankan Tools Mass Scanner")
    print(f"{G}[3]{W} Jalankan Tools Malware Scanner V3.0")
    print(f"{G}[4]{W} Update Script")
    print(f"{R}[0]{W} Keluar")
    print(f"{C}------------------------------------------{N}")
    
    pilih = input(f"{Y}Pilih Menu > {N}")

    if pilih == '1':
        print(f"\n{B}[*] Membuka Tools Single Scanner...{N}")
        time.sleep(1)
        # Ganti dengan perintah menjalankan tool Anda
        os.system(" python steganographp.py") 
        input(f"\n{Y}Tekan Enter untuk ke Menu...{N}")
        menu()
        
    elif pilih == '2':
        print(f"\n{B}[*] Membuka Tool Mass Scanner...{N}")
        time.sleep(1)
        # Ganti dengan perintah menjalankan tool Anda
        os.system(" python mas.py")
        input(f"\n{Y}Tekan Enter untuk kembali...{N}")
        menu()

    elif pilih == '3':
        print(f"\n{B}[*] Membuka Tools Malware Scanner...{N}")
        time.sleep(1)
        # Ganti dengan perintah menjalankan tool Anda
        os.system(" python malwarescanner.py")
        input(f"\n{Y}Tekan Enter untuk kembali...{N}")
        menu()

    elif pilih == '4':
        print(f"\n{G}[+] Mengecek Update...{N}")
        os.system("https://github.com/CyberNews0/staganographpy")
        time.sleep(2)
        menu()

    elif pilih == '0':
        print(f"\n{R}Sampai Jumpa!{N}")
        sys.exit()

    else:
        print(f"\n{R}[!] Pilihan Salah!{N}")
        time.sleep(1)
        menu()

if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print(f"\n{R}Dibatalkan oleh pengguna.{N}")
        sys.exit()
