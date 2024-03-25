def hitung_hasil_perkalian(angka):
    hasil = 1
    for i in range(1, angka + 1):
        hasil *= i
    return hasil

# Inputpengguna
tanggal_ujian = int(input("Masukkan tanggal ujian hari ini (sebuah bilangan bulat): "))

# Hitung hasil perkalian dari semua nilai dari 1 hingga angka yang dimasukkan
hasil = hitung_hasil_perkalian(tanggal_ujian)

# Cetak hasilnya
print("Hasil perkalian dari semua nilai dari 1 hingga", tanggal_ujian, "adalah:", hasil)
