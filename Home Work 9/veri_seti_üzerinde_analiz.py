import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Veri setini yükleme
df = pd.read_csv(r"D:\meuArquivo.csv")

# Veri setinin ilk birkaç satırını gösterme
print(df.head())

# Satılan ürünlerin kategorilere göre dağılımının analizi
kategori_dagilimi = df['CATEGORIA PRODUTO'].value_counts()
print("Kategori Dağılımı:\n", kategori_dagilimi)

# Toplam satış miktarının ve gelirin zaman içindeki değişiminin analizi
df['DATA'] = pd.to_datetime(df['DATA'])
df['YIL'] = df['DATA'].dt.year
satıs_miktarı_zaman = df.groupby('YIL')['QTDE'].sum()
gelir_zaman = df.groupby('YIL')['TOTAL'].sum()
print("Satış Miktarı Zaman İçinde Değişimi:\n", satıs_miktarı_zaman)
print("Gelir Zaman İçinde Değişimi:\n", gelir_zaman)

# Mağaza bazında satış performansının karşılaştırılması
mağaza_satışları = df.groupby('LOJA')['TOTAL'].sum().sort_values(ascending=False)
print("Mağaza Bazında Satış Performansı:\n", mağaza_satışları)

# Satılan ürünlerin fiyat dağılımının ve ortalama fiyatının belirlenmesi
plt.figure(figsize=(10, 6))
sns.histplot(df['VALOR'], bins=20, kde=True)
plt.title("Ürün Fiyatı Dağılımı")
plt.xlabel("Fiyat")
plt.ylabel("Frekans")


ortalama_fiyat = df['VALOR'].mean()
print("Ortalama Fiyat:", ortalama_fiyat)

# İndirimlerin satışlara etkisinin analizi
indirim_oranı = df['DESCONTO'] / df['VALOR']
df['INDIRIM_ORANI'] = indirim_oranı
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='INDIRIM_ORANI', y='QTDE')
plt.title("İndirim Oranı ile Satış Miktarı Arasındaki İlişki")
plt.xlabel("İndirim Oranı")
plt.ylabel("Satış Miktarı")


# Müşteri cinsiyetine veya medeni durumuna göre satın alma davranışlarının analizi
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='SEXO', hue='ESTADO CIVIL')
plt.title("Cinsiyet ve Medeni Durum Bazında Satın Alma Davranışı")
plt.xlabel("Cinsiyet")
plt.ylabel("Satın Alma Sayısı")

plt.show()