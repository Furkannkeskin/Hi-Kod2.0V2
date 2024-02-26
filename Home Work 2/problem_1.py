print("""****************
Kullanıcıdan maaş bilgisi alıp vergi kesintisi hesaplama
Maaş hesaplama programını sonlandırmak için lütfen "q" ya basın.
****************""")

while True:
    maas = input("Lütfen maaşınızı girin: ")

    if maas.lower() == "q":
        print("İyi günler dileriz.")
        break

    maas = int(maas)  # Kullanıcının girişini integer'a çevir

    if maas < 10000:
        vergi_tutarı = maas * 0.05
        yeni_maas = maas - vergi_tutarı
        print(f"Yeni maaşınız: {yeni_maas}")
    elif maas < 25000:
        vergi_tutarı = maas * 0.1
        yeni_maas = maas - vergi_tutarı
        print(f"Yeni maaşınız: {yeni_maas}")
    elif maas < 45000:
        vergi_tutarı = maas * 0.25
        yeni_maas = maas - vergi_tutarı
        print(f"Yeni maaşınız: {yeni_maas}")
    else:
        vergi_tutarı = maas * 0.3
        yeni_maas = maas - vergi_tutarı
        print(f"Yeni maaşınız: {yeni_maas}")