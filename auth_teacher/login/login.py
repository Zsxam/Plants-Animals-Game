def login_teacher():

    print("Silahkan Login")

    username_terdaftar = "Daspro2024"
    password_terdaftar = "Latihan"
    kesempatan = 5

    while kesempatan > 0:
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        if username == username_terdaftar and password == password_terdaftar:
            print("Login berhasil!")
            return username

        elif username == username_terdaftar:
            print(f"Password salah, kesempatan tersisa: {kesempatan-1}")
        elif password == password_terdaftar:
            print(f"Username salah, kesempatan tersisa: {kesempatan-1}")
        else:
            print(f"Username dan password salah, kesempatan tersisa: {kesempatan-1}")

        kesempatan -= 1

    print("Anda telah keluar dari sistem login")