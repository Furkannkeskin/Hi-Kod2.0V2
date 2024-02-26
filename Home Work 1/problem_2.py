print("""*****************
İsimlerden oluşan üç değişkenin mantıksal operatörler ile karşılaştırılması.
*****************""")
# İsimlere yaş değerleri atanır
furkan_yaş = 22
mete_yaş = 25
berkay_yaş = 18

# Karşılaştırma ve mantıksal operatörlerle değerlendirme yapılır
karşılaştırma_sonucu_1 = furkan_yaş < mete_yaş
karşılaştırma_sonucu_2 = mete_yaş > berkay_yaş
karşılaştırma_sonucu_3 = furkan_yaş == berkay_yaş
mantıksal_sonuç = karşılaştırma_sonucu_1 and karşılaştırma_sonucu_2 and karşılaştırma_sonucu_3

# Sonuçlar yazdırılır
print("Furkan yaş küçük mü Mete'nin yaşından?:", karşılaştırma_sonucu_1)
print("Mete yaş büyük mü Berkay'ın yaşından?:", karşılaştırma_sonucu_2)
print("Furkan yaş Berkay'ın yaşına eşit mi?:", karşılaştırma_sonucu_3)
print("Her üç durum da doğru mu?:", mantıksal_sonuç)