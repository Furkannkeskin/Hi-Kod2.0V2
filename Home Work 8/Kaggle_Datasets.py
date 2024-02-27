print("""*********************
Bir veri seti üzerinde analiz ve görselleştirme çalışmaları
*********************""")

import pandas as pd

# Veri setini yükleyelim
veri = pd.read_csv("meuArquivo.csv")

# Veri setini gösterelim
print(veri.head())

import matplotlib.pyplot as plt

# Kategori bazında toplam gelir miktarını hesaplayalım
kategori_gelir = veri.groupby('CATEGORIA PRODUTO')['TOTAL'].sum()

# Kategorik gelirleri çubuk grafik olarak görselleştirelim
kategori_gelir.plot(kind='bar')
plt.title('Kategoriye Göre Toplam Gelir')
plt.xlabel('Kategori')
plt.ylabel('Toplam Gelir')
plt.show()



# Kategori değişkenin frekans dağılımını gösterme
plt.figure(figsize=(10, 6))
veri['CATEGORIA PRODUTO'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Kategori Ürün Dağılımı')
plt.xlabel('Kategori')
plt.ylabel('Frekans')
plt.xticks(rotation=45)
plt.show()

# Sayısal değişkenin dağılımını gösterme
plt.figure(figsize=(10, 6))
plt.hist(veri['QTDE'], bins=20, color='orange', edgecolor='black')
plt.title('Ürün Miktarı Dağılımı')
plt.xlabel('Miktar')
plt.ylabel('Frekans')
plt.show()

# Değişkenler arasındaki ilişkiyi gösterme (örneğin, QTDE ve VALOR arasındaki ilişki)
plt.figure(figsize=(10, 6))
plt.scatter(veri['QTDE'], veri['VALOR'], color='green')
plt.title('Ürün Miktarı ve Değeri Arasındaki İlişki')
plt.xlabel('Miktar')
plt.ylabel('Değer')
plt.show()