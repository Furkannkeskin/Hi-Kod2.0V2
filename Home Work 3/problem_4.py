print("""*****************
Kişinin yaşında göre emeklilik durumu hesaplama
*****************""")
from datetime import datetime


def hesapla_yas(dogum_yili):
    simdiki_yil = datetime.now().year
    yas = simdiki_yil - dogum_yili
    return yas


def emeklilik_durumu(isim, dogum_yili):
    yas = hesapla_yas(dogum_yili)
    emeklilik_yasi = 65

    if yas >= emeklilik_yasi:
        print("{} emekli oldunuz.".format(isim))
    else:
        kalan_yil = emeklilik_yasi - yas
        print("{} emekliliğine {} yıl kaldı.".format(isim, kalan_yil))


# Fonksiyonu kullanarak emeklilik durumunu kontrol etmek için:
isim = input("İsminizi girin: ")
dogum_yili = int(input("Doğum yılınızı girin: "))

emeklilik_durumu(isim, dogum_yili)