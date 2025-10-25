def not_ekle():
    not_metni = input("Eklemek istediğiniz notu yaziniz:")
    with open("notlar.txt", "a" , encoding="utf-8") as dosya:
      dosya.write(not_metni+ "\n")#kullanıcının yazdığı notu dosyaya ekler, sonra yeni satıra geçer.
    print("Not başariyla yüklendi!")

def notlari_goster():
    try:#Dosya yoksa hata vermesin diye hata yakalama yapısıdır.
      with open("notlar.txt","r",encoding="utf-8") as dosya:
         notlar =dosya.readlines()#Dosyadaki her satırı listeye çevirir
         if not notlar:
            print("Henüz bir not eklenmemiş.")
         else:
            print("\n----NOTLARINIZ----")
            for i, not_metni in enumerate(notlar, start= 1):#Her notun başına sıra numarası ekler
               print(f"{i}. {not_metni.strip()}")#strip satır  sonundaki \n yeni satır karakterini siler,daha düzgün görüntü verir.
    except FileNotFoundError:
      print("Henüz not dosyasi bulunamadi, önce not ekleyiniz. ")

def notlari_sil():
   notlari_goster()
   try:
      with open("notlar.txt","r",encoding="utf-8") as dosya:
         notlar = dosya.readlines()
      if not notlar:
         return
      silinen= int(input("\nSilmek istediğiniz notun numarasını giriniz: "))
      if 1 <= silinen <= len(notlar): #Girilen numaranın geçerli bir sıra numarası olup olmadığını kontrol eder.
          silinen = notlar.pop(silinen -1 )# o numaradaki listeden çıkarırız.
          with open("notlar.txt","w",encoding="utf-8") as dosya:
             dosya.writelines(notlar)
          print(f"'{silinen.strip()}' adlı not silindi.")
      else:
         print("Geçersiz numara!")
   except ValueError:
      print("Lütfen geçerli sayı giriniz: ")
   except FileNotFoundError:
      print("Henüz not dosyası yok.")

def ana_menu():
   while True:
      print("\n----NOT DEFTERİ UYGULAMASİ----")
      print("1.Yeni not ekle")
      print("2.Notları göster")
      print("3.Not sil")
      print("4.Çıkış")
      secim = input("Bir seçenek giriniz(1/2/3/4): ")
      if secim == "1":
         not_ekle()
      elif secim == "2":
         notlari_goster()
      elif secim == "3":
         notlari_sil()
      elif secim == "4":
         print("Programdan çikiliyor.")
         break
      else:
         print("Geçersiz seçim! Lütfen 1-4 arasında bir sayı giriniz.")
ana_menu()
