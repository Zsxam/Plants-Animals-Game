import os
import json
import random

# File yang berisi informasi hewan dan tumbuhan
SUBJECTS_FILE = "game_core/subjects.json"
# File yang berisi pertanyaan kuis
QUIZ_FILE = "game_core/quiz_questions.json"
# File yang berisi kelas
KELAS_FILE = "mode/class_mode/kelas.json"

# Load data dari file JSON
def load_data(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File {filename} tidak ditemukan")
        return None

def save_data(data, filename):
    try:
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
    except FileNotFoundError:
        print(f"File {filename} tidak ditemukan")
        return None

# Fungsi untuk siswa memilih telur di Mode Mandiri atau Mode Kelas
def crack_eggs(subject_type, name, class_code):
    subjects_data = load_data(SUBJECTS_FILE)
    
    if subject_type not in subjects_data:
        print(f"Subjek '{subject_type}' tidak ditemukan di data.")
        return
    
    selected_eggs = set()
    num_eggs = 5 
    cracked_subjects = []
    available_subjects = subjects_data[subject_type][:]  # Salin daftar subjek agar data asli tidak terpengaruh
    
    print(f"Kamu harus memecahkan 3-5 telur dengan memilih angka dari 1 hingga 15 untuk melanjutkan ke kuis.")

    while len(selected_eggs) < num_eggs:
        try:
            choice = int(input("\nPilih nomor telur (1-15): "))
            if choice < 1 or choice > 15:
                print("Nomor telur harus antara 1 hingga 15.")
                continue
            if choice in selected_eggs:
                print("Telur ini sudah dipilih sebelumnya!")
                continue

            if not available_subjects:
                print("Tidak ada subjek tersisa untuk dipilih.")
                break

            # Pilih subjek secara acak dan hapus dari daftar
            subject_info = random.choice(available_subjects)
            available_subjects.remove(subject_info)

            selected_eggs.add(choice)
            cracked_subjects.append(subject_info["name"])
            print(f"Telur {choice}: {subject_info['name']} - {subject_info['info']}")

            # Cek jumlah telur yang telah dipecahkan
            if len(selected_eggs) == 3:
                while True:
                    verif = input("\nAnda sudah memecahkan 3 cracks, apakah anda ingin melanjutkan ke quiz? (ya/tidak): ")
                    if verif.lower() == "ya":
                        return cracked_subjects
                    elif verif.lower() == "tidak":
                        print("Anda bisa memecahkan 2 kali lagi.")
                        break
                    else:
                        print("Pilihan tidak valid, silakan memasukkan 'ya' atau 'tidak'")
                        
            elif len(selected_eggs) == 4:
                while True:
                    verif = input("\nAnda sudah memecahkan 4 cracks, apakah anda ingin melanjutkan ke quiz? (ya/tidak): ")
                    if verif.lower() == "ya":
                        return cracked_subjects
                    elif verif.lower() == "tidak":
                        print("Anda bisa memecahkan 1 kali lagi.")
                        break
                    else:
                        print("Pilihan tidak valid, silakan memasukkan 'ya' atau 'tidak'")
            elif len(selected_eggs) == 5:
                print("Anda telah memecahkan 5 telur. Melanjutkan ke kuis.")
                return cracked_subjects

        except ValueError:
            print("Masukkan nomor yang valid!")

# Fungsi Kuis dengan pertanyaan berdasarkan isi telur yang dipecahkan
def quiz(cracked_subjects, name, class_code):
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
        while True:
            try:
                answer = int(input("Pilih jawaban yang benar (masukkan nomor 1-3): "))
                if 0 < answer <= 3:
                    if question_data["options"][int(answer) - 1] == question_data["answer"]:
                        print("Jawaban kamu benar!")
                        score += 1
                    else:
                        print(f"Jawaban salah. Jawaban yang benar adalah: {question_data['answer']}")
                    break
                else:
                    print("Kamu memasukkan jawaban yang tidak ada di pilihan. Silahkan coba lagi.")
            except ValueError:
                print("Masukkan nomor yang valid!")

    score_updated = score/len(cracked_subjects)*100
    score_bulat = round(score_updated, 1)
    print(f"\nSkor kamu: {score_bulat}/100")

    # Menyimpan skor ke dalam kelas.json
    data_kelas = load_data(KELAS_FILE)
    for kelas in data_kelas["classes"]:
        if kelas["class_code"] == class_code:
            if "students_scores" not in kelas:
                kelas["students_scores"] = {}
            kelas["students_scores"][name] = score_bulat
            break

    save_data(data_kelas, KELAS_FILE)
    print(f"Skor {name} telah disimpan di kelas dengan kode {class_code}.")
    print("Kuis telah selesai!\n")
    while True:
        kembali = input("Ke menu awal? (ya/tidak): ")
        if kembali.lower() == "tidak":
            print("Terimakasih Sudah Memainkan Game Plants & Animals! 😊\n")
            quit()
        elif kembali.lower() == "ya":
            return True
        else: 
            print("Masukkan 'ya' atau 'tidak' untuk memilih jawaban yang benar.\n")
        