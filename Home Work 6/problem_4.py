print("""****************
iki tane iki boyutlu arrayıbsatır ve sütun bazında birleştirme.
****************
iki tane iki boyutlu arrayıbsa""")
import numpy as np

# Sıfırlardan oluşan bir 2x3 boyutlu dizi oluşturma
sifirlar = np.zeros((2, 3))
print("Sıfırlar:")
print(sifirlar)

# Birlerden oluşan bir 2x3 boyutlu dizi oluşturma
birler = np.ones((2, 3))
print("\nBirler:")
print(birler)

# Satır bazında birleştirme
birlesik_satir = np.concatenate((sifirlar, birler), axis=0)
print("\nSatır bazında birleştirme:")
print(birlesik_satir)

# Sütun bazında birleştirme
birlesik_sutun = np.concatenate((sifirlar, birler), axis=1)
print("\nSütun bazında birleştirme:")
print(birlesik_sutun)