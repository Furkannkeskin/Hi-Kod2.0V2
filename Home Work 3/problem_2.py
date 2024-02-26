print("""***************
Faktöryel Bulma Ekranı

Çıkmak için 'q' ya basın.
***************
""")
def faktöryel_hesapla():
    while True:
        sayı = input("Sayı (çıkmak için 'q' ya basın): ")

        if sayı.lower() == "q":
            print("Program Sonlandırılıyor.")
            break
        elif int(sayı) < 0:
            print("Pozitif Sayı Giriniz.")
        else:
            sayı = int(sayı)
            faktöryel = 1
            for i in range(2, sayı + 1):
                print("Faktöryel", faktöryel, "i", i)
                faktöryel *= i
            print("Faktöryel:", faktöryel)

# Fonksiyonu çağır
faktöryel_hesapla()