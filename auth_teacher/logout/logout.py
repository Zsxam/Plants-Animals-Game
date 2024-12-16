import index

def teacher_logout():
    print("Menu Logout")
    pilih = input("Apakah anda ingin logout? (ya/tidak): ").strip().lower()
    if pilih == "ya":
        teacher_profile = False
        print("Logout berhasil!")
        index.main()
    elif pilih == "tidak":
        print("Logout dibatalkan.")
    else:
        print("Tidak Valid. Silahkan pilih ya/tidak.")