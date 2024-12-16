import os
import json
# File yang berisi data guru
TEACHER_FILE = "auth_teacher\data_guru.json"

def load_data(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def login_teacher():

    data_guru = load_data(TEACHER_FILE)
    if len(data_guru) == 0:
        print("Data guru tidak tersedia.")
        return
    os.system('cls')
    print("Silahkan Login")
    kesempatan = 5

    while kesempatan > 0:
        username = input("Masukkan Username: ")
        password = input("Masukkan Password: ")

        for guru in data_guru:
            if guru["Username"] == username and guru["Password"] == password:
                os.system('cls')
                print(f"Selamat datang, {username}!")
                return username
            elif guru["Username"] == username:
                print(f"\nPassword salah, kesempatan tersisa: {kesempatan-1}")
            elif guru["Password"] == password:
                print(f"\nUsername salah, kesempatan tersisa: {kesempatan-1}")
            else:
                print(f"\nUsername dan password salah, kesempatan tersisa: {kesempatan-1}")

        kesempatan -= 1

    print("Anda telah keluar dari sistem login")