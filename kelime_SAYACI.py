from collections import Counter# ögelerin kaç kez geçtiğini sayar
metin = input("Bir metin giriniz: ")
kelimeler = metin.split()

# Harf sayısı (boşluklar hariç)
harf_sayisi = len(metin.replace(" ", ""))

# Kelime sayısı
kelime_sayisi = len(kelimeler)

# En çok geçen kelime
kelime_sayilari = Counter(kelimeler)
en_cok = kelime_sayilari.most_common(1)[0]  # en çok geçen 1 kelimeyi listeler

# Sonuçları yazdır
print(f"Toplam kelime sayısı: {kelime_sayisi}")
print(f"Toplam harf sayısı: {harf_sayisi}")
print(f"En çok geçen kelime: '{en_cok[0]}' ({en_cok[1]} kez)")
