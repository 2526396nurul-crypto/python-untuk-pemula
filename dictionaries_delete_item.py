profil = {
    "nama_depan": "Nurul",
    "nama_belakang": "Azizah",
    "bab_selesai": 6
}

# Menghapus item dengan pop, wajib menyebut nama key
profil.pop("bab_selesai")
print(profil)

# Menghapus semua item dengan clear
profil.clear()
print(profil)
