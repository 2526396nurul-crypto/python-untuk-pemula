profil = {
    "nama_depan": "Nurul",
    "nama_belakang": "Azizah",
    "bab_selesai": 5
}

# Cara pertama mengubah value
profil["bab_selesai"] = 6

# Cara kedua dengan method update
# Jika key sudah ada, value diubah. Jika belum ada, item baru ditambahkan
profil.update({"bab_selesai": 6})
profil.update({"tugas": "PY1"})
print(profil)
