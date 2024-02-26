print("""***************
Arrayler üzerinde indexleme ve slicing işlemi
***************""")
import numpy as np

# İki boyutlu array oluşturma
iki_boyutlu_array = np.array([[1, 2, 3], [4, 5, 6]])

# Üç boyutlu array oluşturma
uc_boyutlu_array = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])

# İki boyutlu array bilgileri
print("İki Boyutlu Array:")
print("Boyut:", iki_boyutlu_array.ndim)
print("Eleman Sayısı:", iki_boyutlu_array.size)
print("Satır ve Sütun Sayısı:", iki_boyutlu_array.shape)

# Üç boyutlu array bilgileri
print("\nÜç Boyutlu Array:")
print("Boyut:", uc_boyutlu_array.ndim)
print("Eleman Sayısı:", uc_boyutlu_array.size)
print("Satır, Sütun ve Yükseklik Sayısı:", uc_boyutlu_array.shape)

# İki boyutlu array indexleme ve dilimleme
print("\nİki Boyutlu Array Indexleme ve Dilimleme:")
print("İlk satır:", iki_boyutlu_array[0])
print("İkinci satır, ikinci sütun:", iki_boyutlu_array[1, 1])
print("Tüm satırlar, ikinci sütun:", iki_boyutlu_array[:, 1])
print("Tüm satırlar, ikinci sütun üzeri dilim:", iki_boyutlu_array[:, 1:2])

# Üç boyutlu array indexleme ve dilimleme
print("\nÜç Boyutlu Array Indexleme ve Dilimleme:")
print("İlk matris:")
print(uc_boyutlu_array[0])
print("İlk matris, ilk satır, ikinci sütun:", uc_boyutlu_array[0, 0, 1])
print("İlk matris, tüm satırlar, ikinci sütun:", uc_boyutlu_array[0, :, 1])