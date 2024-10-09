import tkinter as tk
import math

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Advanced Calculator")
        master.geometry("400x500")
        master.configure(bg='#f0f0f0')

        self.total = tk.StringVar()
        self.total.set("")

        self.entry = tk.Entry(master, textvariable=self.total, justify="right", font=('Arial', 24), bd=5, relief=tk.SUNKEN)
        self.entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10, sticky="nsew")

        buttons = [
            ('C', '#ff9999'), ('(', '#cccccc'), (')', '#cccccc'), ('/', '#ffcc99'),
            ('7', '#ffffff'), ('8', '#ffffff'), ('9', '#ffffff'), ('*', '#ffcc99'),
            ('4', '#ffffff'), ('5', '#ffffff'), ('6', '#ffffff'), ('-', '#ffcc99'),
            ('1', '#ffffff'), ('2', '#ffffff'), ('3', '#ffffff'), ('+', '#ffcc99'),
            ('0', '#ffffff'), ('.', '#ffffff'), ('±', '#cccccc'), ('=', '#99ccff')
        ]

        row = 1
        col = 0
        for (text, color) in buttons:
            cmd = lambda x=text: self.click(x)
            tk.Button(master, text=text, command=cmd, height=2, width=5, font=('Arial', 18), bg=color).grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
            col += 1
            if col > 3:
                col = 0
                row += 1

        # Advanced operations
        advanced_buttons = [
            ('sqrt', '√'), ('pow', 'x²'), ('sin', 'sin'), ('cos', 'cos')
        ]

        for (operation, text) in advanced_buttons:
            cmd = lambda x=operation: self.advanced_operation(x)
            tk.Button(master, text=text, command=cmd, height=2, width=5, font=('Arial', 16), bg='#ccccff').grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
            col += 1

        # Configure grid
        for i in range(6):
            master.grid_rowconfigure(i, weight=1)
        for i in range(4):
            master.grid_columnconfigure(i, weight=1)

    def click(self, key):
        if key == 'C':
            self.total.set("")
        elif key == '=':
            try:
                result = eval(self.total.get())
                self.total.set(result)
            except:
                self.total.set("Error")
        elif key == '±':
            try:
                if self.total.get()[0] == '-':
                    self.total.set(self.total.get()[1:])
                else:
                    self.total.set('-' + self.total.get())
            except IndexError:
                pass
        else:
            current = self.total.get()
            self.total.set(current + key)

    def advanced_operation(self, operation):
        try:
            value = float(self.total.get())
            if operation == 'sqrt':
                result = math.sqrt(value)
            elif operation == 'pow':
                result = value ** 2
            elif operation == 'sin':
                result = math.sin(math.radians(value))
            elif operation == 'cos':
                result = math.cos(math.radians(value))
            self.total.set(result)
        except:
            self.total.set("Error")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
