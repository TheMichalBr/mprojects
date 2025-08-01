import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.ttk import Style
import os

class Notepad(tk.Tk):
    def __init__(self):
        super().__init__()
        Style().theme_use("clam")

        self.title("Poznámkový blok")
        self.geometry("900x500")
        self.current_file = None
        self.file_modified = False
        self.night_mode = False

        self.create_widgets()
        self.create_menu()
        self.bind_events()

    def create_widgets(self):
        self.text = tk.Text(self, wrap="word", font=("Consolas", 12), undo=True)
        self.text.pack(expand=True, fill='both', padx=2, pady=2)

        self.scrollbar = tk.Scrollbar(self.text, command=self.text.yview)
        self.text.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def create_menu(self):
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Nový", command=self.new_file)
        filemenu.add_command(label="Otevřít", command=self.open_file)
        filemenu.add_command(label="Uložit", command=self.save_file)
        filemenu.add_command(label="Uložit jako", command=self.save_file_as)
        filemenu.add_separator()
        filemenu.add_command(label="Noční režim", command=self.night_mode_toggle)
        filemenu.add_separator()
        filemenu.add_command(label="Ukončit", command=self.exit_program)

        menubar.add_cascade(label="Soubor", menu=filemenu)

    def bind_events(self):
        self.text.bind("<<Modified>>", self.on_modified)

    def on_modified(self, event=None):
        self.file_modified = self.text.edit_modified()
        self.text.edit_modified(False)
        self.update_title()

    def update_title(self):
        filename = os.path.basename(self.current_file) if self.current_file else "Bez názvu"
        mod = "*" if self.file_modified else ""
        self.title(f"{mod}{filename} - Poznámkový blok")

    def new_file(self):
        if self.confirm_save_changes():
            self.text.delete(1.0, tk.END)
            self.current_file = None
            self.file_modified = False
            self.update_title()

    def open_file(self):
        if self.confirm_save_changes():
            path = filedialog.askopenfilename(filetypes=[("Textové soubory", "*.txt"), ("Všechny soubory", "*.*")])
            if path:
                with open(path, "r", encoding="utf-8") as file:
                    content = file.read()
                self.text.delete(1.0, tk.END)
                self.text.insert(tk.END, content)
                self.current_file = path
                self.file_modified = False
                self.update_title()

    def save_file(self):
        if self.current_file:
            content = self.text.get(1.0, tk.END)
            with open(self.current_file, "w", encoding="utf-8") as file:
                file.write(content)
            self.file_modified = False
            self.update_title()
        else:
            self.save_file_as()

    def save_file_as(self):
        path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Textové soubory", "*.txt"), ("Všechny soubory", "*.*")])
        if path:
            self.current_file = path
            self.save_file()

    def night_mode_toggle(self):
        self.night_mode = not self.night_mode
        bg = "#1e1e1e" if self.night_mode else "white"
        fg = "white" if self.night_mode else "black"
        insert_bg = "white" if self.night_mode else "black"
        self.text.configure(bg=bg, fg=fg, insertbackground=insert_bg)

    def confirm_save_changes(self):
        if self.file_modified:
            result = messagebox.askyesnocancel("Uložit změny?", "Chcete uložit změny před pokračováním?")
            if result:  # Ano
                self.save_file()
                return True
            elif result is None:  # Zrušit
                return False
        return True

    def exit_program(self):
        if self.confirm_save_changes():
            self.destroy()

if __name__ == "__main__":
    app = Notepad()
    app.mainloop()
