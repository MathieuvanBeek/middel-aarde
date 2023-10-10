import tkinter as tk
from tkinter import *


def edit_text(label, tekst):
    label['text'] = tekst


def main():
    def on_new():
        pass

    def on_open():
        pass

    def on_save():
        pass

    def on_exit():
        root.quit()

    root = tk.Tk()
    root.title("main menu")
    root.geometry('600x400')

    menu_bar = Menu(root)
    root.config(menu=menu_bar)

    file_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Bestand", menu=file_menu)
    file_menu.add_command(label="Nieuw", command=on_new)
    file_menu.add_command(label="Openen", command=on_open)
    file_menu.add_command(label="Opslaan", command=on_save)
    file_menu.add_separator()
    file_menu.add_command(label="Afsluiten", command=on_exit)

    edit_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Bewerken", menu=edit_menu)

    textlabel = Label(root, text='')
    knop = Button(root, text='button', command=lambda: edit_text(textlabel, 'funny'))

    knop.pack()
    textlabel.pack()

    root.mainloop()


if __name__ == '__main__':
    main()
