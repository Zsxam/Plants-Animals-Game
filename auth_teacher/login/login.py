import os
import json
# File yang berisi data guru
TEACHER_FILE = "auth_teacher/data_guru.json"

def load_data(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def login_teacher():
    os.system('cls')
    data_guru = load_data(TEACHER_FILE)
    if len(data_guru) == 0:
        print("Data guru tidak tersedia, Register terlebih dahulu")
        return
    print("Silahkan Login")
    kesempatan = 5

    while kesempatan > 0:
        email = input("\nMasukkan Email: ")
        password = input("Masukkan Password: ")

        for guru in data_guru:
            if guru["email"] == email and guru["password"] == password:
                os.system('cls')
                return email

        kesempatan -= 1
        print(f"\nEmail atau password salah, kesempatan tersisa: {kesempatan}")

    print("Anda telah keluar dari sistem login\n")
    return