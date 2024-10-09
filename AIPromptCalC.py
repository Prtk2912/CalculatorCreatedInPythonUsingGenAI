import tkinter as tk
from tkinter import StringVar
import math

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("350x300")
        self.resizable(False, False)

        # Create display area
        self.display_var = StringVar()
        self.display_entry = tk.Entry(self, textvariable=self.display_var, justify='right', font=('Arial', 24), relief='sunken')
        self.display_entry.grid(row=0, column=0, columnspan=6, padx=5, pady=5)

        # Button colors
        button_colors = {
            'digits': '#FFFFFF',
            'equals': '#E6F3FF',
            'clear': '#FFE6E6',
            'basic_ops': '#FFE6CC',
            'advanced_ops': '#E6E6FF',
            'other': '#E6E6E6'
        }

        # Create buttons
        buttons = [
            ['(', ')', 'C', '=', '±', '√'],
            ['7', '8', '9', '/', '*', 'x²'],
            ['4', '5', '6', '-', '+', 'sin'],
            ['1', '2', '3', '*', '/', 'cos'],
            ['0', '.', '=', '-', '+', '']
        ]

        row_val = 1
        col_val = 0

        for row in buttons:
            for button in row:
                if button == '':
                    col_val += 1
                    continue
                elif button == '=':
                    self.create_button(button, lambda b=button: self.click(b), button_colors['equals'], row_val, col_val)
                elif button == 'C':
                    self.create_button(button, self.clear, button_colors['clear'], row_val, col_val)
                elif button in ['+', '-', '*', '/']:
                    self.create_button(button, lambda b=button: self.click(b), button_colors['basic_ops'], row_val, col_val)
                elif button in ['√', 'x²', 'sin', 'cos']:
                    self.create_button(button, lambda b=button: self.advanced_operation(b), button_colors['advanced_ops'], row_val, col_val)
                elif button == '±':
                    self.create_button(button, self.toggle_sign, button_colors['other'], row_val, col_val)
                else:
                    self.create_button(button, lambda b=button: self.click(b), button_colors['digits'], row_val, col_val)

                col_val += 1
                if col_val > 5:
                    col_val = 0
                    row_val += 1

    def create_button(self, text, command, color, row_val, col_val):
        tk.Button(self, text=text, command=command, bg=color).grid(row=row_val, column=col_val, padx=5, pady=5)

    def click(self, button):
        current_value = self.display_var.get()
        if button == '=':
            try:
                result = str(eval(current_value))
                self.display_var.set(result)
            except Exception as e:
                self.display_var.set("Error")
        else:
            new_value = current_value + str(button)
            self.display_var.set(new_value)

    def calculate(self):
        try:
            result = str(eval(self.display_var.get()))
            self.display_var.set(result)
        except Exception as e:
            self.display_var.set("Error")

    def clear(self):
        self.display_var.set("")

    def toggle_sign(self):
        current_value = self.display_var.get()
        if current_value.startswith('-'):
            new_value = current_value[1:]
        else:
            new_value = '-' + current_value
        self.display_var.set(new_value)

    def advanced_operation(self, operation):
        current_value = self.display_var.get()
        try:
            if operation == '√':
                result = str(math.sqrt(float(current_value)))
            elif operation == 'x²':
                result = str(float(current_value) ** 2)
            elif operation == 'sin':
                result = str(math.sin(math.radians(float(current_value))))
            elif operation == 'cos':
                result = str(math.cos(math.radians(float(current_value))))
            self.display_var.set(result)
        except Exception as e:
            self.display_var.set("Error")

    def run(self):
        self.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()