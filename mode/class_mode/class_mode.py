import json
import os
import game_core.game_kelas as game_kelas
import index

KELAS_FILE = "mode/class_mode/kelas.json"

def load_data(filename):
    with open(filename, "r") as f:
        return json.load(f)

def save_data(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
        
def class_mode():
    data = load_data(KELAS_FILE)
    class_code = input("Masukkan kode kelas: ")
    kelas_list = data.get("classes", [])
    found_class = None

    # Cari kelas berdasarkan kode
    for k in kelas_list:
        if k.get("class_code") == class_code:
            found_class = k  # Simpan dictionary kelas yang sesuai
            break

    # Jika kelas ditemukan
    if found_class:
        print(f"Selamat datang di kelas: {found_class['class_name']}")
        name = input("Masukkan Nama: ")
        subject = found_class["subject"]
        print(f"Subjek kelas ini adalah: {subject}\n")

        # Siswa langsung memecahkan telur berdasarkan subjek kelas
        cracked_subjects = game_kelas.crack_eggs(subject, name, class_code)
        if cracked_subjects:
            game_kelas.quiz(cracked_subjects, name, class_code)
        else:
            print("Tidak ada subjek yang dapat dipelajari. Kembali ke menu utama.\n")
    else:
        print("Kode kelas tidak ditemukan!\n")

