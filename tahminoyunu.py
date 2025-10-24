import random

def sayi_tahminoyunu():
    print("Sayı tahmin oyununa hoşgeldiniz!")
    print("Bilgisayar 1 ile 50 arasında sayı seçecek.")
    
    rastgele_sayi = random.randint(1, 50)
    tahmin_hakki = 5

    while tahmin_hakki > 0:
        try:
            tahmin = int(input("Lütfen bir sayı tahmin ediniz: "))

            if tahmin < 1 or tahmin > 50:
                print("Lütfen 1 ile 50 arasında sayı giriniz.")
                continue

            if tahmin == rastgele_sayi:
                print(f"Tebrikler! Sayıyı doğru bildiniz: {rastgele_sayi}")
                break
            elif tahmin < rastgele_sayi:
                print("Daha büyük bir sayı deneyiniz.")
            else:
                print("Daha küçük bir sayı deneyiniz.")

            tahmin_hakki -= 1
            print(f"Kalan tahmin hakkınız: {tahmin_hakki}\n")

        except ValueError:
            print("Lütfen geçerli bir sayı giriniz.")

    if tahmin_hakki == 0:
        print(f"Maalesef tahmin hakkınız bitti. Doğru sayı: {rastgele_sayi}")

sayi_tahminoyunu()