print("""***************
Kullanıcıdan pi değeri ve yarı çap bilgisi alınarak dairenin alanını ve çevresini hesaplama
***************""")
# Kullanıcıdan pi değeri ve yarı çap bilgisi alınır
pi = float(input("Lütfen pi değerini girin: "))
yaricap = float(input("Lütfen dairenin yarı çapını girin: "))

# Dairenin alanını ve çevresini hesapla
alan = pi * yaricap**2
cevre = 2 * pi * yaricap

# Sonuçları ekrana yazdır
print(f"Dairenin alanı: {alan}")
print(f"Dairenin çevresi: {cevre}")