def load_data(filename):
    with open(filename, "r") as f:
        return json.load(f)

def register_teacher():
    data = load_data(DATA_FILE)
    teachers = data.get("teachers", {})
    
    name = input("Masukkan nama: ")
    email = input("Masukkan email: ")
    password = input("Masukkan password: ")

    if email in teachers:
        print("Email sudah terdaftar!")
        return
    
    teachers[email] = {
        "name": name,
        "password": password,
        "classes": {}
    }
    data["teachers"] = teachers
    save_data(data, DATA_FILE)
    print("Registrasi berhasil!")