# Function dengan Default Value pada Argument
def perkenalan(nama="Siswa"):
    print("Halo, saya %s" % nama)

# Dipanggil dengan Argument
perkenalan("Nurul")

# Dipanggil tanpa Argument, otomatis memakai Default Value
perkenalan()
