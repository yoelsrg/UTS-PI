class BMI:
    def __init__(self, berat_pound, tinggi_kaki):
        self.berat = berat_pound
        self.tinggi = tinggi_kaki

    def BMI_Value(self):
        # Konversi tinggi 
        tinggi_meter = self.tinggi * 0.3048
        # Konversi berat 
        berat_kg = self.berat * 0.453592
        # Hitung BMI
        bmi = berat_kg / (tinggi_meter ** 2)
        return bmi

    def __eq__(self, lainnya):
        return self.berat == lainnya.berat and self.tinggi == lainnya.tinggi

# Berat dan Tinggi:
orang1 = BMI(160, 5)  
orang2 = BMI(180, 6)

print("BMI orang pertama:", orang1.BMI_Value())
print("BMI orang kedua:", orang2.BMI_Value())

# Periksa apakah dua orang memiliki berat dan tinggi yang sama
print("Apakah orang pertama dan orang kedua sama?")
print("= ",orang1 == orang2)

