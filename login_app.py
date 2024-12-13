# login_app.py

import tkinter as tk
from tkinter import messagebox

# Datos de ejemplo para autenticación
users = {
    "elvis": "1234"
}

def verificar_login():
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()

    if usuario in users and users[usuario] == contraseña:
        messagebox.showinfo("Login exitoso", f"Bienvenido {usuario}!")
    else:
        messagebox.showerror("Error de Login", "Usuario o contraseña incorrectos")

# Configurar la ventana principal
root = tk.Tk()
root.title("Login App")
root.geometry("400x300")  # Ajustar tamaño de la ventana

# Crear un canvas para el fondo degradado
canvas = tk.Canvas(root, width=400, height=300)
canvas.pack(fill="both", expand=True)

# Crear el fondo degradado
for i in range(256):
    color = f"#{i:02x}{(255-i):02x}ff"
    canvas.create_line(0, i, 400, i, fill=color)

# Colocar los widgets sobre el canvas
canvas.create_window(200, 50, window=tk.Label(root, text="Usuario", bg=color))
entry_usuario = tk.Entry(root)
canvas.create_window(200, 80, window=entry_usuario)

canvas.create_window(200, 120, window=tk.Label(root, text="Contraseña", bg=color))
entry_contraseña = tk.Entry(root, show="*")
canvas.create_window(200, 150, window=entry_contraseña)

boton_login = tk.Button(root, text="Login", command=verificar_login)
canvas.create_window(200, 200, window=boton_login)

# Ejecutar la aplicación
root.mainloop()
