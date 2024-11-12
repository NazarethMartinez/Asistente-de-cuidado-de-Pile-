from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
import subprocess

#Ventana
app = tk.Tk()
app.title("Bienvenido a GuíaDermAsistente")
app.geometry("800x600") #tamaño de la ventana
app.configure(bg="#FFFFFF") 

# Función para abrir asistente.py
def abrir_asistente():
    subprocess.Popen(["python", "login.py"])


#Etilo para el encabezado
header_font_style = ("Helvetica", 36, "bold")
lbl_header = tk.Label(app, text="GuíaDermAsistente", font=header_font_style, bg="#FFFFFF", fg="#BD825C")
lbl_header.pack(pady=20)

#estilo de fuente para el texto
font_style = ("Bookman Old Style", 12)

# Marco para el texto y la imagen
frame_contenido = tk.Frame(app, bg="#FFFFFF")
frame_contenido.pack(expand=True)
texto = "GuíaDermAsistente es un innovador asistente virtual diseñado para revolucionar la forma en que las personas cuidan su piel. En un mundo donde el cuidado de la piel es los mas importante, GuíaDermAsistente surge como una solución integral y personalizada."
lbl_texto = tk.Label(frame_contenido, text=texto, wraplength=700, justify="left", anchor="w", bg="#FFFFFF", font=font_style)
lbl_texto.pack(side="top", padx=10, pady=10, fill="x")  # Colocar el texto arriba y expandir horizontalmente

# Importacion de  imagen
imagen = Image.open("belleza.jpg")
imagen = imagen.resize((400, 400))  
imagen = ImageTk.PhotoImage(imagen)

# etiqueta para la imagen
lbl_imagen = tk.Label(frame_contenido, image=imagen)
lbl_imagen.image = imagen  # Mantener una referencia
lbl_imagen.pack(side="top", padx=10, pady=10)  

# Marco para el botón
frame_botones = tk.Frame(app, bg="#FFFFFF")
frame_botones.pack(expand=True)

# Función para el botón
def on_button_click():
    print("Botón clickeado")

#estilo de fuente y color para el botón
style = ttk.Style()
style.configure("Custom.TButton", font=("Bookman Old Style", 14), foreground="#BD825C", background="#FFFFFF")

# Botón para abrir la ventana de login
btn_asistente = ttk.Button(app, text="Bienvenido al Sistema", command=abrir_asistente, style="Custom.TButton")
btn_asistente.pack(pady=20)

# Ejecutar ventana
app.mainloop()
