# Membuat Class Siswa dengan property sekolah
class Siswa:
    sekolah = "SMKN 2 Subang"

# Membuat object dari Class Siswa
siswa_1 = Siswa()

# Mengakses property yang didefinisikan di dalam Class
print(siswa_1.sekolah)

# Constructor: method __init__ dijalankan saat object dibuat
class Peserta:
    sekolah = "SMKN 2 Subang"

    def __init__(self, nama):
        self.nama = nama

# Membuat object baru dengan mengirim nama
peserta_1 = Peserta("Nurul")
print(peserta_1.nama)
