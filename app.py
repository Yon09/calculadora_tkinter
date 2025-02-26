import tkinter as tk

# Función para actualizar la pantalla
def click(boton):
    actual = pantalla.get()
    pantalla.delete(0, tk.END)
    pantalla.insert(tk.END, actual + str(boton))

# Función para calcular el resultado
def calcular():
    try:
        resultado = eval(pantalla.get())
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, resultado)
    except:
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, "Error")

# Función para borrar la pantalla
def borrar():
    pantalla.delete(0, tk.END)

# Crear ventana
root = tk.Tk()
root.title("Calculadora")
root.geometry("300x400")

# Campo de texto
pantalla = tk.Entry(root, font=("Arial", 20), justify="right")
pantalla.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8)

# Botones
botones = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+')
]

for fila, valores in enumerate(botones, 1):
    for col, valor in enumerate(valores):
        if valor == "=":
            btn = tk.Button(root, text=valor, font=("Arial", 16), width=5, height=2, command=calcular)
        else:
            btn = tk.Button(root, text=valor, font=("Arial", 16), width=5, height=2, command=lambda v=valor: click(v))
        btn.grid(row=fila, column=col, padx=5, pady=5)

# Botón de borrar
btn_borrar = tk.Button(root, text="C", font=("Arial", 16), width=5, height=2, command=borrar)
btn_borrar.grid(row=4, column=3, padx=5, pady=5)

# Ejecutar la app
root.mainloop()
