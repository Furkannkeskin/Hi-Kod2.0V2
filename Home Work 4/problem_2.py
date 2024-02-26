print("""**************
Liste içindeki string değerleri yeni bir listeye atama
**************""")
liste = ["Python", True, 9, "3", 8.4, "Hi-Kod", "False", 4.7]
yeni_liste = []

for eleman in liste:
    if isinstance(eleman, str):  # Elemanın string olup olmadığını kontrol eder
        yeni_liste.append(eleman)

print(yeni_liste)