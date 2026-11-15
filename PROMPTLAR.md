# Yapay Zekâ ile Çalışma Günlüğü (PROMPTLAR.md)

**Araç:** Claude (Anthropic), claude.ai · **Tarih:** 12–15 Kasım 2026

Kodu Claude ile soru-cevap şeklinde geliştirdim. Bu günlük, süreçteki prompt'lardan seçtiğim 6 tanesini içerir. Her kayıtta: kullandığım prompt → YZ'nin yanıtı → kararım (Kabul / Düzenleme / Red) ve gerekçesi.

---

## Prompt 1 — Gereksinim kontrolü
**Prompt:** "Bu ödev gereksinimlerini maddeler halinde çıkar ve her birini kasa defterinde nasıl karşılarım, tablo yap."

**Yanıt:** 14 maddelik bir eşleştirme tablosu. Tablo bir açığı ortaya çıkardı: açıklama girdisi doğrulanmıyordu; boş bırakılınca raporda boş satır çıkıyordu.

**Kararım — Red:** Açıklama doğrulamasını eklemedim. Kodu kısa ve her satırını açıklayabileceğim halde tutmak istedim.

---

## Prompt 2 — Önce tasarım
**Prompt:** "Önce akış şeması/sözde kod ver; ben onaylayınca koda geçelim."

**Yanıt:** Kodu değiştirmeden iki seçeneğin sözde kodunu verdi: (A) açıklama boşsa uyarıp tekrar sor, (B) boşsa otomatik "-" yaz. A'nın gerçek doğrulama olduğunu, B'nin daha hızlı ama bilgi kaybına yol açtığını belirtti.

**Kararım — Red:** Mevcut kodun dışına çıkmamaya karar verdiğim için iki seçeneği de uygulamadım.

---

## Prompt 3 — Satır satır açıklama
**Prompt:** "Sadece kullanıcıdan pozitif sayı alan, hatalı girdide çökmeyen bir fonksiyon yaz. Her satırı yorumla."

**Yanıt:** Yeni fonksiyon yazmak yerine kodumdaki `sayi_al` fonksiyonunun her satırını açıkladı. Fonksiyondan çıkmanın tek yolunun `return` olduğunu, diğer bütün yolların tekrar `input`'a döndüğünü gösterdi.

**Kararım — Kabul:** Açıklamayı kodu anlamak için kullandım; kodun kendisi değişmedi.

---

## Prompt 4 — try/except ve continue
**Prompt:** "`try/except` burada tam olarak ne yapıyor? `continue` olmasa ne olurdu?"

**Yanıt:** `float()` çeviremediği girdide `ValueError` üretir; `except` bunu yakalar ve program çökmez. `continue` olmasaydı program alttaki `if sayi <= 0` satırına inerdi: ilk denemede `sayi` tanımsız olduğu için yine çökerdi, sonraki denemelerde eski değere göre yanlış uyarı verirdi.

**Kararım — Kabul:** Fonksiyonun neden çökmediğini artık kendi cümlelerimle açıklayabiliyorum.

---

## Prompt 5 — Kodu eleştirme
**Prompt:** "Yazdığın kodda hangi girdiler sorun çıkarabilir? Bana test senaryoları öner."

**Yanıt:** Kodu 14 uç girdiyle çalıştırdı ve kendi yazdığı kodda 6 sorun buldu. En ciddileri: `nan` ve `inf` tutar olarak kabul ediliyor ve raporu bozuyor ("Net sonuç: nan TL"). Diğerleri: boş açıklama, `0,001` (raporda 0.00 TL), `1e9` (1 milyar TL), uzun açıklamada hizalama bozulması. Dört düzeltme önerdi.

**Kararım — Red:** Önerilen dört düzeltmeyi uygulamadım. Teslimden önce kodu değiştirmek yerine sorunu bilinen bir sınırlama olarak belirtmeyi tercih ettim.

---

## Prompt 6 — Kendi testim
**Prompt:** "Tutar olarak 15o yazdım. Programın çökmemesini bekliyordum ve çökmedi."

**Yanıt:** Bunun bir hata değil, geçen bir test olduğunu söyledi: beklenen ile gerçek aynı. Hata raporu için beklenenle gerçeğin farklı olduğu bir girdi (örn. `nan`) denememi önerdi.

**Kararım — Kabul:** Test tablosundaki T2 satırını kendi bilgisayarımda doğrulamış oldum.
