import json
import uuid
import os
import game_core.game as game
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
    kelas = data.get("classes", [])
    found_class = None

    for k in kelas:
        found_class = k["class_code"]
        if found_class:
            break

    if found_class:
        print(f"Selamat datang di kelas: {kelas['class_name']}")
        subject = kelas["subject"]
        print(f"Subjek kelas ini adalah: {subject}")

        # Siswa langsung memecahkan telur berdasarkan subjek kelas
        game.crack_eggs(subject)
    else:
        print("Kode kelas tidak ditemukan!")
