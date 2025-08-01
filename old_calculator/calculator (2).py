import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import StringVar

class Kalkulacka(ttk.Window):
    def __init__(self):
        super().__init__(title="Kalkulačka", themename="darkly", size=(300, 400))
        self.resizable(False, False)
        
        self.vyraz = StringVar()

        # Display
        entry = ttk.Entry(self, textvariable=self.vyraz, font=("Segoe UI", 18), justify="right")
        entry.pack(fill=X, padx=10, pady=20, ipady=10)

        # Tlačítka
        btns = [
            ("7", "8", "9", "/"),
            ("4", "5", "6", "*"),
            ("1", "2", "3", "-"),
            ("0", ".", "=", "+"),
            ("C",),
        ]

        for radek in btns:
            frame = ttk.Frame(self)
            frame.pack(padx=10, pady=5, fill=X)
            for tl in radek:
                ttk.Button(
                    frame,
                    text=tl,
                    bootstyle="info" if tl not in ("=", "C") else ("success" if tl == "=" else "danger"),
                    width=6,
                    command=lambda t=tl: self.zpracuj(t)
                ).pack(side=LEFT, expand=True, fill=X, padx=2)

    def zpracuj(self, tl):
        if tl == "C":
            self.vyraz.set("")
        elif tl == "=":
            try:
                vysledek = eval(self.vyraz.get())
                self.vyraz.set(str(vysledek))
            except:
                self.vyraz.set("Chyba")
        else:
            self.vyraz.set(self.vyraz.get() + tl)

if __name__ == "__main__":
    app = Kalkulacka()
    app.mainloop()