print("""*************
Deişkenlere atanmış değerlerin veri tipleri arasında denüşüm yapma
*************""")

değişken_1 = "Furkan" #String - Integer Dönüşümü
değişken_2 = "123"

try:
    integer_değeri_1 = int(değişken_1)
    print("değişken_1 integer değeri:", integer_değeri_1)
except ValueError:
    print("değişken_1 dönüşüm hatası: String içinde sayısal bir değer bulunmamaktadır.")

try:
    integer_değeri_2 = int(değişken_2)
    print("değişken_2 integer değeri:", integer_değeri_2)
except ValueError:
    print("değişken_2 dönüşüm hatası: String içinde sayısal bir değer bulunmamaktadır.")

my_tuple = (1, 2, 3, 4, 5) #Tuple-Liste Dönüşümü
my_list = list(my_tuple)
print(my_list)

my_list = [1, 2, 3, 4, 5] #Liste-Tuple Dönüşümü
my_tuple = tuple(my_list)
print(my_tuple)

boolean_değer1 = True #Boolean-String Dönüşümü
string_değer1 = str(boolean_değer1)
print(string_değer1)  # "True"

string1 = "Hello" #String bir ifadenin Boolean'a çevrilmesi
bool_value1 = bool(string1)
print(bool_value1)  # True

string2 = ""   #Boş bir stringin Boolean'a çevrilmesi
bool_value2 = bool(string2)
print(bool_value2)  # False

değişken_5 = 2 #Integer-Float dönüşümü
float_değeri = float(değişken_5)
print(float_değeri)

değişken_6 = 3.14 #Float- Integer dönüşümü
integer_değeri = int(değişken_6)
print(integer_değeri)