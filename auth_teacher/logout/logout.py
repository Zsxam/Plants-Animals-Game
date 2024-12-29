import index

def teacher_logout():
    print("Menu Logout")
    while True:
        pilih = input("Apakah anda ingin logout? (ya/tidak): ").strip().lower()
        if pilih == "ya":
            teacher_profile = False
            print("Logout berhasil!\n")
            return True
        elif pilih == "tidak":
            print("Logout dibatalkan.\n")
            return False
        else:
            print("Tidak Valid. Silahkan pilih ya/tidak.\n")