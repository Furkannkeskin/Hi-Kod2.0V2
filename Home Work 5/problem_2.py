print("""**************
Sözlük üzerinde işlem yapma
**************""")
# Öğrenci bilgilerini içeren sözlük
ogrenci_bilgileri = {
    "Ali": {"Matematik": 85, "Fizik": 75, "Kimya": 90},
    "Ayşe": {"Matematik": 70, "Fizik": 80, "Kimya": 65},
    "Mehmet": {"Matematik": 90, "Fizik": 85, "Kimya": 70}
}

# Kullanıcıya hangi işlemi yapmak istediğini sormak için menü gösterilir
while True:
    print("\n1. Öğrenci bilgilerini görüntüle")
    print("2. Yeni öğrenci ve not ekle")
    print("3. Not güncelle")
    print("4. Çıkış")

    secim = input("Yapmak istediğiniz işlemi seçin (1-4): ")

    # Öğrenci bilgilerini görüntüleme
    if secim == '1':
        isim = input("Öğrencinin adını girin: ")
        if isim in ogrenci_bilgileri:
            print(f"{isim} öğrencisinin bilgileri: {ogrenci_bilgileri[isim]}")
        else:
            print("Girilen öğrenci bulunamadı.")

    # Yeni öğrenci ve not ekleme
    elif secim == '2':
        isim = input("Yeni öğrencinin adını girin: ")
        matematik_notu = int(input("Matematik notunu girin: "))
        fizik_notu = int(input("Fizik notunu girin: "))
        kimya_notu = int(input("Kimya notunu girin: "))
        ogrenci_bilgileri[isim] = {"Matematik": matematik_notu, "Fizik": fizik_notu, "Kimya": kimya_notu}
        print(f"{isim} öğrencisinin bilgileri başarıyla eklendi.")

    # Not güncelleme
    elif secim == '3':
        isim = input("Notlarını güncellemek istediğiniz öğrencinin adını girin: ")
        if isim in ogrenci_bilgileri:
            ders = input("Güncellemek istediğiniz dersin adını girin (Matematik, Fizik, Kimya): ")
            if ders in ogrenci_bilgileri[isim]:
                yeni_not = int(input(f"Yeni {ders} notunu girin: "))
                ogrenci_bilgileri[isim][ders] = yeni_not
                print(f"{isim} öğrencisinin {ders} notu başarıyla güncellendi.")
            else:
                print("Girilen ders bilgisi bulunamadı.")
        else:
            print("Girilen öğrenci bulunamadı.")

    # Çıkış
    elif secim == '4':
        print("Programdan çıkılıyor...")
        break

    else:
        print("Geçersiz seçim! Lütfen 1 ile 4 arasında bir sayı girin.")