import tkinter as tk

# Función para actualizar la pantalla
def click(boton):
    if pantalla.get() == "0":
        pantalla.delete(0, tk.END)
    pantalla.insert(tk.END, str(boton))

# Función para calcular el resultado
def calcular():
    try:
        resultado = eval(pantalla.get().replace("X", "*"))  # Reemplazar X por *
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, resultado)
    except:
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, "Error")

# Función para borrar la pantalla completamente
def borrar_todo():
    pantalla.delete(0, tk.END)
    pantalla.insert(0, "0")

# Función para borrar solo un dígito
def borrar_uno():
    contenido = pantalla.get()
    if len(contenido) > 1:
        pantalla.delete(len(contenido) - 1, tk.END)
    else:
        pantalla.delete(0, tk.END)
        pantalla.insert(0, "0")

# Función para borrar un número completo (cadena de dígitos)
def borrar_numero():
    contenido = pantalla.get()
    if contenido == "0":
        return
    
    nuevo_contenido = contenido.rstrip("0123456789.")  # Elimina solo números y punto decimal
    pantalla.delete(0, tk.END)
    pantalla.insert(0, nuevo_contenido if nuevo_contenido else "0")

# Función para cambiar el signo del número actual
def cambiar_signo():
    contenido = pantalla.get()
    if contenido in ["", "0", "Error"]:
        return
    try:
        if " " in contenido:
            partes = contenido.split(" ")
            partes[-1] = str(-float(partes[-1]))  
            pantalla.delete(0, tk.END)
            pantalla.insert(tk.END, " ".join(partes))
        else:
            pantalla.delete(0, tk.END)
            pantalla.insert(tk.END, str(-float(contenido)))
    except:
        pantalla.delete(0, tk.END)
        pantalla.insert(0, "Error")

# Función para manejar las teclas del teclado físico y el teclado numérico
def manejar_tecla(event):
    tecla = event.keysym  

    numpad = {  
        "KP_0": "0", "KP_1": "1", "KP_2": "2", "KP_3": "3", "KP_4": "4",
        "KP_5": "5", "KP_6": "6", "KP_7": "7", "KP_8": "8", "KP_9": "9",
        "KP_Decimal": ".", "KP_Add": "+", "KP_Subtract": "-", 
        "KP_Multiply": "*", "KP_Divide": "/"
    }

    if tecla.isdigit() or tecla in numpad:  
        click(numpad.get(tecla, tecla))
    elif tecla in ["plus", "minus", "asterisk", "slash"]:  
        operadores = { "plus": "+", "minus": "-", "asterisk": "*", "slash": "/" }
        click(operadores[tecla])
    elif tecla in ["Return", "KP_Enter"]:  
        calcular()
    elif tecla == "BackSpace":
        if event.state & 4:  # Shift + Backspace → Borra todo
            borrar_todo()
        elif event.state & 1:  # Control + Backspace → Borra un número completo
            borrar_numero()
        else:  # Solo Backspace → Borra un dígito
            borrar_uno()
    elif tecla in ["period", "KP_Decimal"]:  
        click(".")
    elif tecla == "Escape":  
        root.quit()

# Crear ventana
root = tk.Tk()
root.title("Calculadora")
root.geometry("350x450")
root.resizable(False, False)

# Estilos de los botones
boton_estilo = {"font": ("Arial", 16), "width": 5, "height": 2, "bd": 2, "relief": "ridge"}

# Campo de texto
pantalla = tk.Entry(root, font=("Arial", 24), justify="right", bd=5, relief="sunken")
pantalla.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=10, pady=10, padx=5)
pantalla.insert(0, "0")

# Configuración de botones con colores
botones = [
    ('7', '8', '9', '/'),  
    ('4', '5', '6', 'X'),  
    ('1', '2', '3', '-'),  
    ('+/-', '0', '.', '+')
]

colores = {
    "numeros": "#86B049",  
    "operadores": "#24B0D9",  
    "especiales": "#F3A81F",  
    "borrar": "#E0452D",  
    "borrar_todo": "#D9534F",  
    "igual": "#24B0D9"  
}

for fila, valores in enumerate(botones, 1):
    for col, valor in enumerate(valores):
        if valor == "+/-":
            btn = tk.Button(root, text=valor, bg=colores["especiales"], fg="white", **boton_estilo, command=cambiar_signo)
        else:
            color = colores["numeros"] if valor.isdigit() or valor == "." else colores["operadores"]
            btn = tk.Button(root, text=valor, bg=color, fg="white", **boton_estilo, command=lambda v=valor: click(v))
        btn.grid(row=fila, column=col, padx=5, pady=5)

# Botón de borrar un solo dígito
btn_borrar = tk.Button(root, text="C", bg=colores["borrar"], fg="white", **boton_estilo, command=borrar_uno)
btn_borrar.grid(row=5, column=0, padx=5, pady=5)

# Botón de borrar todo (CC)
btn_borrar_todo = tk.Button(root, text="CC", bg=colores["borrar_todo"], fg="white", font=("Arial", 16), height=2, bd=2, relief="ridge", command=borrar_todo)
btn_borrar_todo.grid(row=5, column=1, columnspan=2, sticky="nsew", padx=5, pady=5)

# Botón de igual (=)
btn_igual = tk.Button(root, text="=", bg=colores["igual"], fg="white", font=("Arial", 16), height=2, bd=2, relief="ridge", command=calcular)
btn_igual.grid(row=5, column=3, sticky="nsew", padx=5, pady=5)

# Ajustar tamaño dinámico
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

# Vincular teclado físico y numpad con la función de manejo de teclas
root.bind("<Key>", manejar_tecla)

# Ejecutar la app
root.mainloop()
