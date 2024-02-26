import time

print("""******************
Kullanıcıdan isim, soy_isim,yaş,şehir ve meslek bilgisi alma
******************""")

ad=input("Kullanıcı adı:")
soy_ad=input("Kullanıcı soy_adı:")
yas=input("Kullanıcı yaşı:")
sehir=input("Kullanıcı şehri:")
meslek=input("Kullancı mesleği:")

bilgiler=[ad,soy_ad,yas,sehir,meslek]

print("Bilgiler Kaydediliyor....")
time.sleep(1)
print(f"Kullanıcı adı:{ad}\nKullanıcı soy_adı:{soy_ad}\nKullanıcı yaşı:{yas}\nKullanıcı şehri:{sehir}\nKullanıcı mesleği:{meslek}")
print("Bilgiler Kaydedildi.")