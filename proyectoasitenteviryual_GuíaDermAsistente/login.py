import tkinter as tk
from tkinter import messagebox, ttk
import pymongo
import subprocess
from PIL import Image, ImageTk

# Conexion a la base de datos MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["UsuariosEntrada"]
usuarios = db["usuarios"]

def registrar_usuario(usuario, contraseña):
    nuevo_usuario = {"usuario": usuario, "contraseña": contraseña}
    usuarios.insert_one(nuevo_usuario)
    messagebox.showinfo("Registro exitoso", "¡Usuario registrado con éxito!")

# Función para verificar las credenciales del usuario
def verificar_credenciales(usuario, contraseña):
    usuario_encontrado = usuarios.find_one({"usuario": usuario, "contraseña": contraseña})
    if usuario_encontrado:
        messagebox.showinfo("Login exitoso", "¡Bienvenido, {}!".format(usuario))
        abrir_asistente()
    else:
        messagebox.showerror("Error de login", "Usuario o contraseña incorrectos")

# Función para abrir ventana "asistente.py"
def abrir_asistente():
    subprocess.Popen(["python", "asitente.py"])

#ventana de la aplicación
app = tk.Tk()
app.title("Login GuíaDermAsistente")
app.geometry("800x600")
app.configure(bg="#FFFFFF") 

# Configuración del estilo
style = ttk.Style()
style.configure("TLabel", font=('Arial', 10), padding=10)
style.configure("TEntry", padding=5)
style.configure("TButton", font=('Arial', 10), padding=10)
style.configure("TFrame", background="#FFFFFF")

# Frame para mejorar la organización y el diseño
main_frame = ttk.Frame(app, padding="30 30 30 30", style="TFrame")
main_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

app.columnconfigure(0, weight=1)
app.rowconfigure(0, weight=1)

main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)
main_frame.rowconfigure(0, weight=1)
main_frame.rowconfigure(1, weight=1)

# Agregar la imagen
image_path = "jjj.jpg" 
image = Image.open(image_path)
image = image.resize((1400, 400), Image.ADAPTIVE) 
photo = ImageTk.PhotoImage(image)

#etiqueta para mostrar la imagen
lbl_imagen = tk.Label(main_frame, image=photo)
lbl_imagen.grid(row=0, column=0, columnspan=2, pady=10)

# Etiquetas y campos de entrada
lbl_usuario = tk.Label(main_frame, text="Usuario:", font=("Bookman Old Style", 14), bg="#FFFFFF")
lbl_usuario.grid(column=0, row=1, sticky=tk.E, padx=(10, 5), pady=5)
entry_usuario = ttk.Entry(main_frame, width=20)
entry_usuario.grid(column=1, row=1, sticky=tk.W, padx=(5, 10), pady=5)

lbl_contraseña = tk.Label(main_frame, text="Contraseña:", font=("Bookman Old Style", 14), bg="#FFFFFF")
lbl_contraseña.grid(column=0, row=2, sticky=tk.E, padx=(10, 5), pady=5)
entry_contraseña = ttk.Entry(main_frame, show="*", width=20)
entry_contraseña.grid(column=1, row=2, sticky=tk.W, padx=(5, 10), pady=5)

# Función para el botón de registro
def registro():
    if not entry_usuario.get() or not entry_contraseña.get():
        messagebox.showwarning("Advertencia", "Por favor completa todos los campos para registrar.")
    else:
        usuario = entry_usuario.get()
        contraseña = entry_contraseña.get()
        registrar_usuario(usuario, contraseña)

# Función para el botón de login
def login():
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()
    verificar_credenciales(usuario, contraseña)

# Botones de registro y login
btn_registro = tk.Button(main_frame, text="Registrar", command=registro, bg="#BD825C", fg="white", font=("Bookman Old Style", 14), relief=tk.RAISED, borderwidth=3)
btn_registro.grid(row=3, column=0, padx=(5, 2), pady=10, sticky=tk.W)

btn_login = tk.Button(main_frame, text="Iniciar", command=login, bg="#BD825C", fg="white", font=("Bookman Old Style", 14), relief=tk.RAISED, borderwidth=3)
btn_login.grid(row=3, column=1, padx=(2, 5), pady=10, sticky=tk.E)

# Ejecutar la aplicación
app.mainloop()
