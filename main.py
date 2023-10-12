import tkinter as tk
import splashscreen

def center_window(window):
    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - window.winfo_width()) // 2
    y = (screen_height - window.winfo_height()) // 2
    window.geometry("+{}+{}".format(x, y))

def main_app():
    main_window = tk.Tk()
    main_window.title("Lord of the Rings")
    main_window.geometry("1400x700")
    center_window(main_window)
    main_window.resizable(False, False)

    background_image = tk.PhotoImage(file="images/main_menu.png")

    background_label = tk.Label(main_window, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    font = ("Footlight MT Light", 16, 'bold')

    personage_kiezen = tk.Button(main_window, text="Personage kiezen", bg='lightgreen', width=55, height=2, borderwidth=4)
    personage_kiezen.place(x=325, y=175)
    personage_kiezen.config(font=font)

    personage_aanmaken = tk.Button(main_window, text="Personage aanmaken", bg='lightgreen', width=55, height=2, borderwidth=4)
    personage_aanmaken.place(x=325, y=275)
    personage_aanmaken.config(font=font)

    instellingen = tk.Button(main_window, text="Instellingen", bg='lightgreen', width=55, height=2, borderwidth=4)
    instellingen.place(x=325, y=375)
    instellingen.config(font=font)

    sluiten = tk.Button(main_window, text="Sluiten", command=lambda: knop_sluiten(main_window), bg='lightgreen',
                        width=55, height=2, borderwidth=4)
    sluiten.place(x=325, y=475)
    sluiten.config(font=font)

    main_window.mainloop()

if __name__ == "__main__":
    splashscreen.main()
    main_app()
