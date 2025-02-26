import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("Mi primera app con Tkinter")
root.geometry("300x200")  # Tamaño de la ventana (ancho x alto)

# Crear un label (texto)
label = tk.Label(root, text="¡Hola, Tkinter!", font=("Arial", 14))
label.pack(pady=10)  # Añadir espaciado vertical

# Crear un botón
def click():
    label.config(text="¡Botón presionado!")

boton = tk.Button(root, text="Haz clic", command=click)
boton.pack()

# Iniciar la aplicación
root.mainloop()
