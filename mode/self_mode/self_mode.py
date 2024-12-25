import game_core.game as game

# Fungsi Mode Mandiri
def self_mode():
    print("Kamu memilih Mode Mandiri.")
    subject_type = input("Pilih jenis subjek untuk dipelajari (Plants/Animals): ").capitalize()
    
    if subject_type not in ["Plants", "Animals"]:
        print("Jenis subjek tidak valid. Silakan pilih 'Plants' atau 'Animals'.")
        return

    # Mulai pemecahan telur setelah memilih subjek
    game.crack_eggs(subject_type)