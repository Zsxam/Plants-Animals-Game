import json

DB_FILE = "dataguru.json"

#Memuat data dari file dataguru.json
def load_database():
    try:
        with open(DB_FILE, "r") as file: #membuka file dalam mode read-only
            return json.load(file) # membaca isi file json dan mengubahnya menjadi objek python
    except FileNotFoundError: #apabila file tidak ada, akan dikembalikan ke dictionary kosong
        return {}  
    except json.JSONDecodeError: #Apabila file json yang rusak atau tidak valid isinya
        print("Database rusak. Membuat ulang database.")
        return {}
#try dan except digunakan supaya program tetap berjalan meskipun ada masalah seperti database belum dibuat atau rusak

#Menyimpan data ke file json
def save_database(data):
    with open(DB_FILE, "w") as file: #Membuka file dataguru.json untuk write mode
        json.dump(data, file, indent=4) #Untuk menulis data ke file dalam format json

#Input untuk registrasi akun pengguna baru
def register_teacher():
    print("Registrasi")
    username = input("Masukkan username: ")
    email = input("Masukkan email: ")
    password = input("Masukkan password: ")

    users = load_database() #Variabel users berisi data dari file dataguru.json

#Untuk menghindari username yang sama
    if username in users:
        print("Username sudah terdaftar. Silahkan buat username lain.")
        return


    users[username] = {
        "email": email,
        "password": password 
    }

    save_database(users)
    print("Registrasi berhasil!")

if __name__ == "__main__":
    register_teacher()

