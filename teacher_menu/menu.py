import json
import uuid
import os
import auth_teacher.logout.logout as lo
import index

KELAS_FILE = "mode/class_mode/kelas.json"
TEACHER_FILE = "auth_teacher/data_guru.json"

def load_data(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File {filename} tidak ditemukan")
        return None

def save_data(data, filename):
    try:
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
    except FileNotFoundError:
        print(f"File {filename} tidak ditemukan")
        return None

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
    while True:
        subject = input("Masukkan jenis subjek (Plants/Animals): ").capitalize()
        if subject in ["Plants", "Animals"]:
            break
        else:
            print("Subjek harus 'Plants' atau 'Animals'. Silahkan coba lagi\n")

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
    return 

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
            while True:
                new_subject = input("Masukkan jenis subjek (Plants/Animals): ").capitalize()
                if new_subject in ["Plants", "Animals"]:
                    break
                else:
                    print("Subjek harus 'Plants' atau 'Animals'. Silahkan coba lagi\n")

            while True:
                valid = input("\nApakah anda yakin dengan perubahan ini? (ya/tidak): ")
                if valid.lower() == "ya":
                    # Update data kelas
                    kelas["class_name"] = new_class_name
                    kelas["subject"] = new_subject
                    save_data(data_kelas, KELAS_FILE)
                    print("Kelas berhasil diperbarui.\n")
                    break
                elif valid.lower() == "tidak":
                    print("Perubahan dibatalkan.\n")
                    break
                else:
                    print("Masukkan jawaban yang valid.")
            return  # Kembali setelah mengedit kelas

    if not kelas_found:
        print("Kelas tidak ditemukan atau Anda tidak memiliki akses untuk mengedit kelas ini.\n")

def delete_class(teacher_profile, class_code):
    # Muat data kelas
    data_kelas = load_data(KELAS_FILE)

    # Filter kelas yang tidak sesuai dengan kode kelas dan teacher_profile
    updated_data_kelas = [kelas for kelas in data_kelas["classes"] if not (kelas["teacher"] == teacher_profile and kelas["class_code"] == class_code)]

    if len(data_kelas["classes"]) == len(updated_data_kelas):
        print("Kelas tidak ditemukan atau Anda tidak memiliki akses untuk menghapus kelas ini.\n")
    else:
        while True:
            valid = input("\nApakah anda yakin ingin menghapus kelas ini? (ya/tidak): ")
            if valid.lower() == "ya":
                save_data({"classes": updated_data_kelas}, KELAS_FILE)
                print("Kelas berhasil dihapus.\n")
                break
            elif valid.lower() == "tidak":
                print("Menghapus kelas dibatalkan.\n")
                break
            else:
                print("Masukkan jawaban yang valid.")
    # Kembali ke menu guru setelah menghapus kelas
    return

def show_classes(teacher_profile):
    data_kelas = load_data(KELAS_FILE)

    # Periksa apakah ada kelas dalam data
    if not data_kelas.get("classes"):
        print("\nBelum ada kelas yang terdaftar.\n")
        return False
    
    cek_kelas = [kelas for kelas in data_kelas.get("classes", []) if kelas.get("teacher") == teacher_profile]

    if not cek_kelas:
        print("\nAnda belum memiliki kelas.\n")
        return False

    print("Kelas yang terdaftar:")
    # Iterasi melalui setiap kelas dalam data_kelas["classes"]
    for kelas in data_kelas.get("classes", []):
        # Cocokkan teacher_profile dengan "teacher" di setiap kelas
        if kelas.get("teacher") == teacher_profile:
            print(f"- Nama Kelas: {kelas['class_name']}, Subjek: {kelas['subject']}, Kode: {kelas['class_code']}")
    print("")
    return True
    
def lihat_skor(teacher_profile):
    data_kelas = load_data(KELAS_FILE)

    print("Menu Melihat Skor")
    print("1. Melihat Skor")
    print("2. Kembali")
    while True:
        lihat_skor = input("Pilih menu (1-2): ")
        if lihat_skor == "1":
            class_code = input("\nMasukkan kode kelas untuk melihat skor siswa: ")
            # Cari kelas berdasarkan kode
            for kelas in data_kelas.get("classes", []):
                if kelas.get("class_code") == class_code and kelas.get("teacher") == teacher_profile:
                    print(f"\nSkor Siswa di Kelas '{kelas['class_name']}':")
                    if kelas.get("students_scores"):
                        # Ambil data skor siswa dan urutkan dari yang terbesar ke terkecil
                        sorted_scores = sorted(kelas["students_scores"].items(), key=lambda x: x[1], reverse=True)
                        # Tampilkan skor yang sudah diurutkan
                        for rank, (student, score) in enumerate(sorted_scores, start=1):
                            print(f"{rank}. {student}: {score}")
                        print("")
                    else:
                        print("Belum ada skor siswa yang terdaftar.\n")
                    return

            print("Kelas tidak ditemukan atau Anda tidak memiliki akses untuk melihat skor siswa di kelas ini.")
        if lihat_skor == "2":
            print("")
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
            lihat = show_classes(teacher_profile)
            if lihat:
                code = input("Masukkan kode kelas yang ingin diubah: ")
                edit_class(teacher_profile, code)
        elif choice == "3":
            lihat = show_classes(teacher_profile)
            if lihat:
                code = input("Masukkan kode kelas yang ingin dihapus: ")
                delete_class(teacher_profile, code)
        elif choice == "4":
            lihat = show_classes(teacher_profile)
            if lihat:
                lihat_skor(teacher_profile)
        elif choice == "5":
            os.system('cls')
            logout = lo.teacher_logout()
            if logout:
                return
        else:
            print("Pilihan tidak valid.\n")
