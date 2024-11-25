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

    print("Silahkan Login")
    kesempatan = 5

    while kesempatan > 0:
        username = input("Masukkan Username: ")
        password = input("Masukkan Password: ")

        for guru in data_guru:
            if guru["Username"] == username and guru["Password"] == password:
                print("Login berhasil")
                return
            elif guru["Username"] == username:
                print(f"Password salah, kesempatan tersisa: {kesempatan-1}")
                break
            elif guru["Password"] == password:
                print(f"Username salah, kesempatan tersisa: {kesempatan-1}")
            else:
                print(f"Username dan password salah, kesempatan tersisa: {kesempatan-1}")

        kesempatan -= 1

    print("Anda telah keluar dari sistem login")