import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import ctypes as ct

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        master.geometry("400x520")

        self.expression = ""
        self.equation = tk.StringVar()

        # --- Displej ---
        self.display_frame = ttk.Frame(master, padding=(10, 10, 10, 0))
        self.display_frame.pack(fill=X)
        self.display = ttk.Entry(
            self.display_frame, 
            textvariable=self.equation, 
            font=('Segoe UI', 32),
            justify='right', 
            state='readonly'
        )
        self.display.pack(fill=X, expand=True, ipady=10)
        self.button_frame = ttk.Frame(master, padding=10)
        self.button_frame.pack(fill=BOTH, expand=True)

        buttons = [
            ('C', 1, 0, 'danger'), ('/', 1, 3, 'info'),
            ('7', 2, 0, 'secondary'), ('8', 2, 1, 'secondary'), ('9', 2, 2, 'secondary'), ('*', 2, 3, 'info'),
            ('4', 3, 0, 'secondary'), ('5', 3, 1, 'secondary'), ('6', 3, 2, 'secondary'), ('-', 3, 3, 'info'),
            ('1', 4, 0, 'secondary'), ('2', 4, 1, 'secondary'), ('3', 4, 2, 'secondary'), ('+', 4, 3, 'info'),
            ('0', 5, 0, 'secondary', 2), ('.', 5, 2, 'secondary'), ('=', 5, 3, 'success')
        ]

        for (text, row, col, style, *args) in buttons:
            colspan = args[0] if args else 1
            button = ttk.Button(
                self.button_frame, 
                text=text, 
                bootstyle=style, 
                command=lambda t=text: self.on_button_press(t)
            )
            button.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=3, pady=3)
        
        self.button_frame.grid_columnconfigure(1, weight=1)
        self.button_frame.grid_columnconfigure(2, weight=1)

        for i in range(6):
            self.button_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.button_frame.grid_columnconfigure(i, weight=1)

    def on_button_press(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '=':
            try:
                self.expression = self.expression.replace(',', '.')
                result = str(eval(self.expression))
                self.expression = result.replace('.', ',')
            except:
                self.expression = "Chyba"
        else:
            if self.expression == "Chyba":
                self.expression = ""
            self.expression += str(char)
        
        self.equation.set(self.expression.replace('.', ','))

    def dark_title_bar(window):
        window.update()
        DWMWA_USE_IMMERSIVE_DARK_MODE = 20
        set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
        get_parent = ct.windll.user32.GetParent
        hwnd = get_parent(window.winfo_id())
        rendering_policy = DWMWA_USE_IMMERSIVE_DARK_MODE
        value = 2
        value = ct.c_int(value)
        set_window_attribute(hwnd, rendering_policy, ct.byref(value),
        ct.sizeof(value))

if __name__ == "__main__":
    app = ttk.Window(themename="cyborg")
    
    app.style.theme_use(app.style.theme_names()[0])

    CalculatorApp(app)
    app.mainloop()