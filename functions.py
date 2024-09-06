FILEPATH = "kadro.txt"

def dosya_ac(dosya_ad=FILEPATH):
    """ Kadro dosyasını açmaya yarar. """
    with open(dosya_ad, 'r') as dosya_local:
        kadro_local = dosya_local.readlines()
    return kadro_local

def dosya_yaz(eklenecek,dosya_adi=FILEPATH):
    with open(dosya_adi, 'w') as dosya:
        dosya.writelines(eklenecek)


if __name__ == "__main__":
    print("Çet noluyoooo")
