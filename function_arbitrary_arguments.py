# Function dengan Arbitrary Arguments bernama "daftar"
def tampilkan_bab(*daftar):
    for nama in daftar:
        print("Bab: %s" % nama)

# Jumlah value yang dikirim bebas
tampilkan_bab("Pengenalan", "Variabel", "Operator")
