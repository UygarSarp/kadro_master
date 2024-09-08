
import functions as xd
import FreeSimpleGUI as sg

yazi = sg.Text("Kadroya kimi ekleyeceğini yaz.")
gir = sg.InputText(key="oyuncu")
buton = sg.Button("Ekle")

window = sg.Window("Kadrolama Programı",layout=[[yazi],[gir,buton]], font=('Cuckoo',20))

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
        case sg.WINDOW_CLOSED:
            break
window.close()
