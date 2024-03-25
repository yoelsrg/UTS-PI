def baca_bilangan_dari_berkas(nama_berkas):
    try:
        with open(nama_berkas, 'r') as berkas:
            bilangan = [int(line.strip()) for line in berkas]
        return bilangan
    except FileNotFoundError:
        print("Berkas tidak ditemukan.")
        return []

def cetak_jumlah_dengan_pemisah_koma(bilangan):
    total = sum(bilangan)
    total_terformat = "{:,}".format(total)
    print("Jumlah bilangan adalah:", total_terformat)

# Baca angka dari input.txt
bilangan = baca_bilangan_dari_berkas("input.txt")

# Cetak jumlah 
if bilangan:
    cetak_jumlah_dengan_pemisah_koma(bilangan)
