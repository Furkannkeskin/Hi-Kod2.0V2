print("""*************
Listelerde index ve slicing işlemleri yapma
*************""")
liste = ["Python", True, 9, "3", 8.4, "Hi-Kod", "False", 4.7]

# "3" değerine ulaşmak için indexleme.
deger_1 = liste[3]
print(deger_1)

# "Hi-Kod" değerine ulaşmak için indexleme.
deger_2 = liste[5]
print(deger_2)

# 4.7 değerine ulaşmak için indexleme.
deger_3 = liste[-1]
print(deger_3)

# 9,"3",8.4,"Hi-Kod" değerlerine ulaşmak için slicing.
slicing_1 = liste[2:6]
print(slicing_1)

# 8.4,"Hi-Kod","False",4.7 değerlerine ulaşmak için slicing.
slicing_2 = liste[4:]
print(slicing_2)