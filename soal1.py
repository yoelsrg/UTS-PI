import math
from datetime import datetime

def bagi_dengan_hari(bilangan):
    # Tahun saat ini
    tahun_saat_ini = datetime.now().year

    # Periksa apakah tahun kabisat
    if tahun_saat_ini % 4 == 0 and (tahun_saat_ini % 100 != 0 or tahun_saat_ini % 400 == 0):
        jumlah_hari_tahun = 366
    else:
        jumlah_hari_tahun = 365

    # Bagi bilangan 
    hasil = bilangan / jumlah_hari_tahun

    # Bulatkan hasil ke 11 tempat desimal
    hasil_bulat = round(hasil, 11)

    # Tampilkan hasil
    print("Hasil:", hasil_bulat)

# Input pengguna
bilangan = int(input("Masukkan sebuah bilangan bulat: "))

# Fungsi untuk membagi dengan jumlah hari dalam tahun ini
bagi_dengan_hari(bilangan)
