import json
import uuid
import os
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
def create_class(teacher_profile):
    # Muat data guru
    data_guru = load_data(TEACHER_FILE)

    # Pastikan data guru adalah list
    if not isinstance(data_guru, list):
        print("Data guru tidak valid.")
        index.main()

    # Periksa apakah email guru ditemukan dalam data
    teacher_found = any(guru.get("email") == teacher_profile for guru in data_guru if "email" in guru)
    if not teacher_found:
        print(f"Guru dengan email '{teacher_profile}' tidak ditemukan.")
        index.main()

    # Lanjutkan pembuatan kelas
    data_kelas = load_data(KELAS_FILE)

    if "classes" not in data_kelas:
        data_kelas["classes"] = []

    class_name = input("Masukkan nama kelas: ")
    class_code = str(uuid.uuid4())[:6]
    subject = input("Masukkan jenis subjek (Plants/Animals): ")

    new_class = {
        "teacher": teacher_profile,
        "class_name": class_name,
        "subject": subject,
        "class_code": class_code,
        "students_scores": {}
    }

    data_kelas["classes"].append(new_class)
    save_data(data_kelas, KELAS_FILE)
    print(f"Kelas '{class_name}' berhasil dibuat dengan kode: {class_code} !")

    # Kembali ke menu guru setelah menambah kelas
    print(" ")
    teacher_menu(teacher_profile)  # Panggil kembali menu guru

def edit_class(teacher_profile, class_code):
    # Muat data kelas
    data_kelas = load_data(KELAS_FILE) 
    kelas_found = False  # Flag untuk mengecek apakah kelas ditemukan

    # Cari kelas berdasarkan kode
    for kelas in data_kelas.get("classes", []):
        if kelas.get("class_code") == class_code and kelas.get("teacher") == teacher_profile:
            kelas_found = True  # Tandai bahwa kelas ditemukan
            print(f"Data Kelas {class_code}: ")
            print(f"- Nama Kelas: {kelas['class_name']}, Subjek: {kelas['subject']}, Guru: {kelas['teacher']}")
            print(" ")

            new_class_name = input("Masukkan nama kelas yang baru: ")
            new_subject = input("Masukkan subjek baru (Plants/Animals): ")
            if new_subject.lower() not in ["plants", "animals"]:
                print("Masukkan subjek yang valid!")
                return

            valid = input("Apakah anda yakin dengan perubahan ini? (ya/tidak): ")
            if valid.lower() == "ya":
                # Update data kelas
                kelas["class_name"] = new_class_name
                kelas["subject"] = new_subject.capitalize()
                save_data(data_kelas, KELAS_FILE)
                print("Kelas berhasil diperbarui.")
            else:
                print("Perubahan dibatalkan.")
            return  # Kembali setelah mengedit kelas

    if not kelas_found:
        print("Kelas tidak ditemukan atau Anda tidak memiliki akses untuk mengedit kelas ini.")

def delete_class(teacher_profile, class_code):
    # Muat data kelas
    data_kelas = load_data(KELAS_FILE)

    # Filter kelas yang tidak sesuai dengan kode kelas dan teacher_profile
    updated_data_kelas = [kelas for kelas in data_kelas["classes"] if not (kelas["teacher"] == teacher_profile and kelas["class_code"] == class_code)]

    if len(data_kelas["classes"]) == len(updated_data_kelas):
        print("Kelas tidak ditemukan atau Anda tidak memiliki akses untuk menghapus kelas ini.")
    else:
        save_data({"classes": updated_data_kelas}, KELAS_FILE)
        print("Kelas berhasil dihapus.")
    # Kembali ke menu guru setelah menghapus kelas
    return

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
    print("\nMenu Melihat Skor")
    print("1. Melihat Skor")
    print("2. Kembali")
    lihat_skor = input("Pilih menu (1-2): ")
    if lihat_skor == "1":
        class_code = input("\nMasukkan kode kelas untuk melihat skor siswa: ")
        # Cari kelas berdasarkan kode
        for kelas in data_kelas.get("classes", []):
            if kelas.get("class_code") == class_code and kelas.get("teacher") == teacher_profile:
                print(f"\nSkor Siswa di Kelas '{kelas['class_name']}':")
                if kelas.get("students_scores"):
                    for student, score in kelas["students_scores"].items():
                        print(f"- {student}: {score}")
                    print("")
                else:
                    print("Belum ada skor siswa yang terdaftar.")
                return

        print("Kelas tidak ditemukan atau Anda tidak memiliki akses untuk melihat skor siswa di kelas ini.")
    if lihat_skor == "2":
        return
    else: 
        print("Masukkan nomor menu yang benar.")

def teacher_menu(teacher_profile):
    data_guru = load_data(TEACHER_FILE)
    while True:
        nama = next((guru['name'] for guru in data_guru if guru['email'] == teacher_profile), None)
        print(f"Selamat datang, {nama}!")
        print("Halaman Guru")
        print("1. Tambah Kelas")
        print("2. Ubah Kelas")
        print("3. Hapus Kelas")
        print("4. Tampilkan Kelas")
        print("5. Logout")

        choice = input("Pilih opsi (1-5): ")
        if choice == "1":
            os.system('cls')
            create_class(teacher_profile)
        elif choice == "2":
            show_classes(teacher_profile)
            code = input("Masukkan kode kelas yang ingin diubah: ")
            edit_class(teacher_profile, code)
        elif choice == "3":
            show_classes(teacher_profile)
            code = input("Masukkan kode kelas yang ingin dihapus: ")
            delete_class(teacher_profile, code)
        elif choice == "4":
            show_classes(teacher_profile)
        elif choice == "5":
            os.system('cls')
            logout = lo.teacher_logout()
            if logout:
                return
        else:
            print("Pilihan tidak valid.\n")
