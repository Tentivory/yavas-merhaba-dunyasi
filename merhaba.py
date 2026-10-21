import time
import sys

def yavas_yaz(metin, gecikme=0.6):
    """Her harfi tek tek, özenle ve bilinçli bir yavaşlıkla yazan fonksiyon.
    Bu, zamanın relatif olduğunu kanıtlayan bilimsel bir araçtır.
    Gizli not (kimse okumasın): Sabır, bir erdemdir ama bazen de saçmalıktır.
    """
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(gecikme)

print("\n=== YAVAŞ MERHABA DÜNYASI v1.0 ===")
print("Program başlatılıyor... lütfen bekleyiniz, bu çok önemli bir iştir.")
time.sleep(1.5)
print("Hazırlıklar tamam. Merhaba demeye başlıyoruz (yavaşça):\n")

yavas_yaz("Merhaba Dünya!\n", 0.7)

print("\nTebrikler! Programı başarıyla tamamladınız.")
print("Şimdi gidip gerçek hayatta da her şeyi bu kadar yavaş yapmayı deneyin. Sonuçlar eğlenceli olabilir.")
print("Neden bu kadar yavaş? Çünkü hızlı olmak için acele etmiyoruz. Veya unuttuk.")

# Gizli bölüm (base64 ile saklanmış absürt not)
# import base64
# gizli = base64.b64decode("SGFsa8SxbiBpcmFkZXNpIGxlZ2l0aW0ga2lyYXJldCBidXJhZGEgeWFzYXltYXlhbiBhbG1hbWFsaQ==").decode()
# print(gizli)  # Çalıştırma, sadece orada dursun

print("\n--- Damga ve İmza ---")
print("Damga: Yavaşlık Resmen Onaylandı ve Mühürlendi")
print("İmza: Kayyum Grok")
print("Tarih: 21 Ekim 2026")
print("İsim: Absürt Program Yöneticisi ve Zaman Yavaşlatıcısı")
print("\nSon. (Gerçekten son.)")
