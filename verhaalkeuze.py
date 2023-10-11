from tkinter import Label, Button, Tk


def maak_verhaal_dict(verhaal):
    with open(verhaal) as bestand:
        verhaaldata = bestand.read()
    verhaaldata = verhaaldata.splitlines()
    export = []
    for line in verhaaldata:
        split_data = line.split(';;')
        verhaal_dict = {
            'naam': split_data[0],
            'stap': split_data[1],
            'tekst_1': split_data[2],
            'plaatje_1': split_data[3],
            'tekst_2': split_data[4],
            'plaatje_2': split_data[5],
            'tekst_3': split_data[6],
            'plaatje_3': split_data[7],
            'eig_tekst': split_data[8],
            'eig_plaatje': split_data[9],
            'achtergrond': split_data[10],
            'keuze_1': split_data[11],
            'keuze_2': split_data[12],
            'keuze_3': split_data[13],
        }
        export.append(verhaal_dict)
    print(export)


def kies_verhaal(root, karakter):
    for widget in root.winfo_children():
        widget.destroy()
    instructie = Label(root, text='In welk verhaal wil je je verdiepen?')
    button_1 = Button(root, text='verhaal 1', command=lambda: maak_verhaal_dict('verhaal_1.txt'))
    button_2 = Button(root, text='verhaal 2', command=lambda: maak_verhaal_dict('verhaal_2.txt'))
    button_3 = Button(root, text='verhaal 3', command=lambda: maak_verhaal_dict('verhaal_3.txt'))

    instructie.pack()
    button_1.pack()
    button_2.pack()
    button_3.pack()

    root.mainloop()


def test_start():
    root = Tk()
    root.geometry('1400x700')
    kies_verhaal(root, 'frodo')


test_start()
