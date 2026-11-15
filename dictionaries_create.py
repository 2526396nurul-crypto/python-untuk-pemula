# Membuat dictionaries untuk menyimpan profil singkat
profil = {
    "nama_depan": "Nurul",
    "nama_belakang": "Azizah",
    "sekolah": "SMKN 2 Subang"
}

# Mengakses item dengan 2 cara
# Cara pertama
print(profil["nama_depan"])

# Cara kedua dengan method get
print(profil.get("sekolah"))

# Mendapatkan semua keys
print(profil.keys())
