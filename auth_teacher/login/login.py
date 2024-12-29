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

    data_guru = load_data(TEACHER_FILE)
    if len(data_guru) == 0:
        print("Data guru tidak tersedia.")
        return
    os.system('cls')
    print("Silahkan Login")
    kesempatan = 5

    while kesempatan > 0:
        email = input("Masukkan Email: ")
        password = input("Masukkan Password: ")

        for guru in data_guru:
            if guru["email"] == email and guru["password"] == password:
                os.system('cls')
                nama = next((guru['name'] for guru in data_guru if guru['email'] == email), None)
                print(f"Selamat datang, {nama}!")
                return email
            elif guru["email"] == email:
                print(f"\nPassword salah, kesempatan tersisa: {kesempatan-1}")
            elif guru["password"] == password:
                print(f"\nEmail salah, kesempatan tersisa: {kesempatan-1}")
            else:
                print(f"\nEmail dan password salah, kesempatan tersisa: {kesempatan-1}")

        kesempatan -= 1

    print("Anda telah keluar dari sistem login")