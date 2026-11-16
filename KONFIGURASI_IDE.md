# Konfigurasi IDE

Catatan Bab 10 (modul bagian 13 dan 14: PyCharm dan Instalasi PyCharm).

## Tentang PyCharm

PyCharm adalah IDE yang dibuat khusus untuk pengembang Python. Fitur yang disebut di modul:

- Intelligent Coding Assistance: syntax highlighting, autocomplete, deteksi dan koreksi kesalahan, serta pencarian dan perpindahan antar file.
- Built-in Developer Tools: debugging, menjalankan skrip, membuat Virtual Environment, dan Python console.
- VCS Support: mengunggah proyek ke repositori GitHub.

## Edisi

Modul menyebut tiga edisi: Professional, Community, dan Edu. Sejak PyCharm 2025.1, edisi Community dan Professional digabung menjadi satu produk bernama PyCharm, dan fitur intinya tetap gratis. Jadi keterangan edisi di modul sudah tidak sepenuhnya sama dengan keadaan sekarang.

## Cara instal menurut modul

- Windows: unduh installer, jalankan, lalu ikuti langkah instalasi sampai selesai.
- Linux: ekstrak dengan `sudo tar xzf pycharm-*.tar.gz -C /opt/`, masuk ke `/opt/pycharm-*/bin`, lalu jalankan `sh pycharm.sh`. Alternatifnya lewat snap: `sudo snap install pycharm-community --classic`.

## Lingkungan yang dipakai

Pengerjaan memakai Arch Linux di WSL2 dengan Python 3.14 dan Virtual Environment `.venv`. Berkas diketik lewat terminal. Pemasangan PyCharm tidak dilakukan dalam pengerjaan ini, jadi isi catatan ini berasal dari modul. Folder `.idea/` (berkas bawaan PyCharm) dimasukkan ke `.gitignore` supaya tidak ikut ter-commit.
