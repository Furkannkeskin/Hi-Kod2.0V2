print("""****************
Kullanıcı şifresi oluşturma gelişmiş örnek.
****************""")

while True:
    kullanici_adi = input("Kullanıcı adınızı girin: ")
    kullanici_sifresi = input("Şifrenizi girin: ")

    if 5 <= len(kullanici_sifresi) <= 10:
        print("Hesabınız oluşturuldu.")
        break
    else:
        print("Lütfen girdiğiniz şifre 5 haneden az, 10 haneden fazla olmasın!")