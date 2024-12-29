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
Plants-Animals-Game/ │ ├── auth_teacher/ │ ├── data_guru.json # Data guru yang terdaftar │ ├── login/ │ │ └── login.py # Modul untuk login guru │ ├── logout/ │ │ └── logout.py # Modul untuk logout guru │ └── register/ │ └── register.py # Modul untuk registrasi guru │ ├── game_core/ │ ├── game.py # Modul utama untuk permainan │ ├── game_kelas.py # Modul untuk permainan di mode kelas │ ├── quiz_questions.json # Pertanyaan kuis │ └── subjects.json # Data tentang tanaman dan hewan │ ├── mode/ │ ├── class_mode/ │ │ ├── class_mode.py # Modul untuk mode kelas │ │ └── kelas.json # Data kelas │ └── self_mode/ │ └── self_mode.py # Modul untuk mode mandiri │ ├── teacher_menu/ │ └── menu.py # Modul untuk menu guru │ ├── index.py # Modul utama untuk menjalankan aplikasi └── README.md # Dokumentasi proyek
```

## Cara Menjalankan Aplikasi
1. **Clone Repository**:
   ```bash
   git clone <URL_REPOSITORY>
   cd Plants-Animals-Game
2. Instalasi Dependensi: Pastikan Anda memiliki Python terinstal. Jika ada dependensi tambahan, Anda dapat menginstalnya menggunakan pip.
3. Jalankan Aplikasi:
   ```bash
   python index.py

## Kontribusi
Jika Anda ingin berkontribusi pada proyek ini, silakan fork repositori ini dan buat pull request dengan perubahan Anda.

## Lisensi
Proyek ini dikerjakan untuk memenuhi tubes Mata Kuliah Pengantar Rekayasa Perangkat Lunak dan Dasar Pemograman.

## Kontak
Jika Anda memiliki pertanyaan atau saran, silakan dm.
