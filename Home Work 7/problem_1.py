print("""********************
DataFrame oluşturma ve üzeerined işlem yapma
********************""")
import pandas as pd

import pandas as pd

# Sözlük oluşturma
sozluk = {
    "Kategori": ["Giyim","Giyim", "Ayakkabı","Aksesuar","Ayakkabı","Giyim","Aksesuar","Aksesuar","Ayakkabı","Giyim"],
    "Ürün": ["Kazak","T-shirt","Sandalet","Küpe","Spor Ayakkabı","Pantolon","Kolye","Yüzük","Çizme","Ceket"],
    "Fiyat": [300,180,450,50,700,400,150,80,850,900]
}

# DataFrame'e dönüştürme
df = pd.DataFrame(sozluk)

# 2. indexte bulunan kategori
kategori_2 = df.iloc[2]['Kategori']
print("2. indexte bulunan kategori:", kategori_2)

# 2. indexte bulunan ürün
urun_2 = df.iloc[2]['Ürün']
print("2. indexte bulunan ürün:", urun_2)

# 4.indexten 9.indexe kadar olan veriler
veriler_4_9 = df.iloc[4:10]
print("4.indexten 9.indexe kadar olan veriler:")
print(veriler_4_9)

# 1.indexten 6.indexe kadar olan ürünler
urunler_1_6 = df.iloc[1:7]['Ürün']
print("1.indexten 6.indexe kadar olan ürünler:")
print(urunler_1_6)

# ödev 2. kısım

# Giyim kategorisinde bulunan ürünler
giyim_urunleri = df[df["Kategori"] == "Giyim"]["Ürün"]
print("Giyim kategorisinde bulunan ürünler:")
print(giyim_urunleri)

# Ayakkabı kategorisinde bulunan ürünler
ayakkabi_urunleri = df[df["Kategori"] == "Ayakkabı"]["Ürün"]
print("\nAyakkabı kategorisinde bulunan ürünler:")
print(ayakkabi_urunleri)

# Aksesuar kategorisinde bulunan ürünler
aksesuar_urunleri = df[df["Kategori"] == "Aksesuar"]["Ürün"]
print("\nAksesuar kategorisinde bulunan ürünler:")
print(aksesuar_urunleri)

#ödev 3. kısım

# Giyim kategorisinde fiyatı 300'den fazla olan ürünler
giyim_fiyat_300 = df[(df["Kategori"] == "Giyim") & (df["Fiyat"] > 300)]
print("Giyim kategorisinde fiyatı 300'den fazla olan ürünler:")
print(giyim_fiyat_300)

# Ayakkabı kategorisinde fiyatı 600'den az olan ürünler
ayakkabi_fiyat_600 = df[(df["Kategori"] == "Ayakkabı") & (df["Fiyat"] < 600)]
print("\nAyakkabı kategorisinde fiyatı 600'den az olan ürünler:")
print(ayakkabi_fiyat_600)

# Aksesuar kategorisinde fiyatı 100'den fazla olan aksesuarlar
aksesuar_fiyat_100 = df[(df["Kategori"] == "Aksesuar") & (df["Fiyat"] > 100)]
print("\nAksesuar kategorisinde fiyatı 100'den fazla olan aksesuarlar:")
print(aksesuar_fiyat_100)