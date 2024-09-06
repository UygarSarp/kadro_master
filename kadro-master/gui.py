import functions as xd
import FreeSimpleGUI as sg

yazi = sg.Text("Kadroya kimi ekleyeceğini yaz.")
gir = sg.InputText("Kimi ekleyecen")
buton = sg.Button("Ekle")

window = sg.Window("Kadrolama Programı",layout=[[yazi],[gir,buton]])
window.read()
window.close()
