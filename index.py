
import auth_teacher.logout.logout as lo
import auth_teacher.login.login as login
import auth_teacher.register.register as reg
import mode.class_mode.class_mode as classes
import mode.self_mode.self_mode as selfs

# Main Program
def main():
    print("Selamat datang di Plants & Animals!")
    print("1. Registrasi Guru")
    print("2. Login Guru")
    print("3. Mode Mandiri")
    print("4. Mode Kelas")

    choice = input("Pilih opsi (1-4): ")
    if choice == "1":
        reg.register_teacher()
    elif choice == "2":
        teacher_profile = login.login_teacher()
        if teacher_profile:
            print("1. Buat Kelas")
            print("2. Logout")
            sub_choice = input("Pilih opsi (1-2): ")
            if sub_choice == "1":
                classes.create_class(teacher_profile)
            elif sub_choice == "2":
                lo.teacher_logout()
    elif choice == "3":
        selfs.self_mode()
    elif choice == "4":
        classes.class_mode()
    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()