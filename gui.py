
import functions as xd
import FreeSimpleGUI as sg

yazi = sg.Text("Kadroya kimi ekleyeceğini yaz.")
gir = sg.InputText(tooltip="Oyuncu gir", key="oyuncu")
buton = sg.Button("Ekle")
list_box = sg.Listbox(values=xd.dosya_ac(), key="kadro", enable_events=True, size=(45, 10))
gitgel = sg.Button("Değiştir")
baybay = sg.Button("Çıkar")
destroy = sg.Button("Sıfırla")
run = sg.Button("Çık")

window = sg.Window("Kadrolama Programı",
                   layout=[[yazi], [gir, buton], [list_box, gitgel, baybay], [run, destroy]],
                   font=('Cuckoo', 20))

while True:
    olay, isim = window.read()
    print(olay)
    print(isim)
    match olay:
        case "Ekle":
            kadro = xd.dosya_ac()
            yeni = isim["oyuncu"]+"\n"
            kadro.append(yeni)
            xd.dosya_yaz(kadro)
            window["kadro"].update(kadro)
            window["oyuncu"].update("")
        case "Değiştir":
            try:
                gidici = isim["kadro"][0]
                gelici = isim["oyuncu"]+"\n"
                kadro = xd.dosya_ac()
                index = kadro.index(gidici)
                kadro[index] = gelici
                xd.dosya_yaz(kadro)
                window["kadro"].update(kadro)
            except IndexError:
                xd.error_pencere("Lütfen işlem yapacağınız oyuncunun üstüne tıklayın.")
        case "Çıkar":
            try:
                gidici = isim["kadro"][0]
                kadro = xd.dosya_ac()
                index = kadro.index(gidici)
                kadro.pop(index)
                xd.dosya_yaz(kadro)
                window["kadro"].update(kadro)
            except IndexError:
                xd.error_pencere("Lütfen işlem yapacağınız oyuncunun üstüne tıklayın.")
        case "kadro":
            try:
                window["oyuncu"].update(isim["kadro"][0])
            except IndexError:
                xd.error_pencere("Bir isim seçebilmek için listenizde en az bir isim olmalıdır!")
        case "Sıfırla":
            xd.dosya_yaz("")
            window["kadro"].update("")

        case "Çık":
            break
        case sg.WINDOW_CLOSED:
            break
window.close()
