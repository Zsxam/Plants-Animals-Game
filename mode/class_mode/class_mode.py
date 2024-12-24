import json
import uuid
import os
import game_core.game as game

KELAS_FILE = "mode\class_mode\kelas.json"
TEACHER_FILE = "auth_teacher\data_guru.json"

def load_data(filename):
    
    with open(filename, "r") as f:
        return json.load(f)

def save_data(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

# Fungsi untuk membuat kelas
def create_class(teacher_email):
    # Muat data guru
    data_guru = load_data(TEACHER_FILE)

    # Pastikan data guru adalah list
    if not isinstance(data_guru, list):
        print("Data guru tidak valid.")
        return

    # Periksa apakah email guru ditemukan dalam data
    teacher_found = any(guru.get("Username") == teacher_email for guru in data_guru)
    if not teacher_found:
        print(f"Guru dengan email '{teacher_email}' tidak ditemukan.")
        return

    # Lanjutkan pembuatan kelas
    data_kelas = load_data(KELAS_FILE)

    if "classes" not in data_kelas:
        data_kelas["classes"] = []

    class_name = input("Masukkan nama kelas: ")
    class_code = str(uuid.uuid4())[:6]
    subject = input("Masukkan jenis subjek (Plants/Animals): ")

    new_class = {
        "teacher": teacher_email,
        "class_name": class_name,
        "subject": subject,
        "class_code": class_code,
        "students_scores": {}
    }

    data_kelas["classes"].append(new_class)
    save_data(data_kelas, KELAS_FILE)
    print(f"Kelas '{class_name}' berhasil dibuat dengan kode: {class_code} !")

def show_classes(teacher_profile):
    data_kelas = load_data(KELAS_FILE)

    # Periksa apakah ada kelas dalam data
    if not data_kelas.get("classes"):
        print("Belum ada kelas yang terdaftar.")
        return
    else:
        print("Kelas yang terdaftar:")

    # Iterasi melalui setiap kelas dalam data_kelas["classes"]
    for kelas in data_kelas.get("classes", []):
        # Cocokkan teacher_profile dengan "teacher" di setiap kelas
        if kelas.get("teacher") == teacher_profile:
            print(f"- Nama Kelas: {kelas['class_name']}, Subjek: {kelas['subject']}, Kode: {kelas['class_code']}")
        
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
