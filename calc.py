import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("tkinter Calculator")

        self.current_input = ""
        self.result = 0
        self.current_operation = None

        self.display = tk.Entry(root, width=35, borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.create_buttons()

    def create_buttons(self):
        # Button creation and placement
        buttons = [
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('/', 3, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('-', 1, 3),
            ('0', 4, 0), ('C', 4, 1), ('+', 4, 3),  
            ('=', 6, 1)
        ]
        for (text, row, col) in buttons:
            if text == '=':
                btn = tk.Button(self.root, text=text, fg='#fff', bg='#007fff', padx=90, pady=20, command=self.evaluate)
            elif text == 'C':
                btn = tk.Button(self.root, text=text, fg='#fff', bg='#ff7f7f', padx=90, pady=20, command=self.clear)
            else:
                btn = tk.Button(self.root, text=text, padx=40, pady=20, command=lambda x=text: self.on_click(x))
            btn.grid(row=row, column=col, columnspan=2 if text in ['C', '='] else 1)

    def on_click(self, char):
        if char in '+-*/':
            self.result = float(self.display.get()) if self.display.get() else 0
            self.current_operation = char
            self.current_input = ""
        else:
            self.current_input += str(char)
        self.update_display(self.current_input)

    def evaluate(self):
        if self.current_operation:
            try:
                num2 = float(self.display.get())
                if self.current_operation == '+':
                    self.result += num2
                elif self.current_operation == '-':
                    self.result -= num2
                elif self.current_operation == '*':
                    self.result *= num2
                elif self.current_operation == '/':
                    if num2 != 0:
                        self.result /= num2
                    else:
                        self.result = "Error"
                self.update_display(str(self.result))
                self.current_input = ""
                self.current_operation = None
            except ValueError:
                self.clear()
                self.update_display("Error")

    def clear(self):
        self.current_input = ""
        self.result = 0
        self.current_operation = None
        self.update_display("0")

    def update_display(self, value):
        self.display.delete(0, tk.END)
        self.display.insert(0, value)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
