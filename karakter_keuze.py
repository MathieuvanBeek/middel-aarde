from tkinter import Tk, Label, Button, Frame
from scherm_1 import *

def maak_karakter_dict():
    with open("tekstbestand.txt") as bestand:
        verhaaldata = bestand.read()
    verhaaldata = verhaaldata.splitlines()
    export = []
    for line in verhaaldata:
        split_data = line.split(';;')
        verhaal_dict = {
            "naam": split_data[0],
            "ras": split_data[1],
            "beschrijving": split_data[2],
            "specialiteit": split_data[3],
            "foto": split_data[4]
        }
        export.append(verhaal_dict)
    return export


def kies_karakter(venster):

    karakter_data = maak_karakter_dict()
    for widget in venster.winfo_children():
        widget.destroy()

    knoppen_frame = Frame(venster)
    knoppen_frame.pack(expand=True)

    button_font = ("Helvetica", 12, "bold")

    button_1 = Button(knoppen_frame, text=karakter_data[0]['naam'], width=30, height=7, command=lambda: karakter_gekozen(venster, karakter_data[0]), font=button_font)
    button_2 = Button(knoppen_frame, text=karakter_data[1]['naam'], width=30, height=7, command=lambda: karakter_gekozen(venster, karakter_data[1]), font=button_font)
    button_3 = Button(knoppen_frame, text=karakter_data[2]['naam'], width=30, height=7, command=lambda: karakter_gekozen(venster, karakter_data[2]), font=button_font)

    button_1.pack(side="left", padx=10)
    button_2.pack(side="left", padx=10)
    button_3.pack(side="left", padx=10)

def test_star(venster):
    kies_karakter(venster)
    venster.geometry("600x600")
    venster.title("Karakter Kiezen")



venster = Tk()
test_star(venster)
venster.mainloop()
