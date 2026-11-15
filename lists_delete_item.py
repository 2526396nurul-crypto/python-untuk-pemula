bab = ["Pengenalan", "Variabel", "Operator"]

# Menghapus item tertentu dengan remove
bab.remove("Variabel")
print(bab)

# Menghapus item terakhir dengan pop
bab = ["Pengenalan", "Variabel", "Operator"]
bab.pop()
print(bab)

# Menghapus item berdasarkan posisinya dengan pop(0)
bab = ["Pengenalan", "Variabel", "Operator"]
bab.pop(0)
print(bab)

# Menghapus semua item dengan clear
bab = ["Pengenalan", "Variabel", "Operator"]
bab.clear()
print(bab)

# Menggabungkan dua lists dengan extend dan tanda +
bab_awal = ["Pengenalan", "Variabel"]
bab_lanjut = ["Operator", "Kondisi"]
bab_awal.extend(bab_lanjut)
print(bab_awal)

semua = bab_lanjut + ["Perulangan"]
print(semua)
