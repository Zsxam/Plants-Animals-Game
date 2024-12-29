import json
import index

TEACHER_FILE = "auth_teacher/data_guru.json"

#Memuat data dari file dataguru.json
def load_data():
    with open(TEACHER_FILE, "r") as f:
        return json.load(f)
#try dan except digunakan supaya program tetap berjalan meskipun ada masalah seperti database belum dibuat atau rusak

#Menyimpan data ke file json
def save_database(data):
    with open(TEACHER_FILE, "w") as file: #Membuka file dataguru.json untuk write mode
        json.dump(data, file, indent=4) #Untuk menulis data ke file dalam format json

#Input untuk registrasi akun pengguna baru
def register_teacher():
    print("Registrasi")
    nama = input("Masukkan nama: ")
    email = input("Masukkan email: ")
    password = input("Masukkan password: ")

    users = load_data() #Variabel users berisi data dari file dataguru.json

#Untuk menghindari username yang sama
    if email in users:
        print("Email sudah terdaftar. Silahkan gunakan Email lain.")
        return


    new_users = {
        "name": nama,
        "email": email,
        "password": password 
    }

    users.append(new_users)
    save_database(users)
    print("Registrasi berhasil!")
    index.main()