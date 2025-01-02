import game_core.game as game

# Fungsi Mode Mandiri
def self_mode():
    print("Kamu memilih Mode Mandiri.")
    while True:
        subject_type = input("Pilih jenis subjek untuk dipelajari (Plants/Animals): ").capitalize()
        
        if subject_type in ["Plants", "Animals"]:
            break
        print("Jenis subjek tidak valid. Silakan pilih 'Plants' atau 'Animals'.\n")

    # Mulai pemecahan telur setelah memilih subjek
    print(f"Subjek yang anda pilih adalah {subject_type.capitalize()}\n")
    cracked_subjects = game.crack_eggs(subject_type)

    if cracked_subjects:
        game.quiz(cracked_subjects)
    else:
        print("Tidak ada subjek yang dapat dipelajari. Kembali ke menu utama.\n")