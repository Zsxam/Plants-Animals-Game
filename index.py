import json
import random

# File yang berisi informasi hewan dan tumbuhan
SUBJECTS_FILE = "Plants-Animals-Game\subjects.json"
# File yang berisi pertanyaan kuis
QUIZ_FILE = "Plants-Animals-Game\quiz_questions.json"

def register_teacher():
    pass

def login_teacher():
    pass

def create_class():
    pass

# Load data dari file JSON
def load_data(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Fungsi untuk siswa memilih telur di Mode Mandiri atau Mode Kelas
def crack_eggs(subject_type):
    subjects_data = load_data(SUBJECTS_FILE)

    if subject_type not in subjects_data:
        print(f"Subjek '{subject_type}' tidak ditemukan di data.")
        return
    
    selected_eggs = set()
    num_eggs = random.randint(3, 5)
    print(f"Kamu harus memecahkan {num_eggs} telur dari 1 hingga 15 untuk melanjutkan ke kuis.")
    cracked_subjects = []

    while len(selected_eggs) < num_eggs:
        try:
            choice = int(input("Pilih nomor telur (1-15): "))
            if choice < 1 or choice > 15:
                print("Nomor telur harus antara 1 hingga 15.")
                continue
            if choice in selected_eggs:
                print("Telur ini sudah dipilih sebelumnya!")
                continue

            selected_eggs.add(choice)
            subject_info = random.choice(subjects_data[subject_type])
            cracked_subjects.append(subject_info["name"])  # Tambahkan subjek yang dipecahkan
            print(f"Telur {choice}: {subject_info['name']} - {subject_info['info']}")
        except ValueError:
            print("Masukkan nomor yang valid!")

    # Setelah memecahkan telur, siswa bisa mengikuti kuis
    quiz(cracked_subjects)


# Fungsi Mode Mandiri
def self_mode():
    print("Kamu memilih Mode Mandiri.")
    subject_type = input("Pilih jenis subjek untuk dipelajari (Plants/Animals): ").capitalize()
    
    if subject_type not in ["Plants", "Animals"]:
        print("Jenis subjek tidak valid. Silakan pilih 'Plants' atau 'Animals'.")
        return

    # Mulai pemecahan telur setelah memilih subjek
    crack_eggs(subject_type)

def class_mode():
    pass

# Fungsi Kuis dengan pertanyaan berdasarkan isi telur yang dipecahkan
def quiz(cracked_subjects):
    quiz_data = load_data(QUIZ_FILE)
    score = 0

    print("\nKuis dimulai! Jawab pertanyaan berikut:")

    for subject in cracked_subjects:
        if subject not in quiz_data:
            print(f"Tidak ada pertanyaan untuk subjek '{subject}'.")
            continue
        
        questions = quiz_data[subject]
        question_data = random.choice(questions)  # Pilih satu pertanyaan acak untuk setiap subjek
        print(f"\nPertanyaan tentang {subject}: {question_data['question']}")
        
        for i, option in enumerate(question_data["options"], 1):
            print(f"{i}. {option}")
        
        answer = input("Pilih jawaban yang benar (masukkan nomor): ")
        if question_data["options"][int(answer) - 1] == question_data["answer"]:
            print("Jawaban kamu benar!")
            score += 1
        else:
            print(f"Jawaban salah. Jawaban yang benar adalah: {question_data['answer']}")

    print(f"\nSkor kamu: {score}/{len(cracked_subjects)}")

# Main Program
def main():
    print("Selamat datang di Plants & Animals!")
    print("1. Registrasi Guru")
    print("2. Login Guru")
    print("3. Mode Mandiri")
    print("4. Mode Kelas")

    choice = input("Pilih opsi (1-4): ")
    if choice == "1":
        register_teacher()
    elif choice == "2":
        teacher_email = login_teacher()
        if teacher_email:
            print("1. Buat Kelas")
            sub_choice = input("Pilih opsi (1): ")
            if sub_choice == "1":
                create_class(teacher_email)
    elif choice == "3":
        self_mode()
    elif choice == "4":
        class_mode()
    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
