# Function dengan Arbitrary Keyword Arguments bernama "siswa"
def profil(**siswa):
    print("Halo, saya %s dari %s" % (siswa["nama"], siswa["sekolah"]))

# Dikirim dengan nama key, urutannya bebas
profil(sekolah="SMKN 2 Subang", nama="Nurul")
