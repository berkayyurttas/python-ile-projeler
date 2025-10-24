def topla(a,b):
    return a+b
def cikarma(a,b):
    return a-b
def carpma(a,b):
    return a*b
def bolme(a,b):
    if b==0:
        return "Hata: Sifira bölünemez!"
         
    return a/b
print("HESAP MAKİNASI")
print("1.Toplama \n 2.Çikarma \n 3.Çarpma \n 4.Bölme")


secim=(input("Lütfen yapmak istediğiniz işlemi seçiniz: (1/2/3/4)"))
sayi1=float(input("Birinci sayi: "))
sayi2=float(input("İkinci sayi: ",))

if secim==1:
    print("Sonuç: ",topla(sayi1,sayi2))
elif secim==2:
    print("Sonuç: ",cikarma(sayi1,sayi2))
elif secim==3:
    print("Sonuç: ",carpma(sayi1,sayi2))
elif secim==4:
    print("Sonuç: ",bolme(sayi1,sayi2))
else:
    print("Geçersiz sayi")
