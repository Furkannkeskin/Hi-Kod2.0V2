print("""**************
Numpy kütüphanesi ve array kullanımı
**************""")
import numpy as np

# Array oluşturma
sayilar = np.array([1, 2, 3, 4, 5])

# Array boyutunu ve eleman sayısını kontrol etme
boyut = sayilar.ndim
eleman_sayisi = sayilar.size

print("Array Boyutu:", boyut)
print("Eleman Sayısı:", eleman_sayisi)