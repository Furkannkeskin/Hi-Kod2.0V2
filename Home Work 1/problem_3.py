print("""***************
Basic Hesap Makinesi
***************""")

# Kullanıcıdan iki değer alınır
sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))

# Toplama
toplam = sayi1 + sayi2
print(f"{sayi1} + {sayi2} = {toplam}")

# Çıkarma
cikarma = sayi1 - sayi2
print(f"{sayi1} - {sayi2} = {cikarma}")

# Çarpma
carpma = sayi1 * sayi2
print(f"{sayi1} * {sayi2} = {carpma}")

# Bölme
if sayi2 != 0:
    bolme = sayi1 / sayi2
    print(f"{sayi1} / {sayi2} = {bolme}")
else:
    print("Bir sayıyı sıfıra bölemezsiniz.")