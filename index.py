import os
import auth_teacher.logout.logout as lo
import auth_teacher.login.login as login
import auth_teacher.register.register as reg
import mode.class_mode.class_mode as classes
import mode.self_mode.self_mode as selfs
import teacher_menu.menu as menu

# Main Program
def main():
    while True:
        print(f"Selamat datang di Plants & Animals!")
        print("1. Registrasi Guru")
        print("2. Login Guru")
        print("3. Mode Mandiri")
        print("4. Mode Kelas")
        print("5. Keluar")

        choice = input("Pilih opsi (1-5): ")
        if choice == "1":
            os.system('cls')
            reg.register_teacher()
        elif choice == "2":
            teacher_profile = login.login_teacher()
            if teacher_profile: 
                menu.teacher_menu(teacher_profile)
        elif choice == "3":
            os.system('cls')
            selfs.self_mode()
        elif choice == "4":
            os.system('cls')
            classes.class_mode()
        elif choice == "5":
            print("Terimakasih Sudah Memainkan Game Plants & Animals! 😊")
            quit()
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()