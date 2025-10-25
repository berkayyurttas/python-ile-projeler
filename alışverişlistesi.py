alisveris_listesi= []
MİN_URUN = 4
def urun_ekle():
    urun=input("Sepete eklemek istediğiniz ürünü yazınız: ")
    alisveris_listesi.append(urun)

    print(f"{urun} eklendi.")
    liste_goster()

def urun_sil():
    if len(alisveris_listesi) < MİN_URUN:
        print(f"Sepette minimum {MİN_URUN} olmalı, daha fazla silemezsiniz! ")
        return
    urun=input("Sepetten silmek istediğiniz ürünü giriniz: ")
    if urun in alisveris_listesi:

        alisveris_listesi.remove(urun)
    else: 

        print(f"{urun} listede yok! ")
    liste_goster()
    
def liste_goster():

   if alisveris_listesi:
       
       print("Alişveriş listesiniz:  ")
       for i, urun in enumerate(alisveris_listesi, start=1):
           print(f"{i}. {urun}") #numara ve isim ile ekrana bastırırız.
   else:
       
       print("Alişveriş listeniz boş. ")

def ana_menu():
   
    while True:
        print("\n-----Alişveriş listenizi giriniz. ")
        print("1.ürün ekle. ")
        print("2.ürün çikar. ")
        print("3.Alişveriş listesini göster. ")
        print("Çikiş yapiliyor. ")
        secim= input("Hangisini seçmek istersiniz(1/2/3/4): ")
        if secim=="1":
          urun_ekle()
        elif secim=="2":
          urun_sil()
        elif secim=="3":
          liste_goster()
        elif secim=="4":
           if len(alisveris_listesi) < MİN_URUN:
               print(f"Sepette minimum {MİN_URUN} ürün olmali. Lütfen ürün ekleyiniz.")
           else:
               print("Programdan çikiliyor.")
               break
        else:
             print("Geçersiz seçim! Lütfen 1/2/3/4 ten birisini seçiniz.")
    
ana_menu()