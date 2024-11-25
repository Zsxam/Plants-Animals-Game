pengguna_login = True

print("Menu Logout")
if pengguna_login:
    pilih = input("Apakah anda ingin logout? (ya/tidak): ").strip().lower()
    if pilih == "ya":
        pengguna_login = False
        print("Logout berhasil!")
    elif pilih == "tidak":
        print("Logout dibatalkan.")
    else:
        print("Tidak Valid. Silahkan pilih ya/tidak.")