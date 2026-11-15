# Kasa Defteri - GEP1316 Ödev 1 - Mevlüt Furkan Yılmaz
# Bir kafenin günlük gelir ve giderlerini kaydeder.

islemler = []  # her işlem bir sözlük: {"tur": ..., "tutar": ..., "aciklama": ...}


def sayi_al(mesaj):
    """Geçerli bir tutar girilene kadar tekrar sorar."""
    while True:
        girdi = input(mesaj)
        if "." in girdi:                           # 1.000 sessizce 1 olarak okunmasın
            print("! Nokta kullanmayın. Kuruş için virgül yazın (örnek: 1000 veya 150,50).")
            continue
        girdi = girdi.replace(",", ".")            # 150,50 -> 150.50
        try:
            sayi = float(girdi)
        except ValueError:
            print("! Lütfen sadece sayı girin (örnek: 150 veya 150,50).")
            continue
        if sayi <= 0:
            print("! Tutar 0'dan büyük olmalı.")
        else:
            return sayi


def islem_ekle(tur):
    """Kullanıcıdan tutar ve açıklama alıp listeye bir sözlük ekler."""
    tutar = sayi_al("Tutar (TL): ")
    aciklama = input("Açıklama: ")
    islemler.append({"tur": tur, "tutar": tutar, "aciklama": aciklama})
    print("✓ Kaydedildi.")


def rapor_olustur():
    """Gün sonu raporunu hazırlar: toplamlar, net sonuç, kâr/zarar."""
    toplam_gelir = 0
    toplam_gider = 0
    for islem in islemler:                 # listedeki her işleme tek tek bak
        if islem["tur"] == "gelir":
            toplam_gelir += islem["tutar"]
        else:
            toplam_gider += islem["tutar"]

    net = toplam_gelir - toplam_gider
    if net > 0:
        sonuc = "KÂR"
    elif net < 0:
        sonuc = "ZARAR"
    else:
        sonuc = "BAŞABAŞ"

    rapor = "------ GÜN SONU RAPORU ------\n"
    for islem in islemler:
        rapor += f"{islem['tur']:<6} {islem['aciklama']:<15} {islem['tutar']:>9.2f} TL\n"
    rapor += f"Toplam gelir : {toplam_gelir:.2f} TL\n"
    rapor += f"Toplam gider : {toplam_gider:.2f} TL\n"
    rapor += f"Net sonuç    : {net:.2f} TL ({sonuc})\n"
    return rapor


def dosyaya_kaydet(rapor):
    """Raporu kasa_raporu.txt dosyasına yazar (eski içeriğin üzerine)."""
    with open("kasa_raporu.txt", "w", encoding="utf-8") as dosya:
        dosya.write(rapor)
    print("✓ Rapor kasa_raporu.txt dosyasına kaydedildi.")


# Ana menü
while True:
    print("\n1) Gelir ekle  2) Gider ekle  3) Rapor  4) Çıkış")
    secim = input("Seçiminiz: ")
    if secim == "1":
        islem_ekle("gelir")
    elif secim == "2":
        islem_ekle("gider")
    elif secim == "3":
        rapor = rapor_olustur()
        print(rapor)
        dosyaya_kaydet(rapor)
    elif secim == "4":
        break
    else:
        print("! 1-4 arası bir sayı girin.")
