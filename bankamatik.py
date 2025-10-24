dogru_pin = "123456"
bakiye = 50000

kullanici_adi = input("Lütfen Kullanici Adinizi Giriniz: ")
pin = input("Lütfen pin kodunuzu giriniz: ")

if pin == dogru_pin:
    print(f"Giriş başarılı, Hoşgeldiniz {kullanici_adi}!\n")
    
    while True:
        print("1. Bakiyeyi görüntüle")
        print("2. Para Yatır")
        print("3. Para Çek")
        print("4. Makbuz Görüntüle")
        print("5. Çıkış")

        secim = input("Seçiminiz: ")

        if secim == "1":
            print(f"Mevcut bakiyeniz: {bakiye} TL\n")
        
        elif secim == "2":
            para_yatir = float(input("Yatırmak istediğiniz miktar: "))
            bakiye += para_yatir
            print(f"Yeni bakiyeniz: {bakiye} TL\n")
            makbuz = input("Makbuz ister misiniz? (e/h): ").lower()
            if makbuz == "e":
                print(f"--- MAKBUZ ---\nİşlem: Para Yatırma\nMiktar: {para_yatir} TL\nYeni Bakiye: {bakiye} TL\n----------------\n")
            else:
                print("Uyarı!! Makbuz almayarak doğayı koruyorsunuz.\n")
        
        elif secim == "3":
            para_cek = float(input("Çekmek istediğiniz miktar: "))
            if para_cek <= bakiye:
                bakiye -= para_cek
                print(f"Bankanızda kalan bakiye: {bakiye} TL\n")
                makbuz = input("Makbuz ister misiniz? (e/h): ").lower()
                if makbuz == "e":
                    print(f"--- MAKBUZ ---\nİşlem: Para Çekme\nMiktar: {para_cek} TL\nKalan Bakiye: {bakiye} TL\n----------------\n")
                else:
                    print("Uyarı!! Makbuz almayarak doğayı koruyorsunuz.\n")
            else:
                print("Yetersiz bakiye!\n")
        
        elif secim == "4":
            print(f"--- MAKBUZ ---\nKullanıcı: {kullanici_adi}\nMevcut Bakiye: {bakiye} TL\n----------------\n")
        
        elif secim == "5":
            print("Bankamızı kullandığınız için teşekkürler, çıkış yapılıyor...")
            break
        
        else:
            print("Geçersiz işlem!\n")
else:
    print("Hatalı PIN!")