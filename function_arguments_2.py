# Membuat Function dengan dua Arguments: nama (string) dan bab (integer)
def perkenalan(nama, bab):
    print("Halo, saya %s. Bab yang selesai: %d" % (nama, bab))

# Dikirim secara berurutan (nama, bab)
perkenalan("Nurul", 6)

# Dikirim dengan nama key, jadi urutannya boleh berbeda
perkenalan(bab=6, nama="Nurul")
