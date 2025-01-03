import os
import json
import random
import index

# File yang berisi informasi hewan dan tumbuhan
SUBJECTS_FILE = "game_core/subjects.json"
# File yang berisi pertanyaan kuis
QUIZ_FILE = "game_core/quiz_questions.json"

# Load data dari file JSON
def load_data(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File {filename} tidak ditemukan")
        return None

# Fungsi untuk siswa memilih telur di Mode Mandiri atau Mode Kelas
def crack_eggs(subject_type):
    subjects_data = load_data(SUBJECTS_FILE)
    
    if subject_type not in subjects_data:
        print(f"Subjek '{subject_type}' tidak ditemukan di data.")
        return
    
    selected_eggs = set()
    num_eggs = 5 
    cracked_subjects = []
    available_subjects = subjects_data[subject_type][:]  # Salin daftar subjek agar data asli tidak terpengaruh
    
    print(f"Kamu harus memecahkan 3-5 telur dari 1 hingga 15 untuk melanjutkan ke kuis.")

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

    # Setelah memecahkan telur, siswa bisa mengikuti kuis
    # verif = "tidak"
    # while verif.lower() != "ya":
    #     verif = input("\nApakah anda ingin langsung melanjutkan ke quiz? (ya/tidak): ")
    #     if verif.lower() == "ya":
    #         os.system('cls')
    #     else: 
    #         print("\nSilahkan baca-baca dahulu (scroll keatas)")

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
                    print("Kamu memasukkan jawaban yang tidak ada di pilihan. Silahkan coba lagi\n")
            except ValueError:
                print("Masukkan nomor yang valid!\n")

    score_updated = int(score/len(cracked_subjects)*100)
    print(f"\nSkor kamu: {score_updated}/100")
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