# Plants & Animals Game

## Deskripsi
Plants & Animals Game adalah aplikasi edukasi interaktif yang dirancang untuk membantu pengguna (khususnya anak sd) belajar tentang berbagai jenis tanaman dan hewan. Aplikasi ini memungkinkan guru untuk membuat kelas dan memberikan kode kelas tersebut kepada siswa. Lalu guru akan menerima hasil quiz yang dikerjakan siswa.

## Fitur
- **Registrasi Guru**: Guru dapat mendaftar untuk membuat akun.
- **Login Guru**: Guru dapat masuk ke akun mereka untuk mengakses fitur aplikasi.
- **Mode Mandiri**: Pengguna dapat memilih untuk belajar secara mandiri tentang tanaman atau hewan.
- **Mode Kelas**: Guru dapat membuat kelas dan mengelola siswa.
- **Kuis**: Setelah mempelajari materi, siswa dapat mengikuti kuis untuk menguji pengetahuan mereka (terdapat di kedua mode).
- **Pengelolaan Kelas**: Guru dapat menambah, mengedit, dan menghapus kelas yang mereka ajar.

## Struktur Proyek
```
Plants-Animals-Game/
│
├── auth_teacher/
│ ├── data_guru.json # Data guru yang terdaftar
│ ├── login/
│ │    └── login.py # Modul untuk login guru
│ ├── logout/
│ │    └── logout.py # Modul untuk logout guru
│ └── register/
│      └── register.py # Modul untuk registrasi guru
│
├── game_core/
│   ├── game.py # Modul utama untuk permainan
│   ├── game_kelas.py # Modul untuk permainan di mode kelas
│   ├── quiz_questions.json # Pertanyaan kuis
│   └── subjects.json # Data tentang tanaman dan hewan
│
├── mode/
│ ├── class_mode/
│ │ ├── class_mode.py # Modul untuk mode kelas
│ │ └── kelas.json # Data kelas
│ └── self_mode/
│ └── self_mode.py # Modul untuk mode mandiri
│
├── teacher_menu/
│ └── menu.py # Modul untuk menu guru
│
├── index.py # Modul utama untuk menjalankan aplikasi
└── README.md # Dokumentasi proyek
```

## Cara Menjalankan Aplikasi
1. **Clone Repository**:
   ```bash
   git clone https://github.com/Zsxam/Plants-Animals-Game.git
   cd Plants-Animals-Game
   ```
2. **Instalasi Dependensi**: 
   Pastikan Anda memiliki Python terinstal. Jika ada dependensi tambahan, Anda dapat menginstalnya menggunakan pip. Misal:
   ```bash
   python -m pip install json
   ```
3. **Jalankan Aplikasi**:
   ```bash
   python index.py
   ```

## Contoh Penggunaan
- Guru:
  1. Registrasi menggunakan modul **auth_teacher/register.py**.
  2. Login ke dalam sistem menggunakan **auth_teacher/login.py**.
  3. Melihat, membuat, mengubah, menghapus kelas di mode kelas.
  4. Melihat hasil kuis siswa.

- Siswa:
  1. Pilih mode belajar (mandiri atau kelas).
  2. Memasukkan kode jika mode kelas
  3. Pelajari materi tentang tanaman dan hewan.
  4. Ikuti kuis untuk mengevaluasi pemahaman.


## Kontribusi
- Fork repositori ini.
- Clone repositori ke lokal Anda:
  ```bash
  git clone <URL_FORK>
  ```
- Buat branch baru untuk fitur baru Anda:
  ```bash
  git checkout -b fitur-baru
  ```
  - Lakukan perubahan dan lakukan commit:
  ```bash
  git add .
  git commit -m "pesan perubahan"
  git push origin fitur-baru
  ```

## Lisensi
Proyek ini dikerjakan untuk memenuhi tubes Mata Kuliah Pengantar Rekayasa Perangkat Lunak dan Dasar Pemograman.

## Kontak
Jika Anda memiliki pertanyaan atau saran, silakan dm ke:
- Instagram: https://instagram.com/azkafdhln
- GitHub: https://github.com/Zsxam
