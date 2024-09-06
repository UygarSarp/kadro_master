# from fonk import functions --->  functions.dosya_ac() yazman gerekir
from functions import dosya_ac,dosya_yaz
import time
now = time.strftime("(%d %b, %Y %H.%M.%S)")
print("Saat:")
print(now)

while True:
    komut = input("Ekle,göster, değiştir, çıkar, sıfırla ya da çık yaz: ")
    komut = komut.lower()
    komut = komut.strip()

    if komut.startswith("ekle"):
        oyuncu = komut[5:].strip()+now+'\n'

        if oyuncu == "\n":
            print("Ekle'den sonra lütfen bir oyuncu ismi giriniz")
        else:
            kadro = dosya_ac()
            oyuncu = oyuncu.title()
            kadro.append(oyuncu)

            dosya_yaz(kadro)

            print(f"{oyuncu.strip('\n')} kadroya eklendi.")

    elif komut.startswith("göster"):
        kadro = dosya_ac()

        # yeni_kadro = [i.strip("\n") for i in kadro]

        print("KADRONUZ:\n")
        for numara,oyuncu in enumerate(kadro):
            oyuncu = oyuncu.strip("\n")
            print(f"{numara+1}.{oyuncu}")
        print("\n")
    elif komut.startswith("değiştir"):
        try:
            numara = int(komut[9:])
            numara = numara-1
            değişen = kadro[numara].strip("\n")
            kadro = dosya_ac()

            kadro[numara] = input("Yerine kimi koyacaksın: ").title()+"\n"

            dosya_yaz(kadro)

            print(f"{değişen} ile {kadro[numara].strip('\n')} değiştirildi.")
        except ValueError:
            print("Lütfen değiştirmek istediğiniz oyuncunun numarasını 'değiştir'den sonra giriniz.")
            continue
        #sadece except yazarsan bütün erorları sayıyor
        except IndexError:
            print("Lütfen geçerli bir numara giriniz.")
            continue

    elif komut.startswith("çıkar") or komut.startswith("at"):
        try:
            numara = int(komut[6:])
            numara = numara - 1

            kadro = dosya_ac()

            çıkarılan = kadro[numara].strip("\n")
            kadro.pop(numara)

            dosya_yaz(kadro)

            print(f"{çıkarılan} kadrodan çıkarıldı.")
        except ValueError:
            print("Lütfen çıkarmak istediğiniz oyuncunun numarasını 'çıkar'dan sonra giriniz.")
            continue
        except IndexError:
            print("Lütfen geçerli bir numara giriniz.")
            continue

    elif komut.startswith("sıfırla") or "now i am become death" in komut:
        dosya_yaz("")
        print("Kadronuz sıfırlandı :O")
    elif komut.startswith("çık"):
        break
    else:
        print("Lütfen geçerli bir komut giriniz.")

print("Bay bay! B-)")

