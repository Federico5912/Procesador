import tkinter as tk
from tkinter import scrolledtext
import math

# Funciones seguras que permitimos evaluar
safe_math = {
    "abs": abs,
    "round": round,
    "min": min,
    "max": max,
    "pow": pow,
    "sqrt": math.sqrt,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "log": math.log,
    "log10": math.log10,
    "exp": math.exp,
    "pi": math.pi,
    "e": math.e,
    "floor": math.floor,
    "ceil": math.ceil,
    "factorial": math.factorial,
    "degrees": math.degrees,
    "radians": math.radians
}

def process_math_input(expr_str: str):
    try:
        result = eval(expr_str, {"__builtins__": {}}, safe_math)
        return result
    except Exception as e:
        return f"Error: {str(e)}"

class MathProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini Procesador Matemático (sin SymPy)")

        self.input_label = tk.Label(root, text="Escribe una expresión matemática:")
        self.input_label.pack(pady=(10, 0))

        self.input_text = tk.Entry(root, font=("Courier", 14), width=60)
        self.input_text.pack(pady=(5, 10))
        self.input_text.bind("<Return>", self.process_input)

        self.process_button = tk.Button(root, text="Procesar", command=self.process_input)
        self.process_button.pack()

        self.output_label = tk.Label(root, text="Resultado:")
        self.output_label.pack(pady=(20, 0))

        self.output_text = scrolledtext.ScrolledText(root, font=("Courier", 14), height=10, width=80, wrap=tk.WORD)
        self.output_text.pack(pady=(5, 10))
        self.output_text.config(state=tk.DISABLED)

    def process_input(self, event=None):
        expr = self.input_text.get()
        result = process_math_input(expr)

        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, str(result))
        self.output_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = MathProcessorApp(root)
    root.mainloop()
