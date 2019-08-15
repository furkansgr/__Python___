# region Ödev-1

'''
Girilen günün haftanın kaçıncı günü olduğunu veren fonksiyon
Pazartesi girildiğinde 1, cuma girildiğinde 5 cıktısını verecek
Günler bir listede tutulacak ,listedeki indexine göre çıktı verilecek
Listedeki elemanlarla girilen değerler karşılaştırılacak
Hata yakalama olucak,hatalı bir durum oluşursa kullanıcıya hata mesajı verrilecek

'''

gün = input("Gün Girin:")

def HafGün(gün):
    i = 0
    günler = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]
    gün = gün.capitalize()
    for i in range(i, len(günler)):
        if gün == günler[i]:
            return "Haftanın {}. günü ".format(i + 1)
    try:
        if gün != günler[i]:
            raise Exception("ValueError")
    except:
        print("Hata")
print(HafGün(gün))

# endregion


# region Ödev-2

'''
Oyun random kütüphanesi kullanılarak 1 ile 45 arasında 6 tane  sayı üretip listeye atayan bir fonksiyon tanımlanacak
Kullanıcının girdiği üç değer bu listedeki sayılar arasında var mı kontrol edecek olan bir fonksiyon tanımlayalım

'''

dd =[]
for a in range(0,3):
    sayı = int(input("Sayı Girin:"))
    dd.append(sayı)
def SayıUret():
    import random as rnd
    liste = []
    for i in range(0,6):
        a = rnd.randint(1,5)
        liste.append(a)
    print(liste)
    return liste
benimListem = SayıUret()
def Kontrol():
    sayac = 0
    for k in range(0,len(dd)):
        if dd[k] in benimListem:
            sayac = + 1
    return "{} değer listede mevcut".format(sayac)
print(Kontrol())

#  if dd in SayıUret():
   #     return "Bu değerler listede mevcut"
    #else:
     #   return "Bu değerler listede mevcut değil"
# endregion
