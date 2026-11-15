# Menghentikan perulangan jika nomor bab adalah 5
# Bab 5 belum dikerjakan, jadi perulangan berhenti sebelum mencetaknya
for bab in range(1, 12):
    if bab == 5:
        break
    print(bab)

# Melewati perulangan jika nomor bab adalah genap (2, 4, 6 dst)
# Hanya nomor ganjil yang dicetak karena yang genap di-skip dengan "continue"
for bab in range(1, 8):
    if bab % 2 == 0:
        continue
    print(bab)
