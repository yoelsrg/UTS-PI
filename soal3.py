from datetime import datetime, timedelta

def cetak_tanggal_mendatang(hari):
    # Tanggal hari ini
    hari_ini = datetime.now()

    # Hitung tanggal kedepannya
    tanggal_mendatang = hari_ini + timedelta(days=hari)

    # Cetak tanggal kedepannya
    tanggal_terformat = tanggal_mendatang.strftime("%A pada %d %B %Y")
    print("Tanggal", hari, "hari dari sekarang adalah:", tanggal_terformat)

# Dapatkan input dari pengguna
hari = int(input("Masukkan jumlah hari dari sekarang: "))

# Cetak tanggal mendatang
cetak_tanggal_mendatang(hari)
