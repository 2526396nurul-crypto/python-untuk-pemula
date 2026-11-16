# Mengubah penamaan parameter self dengan nama param
# Parameter pertama di semua method tetap harus ada
class Siswa:
    sekolah = "SMKN 2 Subang"

    def tampilkan(param):
        print("Sekolah saya %s" % param.sekolah)

# Membuat object baru
siswa_1 = Siswa()

# Memanggil method di dalam Class
siswa_1.tampilkan()
