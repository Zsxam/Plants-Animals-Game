pengguna_login = True

print("Menu Logout")
if pengguna_login:
    pilih = input("Apakah anda ingin logout? (ya/tidak): ").lower()
    if pilih == "ya":
        pengguna_login = False
        print("Logout berhasil!")
    else:
        print("Logout dibatalkan.")