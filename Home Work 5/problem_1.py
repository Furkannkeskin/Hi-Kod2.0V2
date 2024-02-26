print("""***************
Sözlük oluşturma ve sözlük üzerinde işlemler
***************""")
# Öğrenci bilgilerini içeren sözlük
ogrenci_bilgileri = {
    "Ali": {"Matematik": 85, "Fizik": 75, "Kimya": 90},
    "Ayşe": {"Matematik": 70, "Fizik": 80, "Kimya": 65},
    "Mehmet": {"Matematik": 90, "Fizik": 85, "Kimya": 70}
}

# Kullanıcıdan isim ve ders ismi girişi alınır
isim = input("Öğrencinin adını girin: ")
ders = input("Notunu öğrenmek istediğiniz dersi girin (Matematik, Fizik, Kimya): ")

# Girilen isim ve ders ismine göre ilgili notu alınır
if isim in ogrenci_bilgileri and ders in ogrenci_bilgileri[isim]:
    notu = ogrenci_bilgileri[isim][ders]
    print(f"{isim} öğrencisinin {ders} dersinde aldığı not: {notu}")
else:
    print("Girilen öğrenci veya ders bilgisi bulunamadı.")