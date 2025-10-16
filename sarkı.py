import sys
import time

lyrics_with_timing = [
    ("\033[31mİçerisi tam şampiyonlar ligi\033[0m", 0.3),
    ("\033[31mGalericiler\033[0m", 0.3),
    ("\033[31mPlantacılar\033[0m", 0.2),
    ("\033[31mBenim kalbimde korkular var\033[0m", 0.3),
    ("\033[31mMahsar vah sarı\033[0m", 0.3),
    ("\033[31mBenim ortamda kızlar hep tiki\033[0m", 0.3),
    ("\033[31mYüzüm orda yağmurlu tipi\033[0m", 0.3),
    ("\033[31mAh bebeğim uyandım gibi\033[0m", 0.3),
    ("\033[31mBiraz tipin dağılmış\033[0m", 0.3),
    ("\033[31mMahsar vah sarı\033[0m", 0.3),
    ("\033[31mYat esmer kızlar\033[0m", 0.3),
    ("\033[31mBabayı zor yarışlar\033[0m", 0.3),
    ("\033[31mTak Tak Tak kapıda kim var?\033[0m", 0.3),
    ("\033[31mŞu anda kutuplardayım\033[0m", 0.3),
    ("\033[31mTak Tak kapıda kim var?\033[0m", 0.3),
    ("\033[31mBulutlardayım\033[0m", 0.3)
]

for line, delay in lyrics_with_timing:
    for char in line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)
    print()
    time.sleep(delay)