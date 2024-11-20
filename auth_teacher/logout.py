def teacher_logout():
    print("Menu Logout")
    pilih = input("Apakah anda ingin logout? (ya/tidak): ").lower()
    if pilih == "ya":
        teacher_profile = False
        print("Logout berhasil!")
    elif pilih == "tidak":
        print("Logout dibatalkan.")
    else:
        print("Tidak Valid. Silahkan pilih ya/tidak.")