print("""***************
Kullanıcı Grişi Programı
****************
""")
sys_kulanıcı_adı="furkan"
sys_parola="12345"
giriş_hakkı=3
while True:
    kulanıcı_adı=input("Kulanıcı Adı:")
    parola=input("Parola:")
    if(kulanıcı_adı != sys_kulanıcı_adı and parola==sys_parola):
        print("Kullanıcı Adı Hatalı...")
        giriş_hakkı -=1
    elif(kulanıcı_adı == sys_kulanıcı_adı and parola !=sys_parola):
        print("Hatalı Parola Girdiniz.")
        giriş_hakkı -=1
    elif(kulanıcı_adı !=sys_kulanıcı_adı and parola!= sys_parola):
        print("Hatalı Kulanıcı Adı ve Parola Girdiniz...")
        giriş_hakkı -=1
    else:
        print("Sisteme Başarıyla Giriş Yapıldı.")
        break
    if (giriş_hakkı==0):
        print("Giriş Hakkınız Bitti.")
        break