import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Simple Calculator")
        master.geometry("300x400")

        self.total = tk.StringVar()
        self.total.set("")

        self.entry = tk.Entry(master, textvariable=self.total, justify="right", font=('Arial', 20))
        self.entry.grid(row=0, column=0, columnspan=4, pady=5, padx=5, sticky="nsew")

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', 'C', '+'
        ]

        row = 1
        col = 0
        for button in buttons:
            cmd = lambda x=button: self.click(x)
            tk.Button(master, text=button, command=cmd, height=2, width=5).grid(row=row, column=col, sticky="nsew")
            col += 1
            if col > 3:
                col = 0
                row += 1

        tk.Button(master, text="=", command=self.calculate, height=2, width=5).grid(row=row, column=col, sticky="nsew")

        # Configure grid
        for i in range(5):
            master.grid_rowconfigure(i, weight=1)
        for i in range(4):
            master.grid_columnconfigure(i, weight=1)

    def click(self, key):
        if key == 'C':
            self.total.set("")
        else:
            current = self.total.get()
            self.total.set(current + key)

    def calculate(self):
        try:
            result = eval(self.total.get())
            self.total.set(result)
        except:
            self.total.set("Error")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
