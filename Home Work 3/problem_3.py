print("""***********************
Doğum yılına göre yaş hesaplama
***********************""")
from datetime import datetime


def hesapla_yas(dogum_yili):
    simdiki_yil = datetime.now().year
    yas = simdiki_yil - dogum_yili
    return yas


while True:
    dogum_yili_input = input("Doğum yılınızı girin (Çıkış için 'q' tuşuna basın): ")

    if dogum_yili_input.lower() == 'q':
        print("Programdan çıkılıyor...")
        break

    elif dogum_yili_input.isdigit():
        dogum_yili = int(dogum_yili_input)
        yas = hesapla_yas(dogum_yili)
        print("Kişi {} yaşında.".format(yas))
    else:
        print("Geçersiz giriş! Lütfen bir doğum yılı girin veya 'q' tuşuna basarak çıkış yapın.")