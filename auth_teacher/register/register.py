import json
import index

TEACHER_FILE = "auth_teacher/data_guru.json"

#Memuat data dari file dataguru.json
def load_data():
    try:
        with open(TEACHER_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File {TEACHER_FILE} tidak ditemukan.")
        return None
#try dan except digunakan supaya program tetap berjalan meskipun ada masalah seperti database belum dibuat atau rusak

#Menyimpan data ke file json
def save_database(data):
    try:
        with open(TEACHER_FILE, "w") as file: #Membuka file dataguru.json untuk write mode
            json.dump(data, file, indent=4) #Untuk menulis data ke file dalam format json
    except FileNotFoundError:
        print(f"File {TEACHER_FILE} tidak ditemukan.")
        return None

def is_valid_name(name):
    # Periksa setiap karakter dalam nama
    for char in name:
        if not (char.isalpha() or char.isspace()):  # Hanya huruf dan spasi yang diizinkan
            return False
    return True

def is_valid_email(email):
    # Karakter yang diizinkan dalam email
    allowed_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@._-"
    
    # Periksa setiap karakter dalam email
    for char in email:
        if char not in allowed_chars:  # Jika karakter tidak diizinkan
            return False
    
    # Pastikan email mengandung '@' dan '.' serta formatnya benar
    if "@" not in email or "." not in email:
        return False
    
    # Pastikan simbol tidak di awal atau akhir
    if email.startswith("@") or email.endswith("@"):
        return False
    if email.startswith(".") or email.endswith("."):
        return False
    if email.startswith("-") or email.endswith("-"):
        return False
    if email.startswith("_") or email.endswith("_"):
        return False
    
    return True

#Input untuk registrasi akun pengguna baru
def register_teacher():
    print("Registrasi")
    # Validasi nama
    while True:
        nama = input("Masukkan nama: ").strip()
        if nama and is_valid_name(nama):
            break
        print("Nama tidak valid. Silakan coba lagi.\n")
    
    guru = load_data() #Variabel guru berisi data dari file dataguru.json
    existing_emails = [guru["email"] for guru in guru]

    # Validasi email
    while True:
        email = input("Masukkan email: ")
        if email and is_valid_email(email):
            if email in existing_emails:
                print("Email sudah terdaftar. Silahkan gunakan Email lain.\n")
            else: 
                break
        else:
            print("Email tidak valid. Silahkan coba lagi.\n")

    # Validasi password
    while True:
        password = input("Masukkan password: ").strip()
        if password:
            break
        print("Password tidak boleh kosong. Silakan coba lagi.\n")

    new_guru = {
        "name": nama,
        "email": email,
        "password": password 
    }

    guru.append(new_guru)
    save_database(guru)
    print("Registrasi berhasil!\n")
    return