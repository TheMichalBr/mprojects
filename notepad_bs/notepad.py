import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import filedialog, messagebox
import os

class Notepad(tb.Window):
    def __init__(self):
        super().__init__(themename="darkly")  # nebo "litera", "cosmo", "superhero", atd.

        self.title("📝 Moderní Notepad")
        self.geometry("1000x600")
        self.current_file = None
        self.file_modified = False

        self.create_widgets()
        self.create_menu()
        self.bind_events()
        self.update_title()

    def create_widgets(self):
        self.text = tb.Text(
            self,
            wrap="word",
            font=("Consolas", 12),
            undo=True,
            background="#1e1e2e",
            foreground="#ffffff",
            insertbackground="white",
            selectbackground="#44475a",
            relief="flat",
            borderwidth=0
        )
        self.text.pack(expand=True, fill=BOTH, padx=15, pady=15)

        self.scrollbar = tb.Scrollbar(self.text, command=self.text.yview, bootstyle="secondary-round")
        self.text.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=RIGHT, fill=Y)

    def create_menu(self):
        menubar = tb.Menu(self)
        filemenu = tb.Menu(menubar, tearoff=0)

        filemenu.add_command(label="Nový", command=self.new_file)
        filemenu.add_command(label="Otevřít", command=self.open_file)
        filemenu.add_command(label="Uložit", command=self.save_file)
        filemenu.add_command(label="Uložit jako", command=self.save_file_as)
        filemenu.add_separator()
        filemenu.add_command(label="Přepnout režim", command=self.toggle_theme)
        filemenu.add_separator()
        filemenu.add_command(label="Zavřít", command=self.exit_program)

        menubar.add_cascade(label="Soubor", menu=filemenu)
        self.config(menu=menubar)

    def bind_events(self):
        self.text.bind("<<Modified>>", self.on_modified)

    def on_modified(self, event=None):
        self.file_modified = self.text.edit_modified()
        self.text.edit_modified(False)
        self.update_title()

    def update_title(self):
        name = os.path.basename(self.current_file) if self.current_file else "Bez názvu"
        star = "*" if self.file_modified else ""
        self.title(f"{star}{name} - Moderní Notepad")

    def new_file(self):
        if self.confirm_save_changes():
            self.text.delete(1.0, "end")
            self.current_file = None
            self.file_modified = False
            self.update_title()

    def open_file(self):
        if self.confirm_save_changes():
            path = filedialog.askopenfilename(filetypes=[("Textové soubory", "*.txt"), ("Všechny soubory", "*.*")])
            if path:
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                self.text.delete(1.0, "end")
                self.text.insert("end", content)
                self.current_file = path
                self.file_modified = False
                self.update_title()

    def save_file(self):
        if self.current_file:
            with open(self.current_file, "w", encoding="utf-8") as f:
                f.write(self.text.get(1.0, "end"))
            self.file_modified = False
            self.update_title()
        else:
            self.save_file_as()

    def save_file_as(self):
        path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Textové soubory", "*.txt"), ("Všechny soubory", "*.*")])
        if path:
            self.current_file = path
            self.save_file()

    def confirm_save_changes(self):
        if self.file_modified:
            result = messagebox.askyesnocancel("Uložit změny?", "Chcete uložit změny před pokračováním?")
            if result:  # Ano
                self.save_file()
                return True
            elif result is None:  # Zrušit
                return False
        return True

    def toggle_theme(self):
        current = self.style.theme.name
        new_theme = "litera" if current == "darkly" else "darkly"
        self.style.theme_use(new_theme)

    def exit_program(self):
        if self.confirm_save_changes():
            self.destroy()

if __name__ == "__main__":
    Notepad().mainloop()
