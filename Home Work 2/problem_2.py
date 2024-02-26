print("""**************
Kullanıcıdan 6 haneli şifre oluşturmasını isteme
**************
""")
while True:
    # Kullanıcıdan kullanıcı adı ve şifre istenir
    kullanici_adi = input("Kullanıcı adınızı oluşturun: ")
    sifre = input("Şifrenizi oluşturun: ")

    # Şifre uzunluğu kontrol edilir
    if len(sifre) >= 6:
        print("Hesabınız oluşturuldu!")
        break  # Şifre uzunluğu uygunsa döngüden çık
    else:
        print("Şifreniz en az altı karakterden oluşmalıdır. Lütfen yeniden deneyin.")