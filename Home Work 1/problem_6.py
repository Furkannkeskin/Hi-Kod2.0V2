print("""***************
Çift ve Tek sayıları bulma
***************""")
# String ifadeyi bir değişkene tanımla
ifade = "0123456789"

# Çift ve tek rakamları ayırmak için boş string'ler tanımla
cift_sayilar = ""
tek_sayilar = ""

# Her bir rakamı kontrol et ve çift/tek gruplarına ekleyerek ayrıştır
for rakam in ifade:
    if int(rakam) % 2 == 0:
        cift_sayilar += rakam
    else:
        tek_sayilar += rakam

# Sonuçları ekrana yazdır
print("Çift Sayılar:", cift_sayilar)
print("Tek Sayılar:", tek_sayilar)