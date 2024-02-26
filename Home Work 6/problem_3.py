print("""**************
Numpy fonksiyonu ile oluşturulan arraylar üzerinde indexleme ve slicing işlemleri
**************""")
import numpy as np

# Bir boyutlu dizi oluşturma (ve indexleme)
bir_boyutlu = np.array([1, 2, 3, 4, 5])
print("Bir boyutlu dizi:")
print(bir_boyutlu)

# Bir boyutlu diziyi indexleme
print("Indexleme:")
print(bir_boyutlu[0])  # İlk eleman
print(bir_boyutlu[-1]) # Son eleman

# Bir boyutlu diziyi dilimleme (slicing)
print("Dilimleme:")
print(bir_boyutlu[1:4]) # 2. elemandan 4. elemana kadar (4. eleman dahil değil)

# İki boyutlu dizi oluşturma (ve indexleme)
iki_boyutlu = np.array([[1, 2, 3], [4, 5, 6]])
print("\nİki boyutlu dizi:")
print(iki_boyutlu)

# İki boyutlu diziyi indexleme
print("Indexleme:")
print(iki_boyutlu[0, 0])  # İlk eleman
print(iki_boyutlu[1, -1]) # İkinci satırın son elemanı

# İki boyutlu diziyi dilimleme (slicing)
print("Dilimleme:")
print(iki_boyutlu[:, 1:]) # Her satırın 2. sütundan sonrası

# Üç boyutlu dizi oluşturma (ve indexleme)
uc_boyutlu = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("\nÜç boyutlu dizi:")
print(uc_boyutlu)

# Üç boyutlu diziyi indexleme
print("Indexleme:")
print(uc_boyutlu[0, 0, 1]) # İlk matrisin ilk satırının ikinci elemanı
print(uc_boyutlu[1, -1, -1]) # İkinci matrisin son satırının son elemanı

# Üç boyutlu diziyi dilimleme (slicing)
print("Dilimleme:")
print(uc_boyutlu[:, 1:, :]) # Her matrisin ikinci satırı ve sonrası