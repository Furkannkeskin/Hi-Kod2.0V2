print("""***************
Split fonksiyonu,Upper Fonksiyonu,Lower Fonksiyonu
***************""")
# String ifadeyi bir değişkene tanımla
ifade = "Hi-Kod Veri Bilimi Atölyesi"

# String ifadeyi boşluklardan bölerek kelimelere ayır
kelimeler = ifade.split()

# Her bir kelimeyi ayrı bir değişkene atayarak ekrana yazdır
kelime1 = kelimeler[0]
kelime2 = kelimeler[1]
kelime3 = kelimeler[2]
kelime4 = kelimeler[3]

# Her bir kelimeyi ekrana yazdır
print("1. Kelime:", kelime1)
print("2. Kelime:", kelime2)
print("3. Kelime:", kelime3)
print("4. Kelime:", kelime4)

# String ifadeyi bir değişkene tanımla
ifade = "Hi-Kod Veri Bilimi Atölyesi"

# String ifadeyi tamamen büyük harfe çevir
ifade_buyuk = ifade.upper()

# Büyük harfe çevrilen ifadeyi ekrana yazdır
print(ifade_buyuk)

# String ifadeyi bir değişkene tanımla
ifade = "Hi-Kod Veri Bilimi Atölyesi"

# String ifadeyi tamamen küçük harfe çevir
ifade_kucuk = ifade.lower()

# Küçük harfe çevrilen ifadeyi ekrana yazdır
print(ifade_kucuk)
