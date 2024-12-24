import json
import uuid
import os
import game_core.game as game
import auth_teacher.logout.logout as lo
import index

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
        index.main()

    # Periksa apakah email guru ditemukan dalam data
    teacher_found = any(guru.get("email") == teacher_email for guru in data_guru)
    if not teacher_found:
        print(f"Guru dengan email '{teacher_email}' tidak ditemukan.")
        index.main()

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

    print(" ")
    index.main(teacher_email)

def edit_class(teacher_email, class_code, new_class_name, new_subject):
    # Muat data kelas
    data_kelas = load_data(KELAS_FILE)

    # Cari kelas berdasarkan email guru dan kode kelas
    for kelas in data_kelas:
        if kelas["teacher_email"] == teacher_email and kelas["code"] == class_code:
            kelas["name"] = new_class_name
            kelas["subject"] = new_subject
            save_data(data_kelas, KELAS_FILE)
            print("Kelas berhasil diperbarui.")
            return

    print("Kelas tidak ditemukan atau Anda tidak memiliki akses untuk mengedit kelas ini.")

def delete_class(teacher_email, class_code):
    # Muat data kelas
    data_kelas = load_data(KELAS_FILE)

    # Filter kelas yang tidak sesuai dengan kode kelas dan teacher_email
    updated_data_kelas = [kelas for kelas in data_kelas if not (kelas["teacher"] == teacher_email and kelas["class_code"] == class_code)]

    if len(data_kelas) == len(updated_data_kelas):
        print("Kelas tidak ditemukan atau Anda tidak memiliki akses untuk menghapus kelas ini.")
    else:
        save_data(updated_data_kelas, KELAS_FILE)
        print("Kelas berhasil dihapus.")

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
    print(" ")

def teacher_menu(teacher_profile):
    while True:
        print("Menu Kelas")
        print("1. Tambah Kelas")
        print("2. Ubah Kelas")
        print("3. Hapus Kelas")
        print("4. Logout")
        print("5. Kembali")

        choice = input("Pilih opsi (1-4): ")
        if choice == "1":
            os.system('cls')
            create_class(teacher_profile)
        elif choice == "2":
            change_class(teacher_profile)
        elif choice == "3":
            delete_class(teacher_profile)
        elif choice == "4":
            os.system('cls')
            lo.teacher_logout()
        elif choice == "5":
            os.system('cls')
            return teacher_profile
        else:
            print("Pilihan tidak valid.")
