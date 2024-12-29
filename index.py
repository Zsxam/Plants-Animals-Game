import os
import auth_teacher.logout.logout as lo
import auth_teacher.login.login as login
import auth_teacher.register.register as reg
import mode.class_mode.class_mode as classes
import mode.self_mode.self_mode as selfs
import teacher_menu.menu as menu

os.system('cls')
# Main Program
def main(name=""):
    while True:
        print(f"Selamat datang di Plants & Animals! [{name}]")
        print("1. Registrasi Guru")
        print("2. Login Guru")
        print("3. Mode Mandiri")
        print("4. Mode Kelas")
        print("5. Keluar")

        choice = input("Pilih opsi (1-5): ")
        if choice == "1":
            os.system('clear')
            reg.register_teacher()
        elif choice == "2":
            teacher_profile = login.login_teacher()
            menu.teacher_menu(teacher_profile)
        elif choice == "3":
            os.system('clear')
            selfs.self_mode()
        elif choice == "4":
            os.system('clear')
            classes.class_mode()
        elif choice == "5":
            print("Terimakasih Sudah Memainkan Game Plants & Animals! 😊")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()