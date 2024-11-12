import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.messagebox as messagebox

# Variables de entrada
tipo_persona = ctrl.Antecedent(np.arange(0, 101, 1), 'tipo_persona')
tipo_piel = ctrl.Antecedent(np.arange(0, 11, 1), 'tipo_piel')
textura = ctrl.Antecedent(np.arange(0, 11, 1), 'textura')

#Variables de salida
estado_piel = ctrl.Consequent(np.arange(0, 101, 1), 'estado_piel')

# Definir las funciones de pertenencia para cada variable
tipo_persona.automf(3, names=['niño', 'joven', 'adulto'])
tipo_piel.automf(7, names=['normal', 'sensible', 'seca', 'mixta', 'grasa', 'madura'])
textura.automf(4, names=['lisa', 'áspera', 'poros_dilatados', 'acné'])

estado_piel['crítico'] = fuzz.trimf(estado_piel.universe, [0, 0, 20])
estado_piel['muy_dañada'] = fuzz.trimf(estado_piel.universe, [10, 30, 50])
estado_piel['dañada'] = fuzz.trimf(estado_piel.universe, [40, 60, 80])
estado_piel['buena'] = fuzz.trimf(estado_piel.universe, [70, 90, 100])
estado_piel['excelente'] = fuzz.trimf(estado_piel.universe, [80, 100, 100])

# Definir reglas:
#niño
rule1 = ctrl.Rule(tipo_persona['niño'] & tipo_piel['normal'] & textura['lisa'], estado_piel['buena'])
rule2 = ctrl.Rule(tipo_persona['niño'] & tipo_piel['sensible'] & textura['áspera'], estado_piel['dañada'])
rule3 = ctrl.Rule(tipo_persona['niño']& tipo_piel['seca'] & textura['poros_dilatados'], estado_piel['muy_dañada'])
rule4 = ctrl.Rule(tipo_persona['niño']& tipo_piel['mixta'] & textura['acné'],estado_piel['crítico'])
rule5 = ctrl.Rule(tipo_persona['niño']& tipo_piel['grasa'] &textura['lisa'], estado_piel['buena'])
rule6 = ctrl.Rule(tipo_persona['niño'] & tipo_piel['normal'] & textura['poros_dilatados'], estado_piel['muy_dañada'])
rule7 = ctrl.Rule(tipo_persona['niño'] & tipo_piel['sensible'] & textura['poros_dilatados'], estado_piel['dañada'])
rule8 = ctrl.Rule(tipo_persona['niño'] & tipo_piel['seca'] & textura['acné'], estado_piel['crítico'])
rule9 = ctrl.Rule(tipo_persona['niño'] & tipo_piel['mixta'] & textura['áspera'], estado_piel['muy_dañada'])
rule10 = ctrl.Rule(tipo_persona['niño'] & tipo_piel['grasa'] & textura['poros_dilatados'], estado_piel['crítico'])
#joven
rule11= ctrl.Rule(tipo_persona['joven'] & tipo_piel['seca'] & textura['lisa'], estado_piel['excelente'])
rule12 = ctrl.Rule(tipo_persona['joven'] & tipo_piel['normal'] & textura['lisa'], estado_piel['buena'])
rule13 = ctrl.Rule(tipo_persona['joven'] & tipo_piel['grasa'] & textura['acné'], estado_piel['dañada'])
rule14 = ctrl.Rule(tipo_persona['joven'] & tipo_piel['mixta'] & textura['poros_dilatados'], estado_piel['buena'])
rule15 = ctrl.Rule(tipo_persona['joven'] & tipo_piel['sensible'] & textura['áspera'], estado_piel['dañada'])
rule16 = ctrl.Rule(tipo_persona['joven'] & tipo_piel['sensible'] & textura['poros_dilatados'], estado_piel['muy_dañada'])
rule17 = ctrl.Rule(tipo_persona['joven'] & tipo_piel['normal'] & textura['áspera'], estado_piel['dañada'])
rule18 = ctrl.Rule(tipo_persona['joven'] & tipo_piel['grasa'] & textura['lisa'], estado_piel['buena'])
rule19 = ctrl.Rule(tipo_persona['joven'] & tipo_piel['mixta'] & textura['lisa'], estado_piel['excelente'])
rule20 = ctrl.Rule(tipo_persona['joven'] & tipo_piel['seca'] & textura['poros_dilatados'], estado_piel['buena'])
#Adulto
rule21 = ctrl.Rule(tipo_persona['adulto'] & tipo_piel['sensible'] & textura['lisa'], estado_piel['muy_dañada'])
rule22 = ctrl.Rule(tipo_persona['adulto'] & tipo_piel['madura'] & textura['poros_dilatados'], estado_piel['crítico'])
rule23 = ctrl.Rule(tipo_persona['adulto'] & tipo_piel['mixta'] & textura['áspera'], estado_piel['buena'])
rule24 = ctrl.Rule(tipo_persona['adulto'] & tipo_piel['grasa'] & textura['poros_dilatados'], estado_piel['dañada'])
rule25 = ctrl.Rule(tipo_persona['adulto'] & tipo_piel['normal'] & textura['lisa'], estado_piel['excelente'])
rule26 = ctrl.Rule(tipo_persona['adulto'] & tipo_piel['seca'] & textura['lisa'], estado_piel['excelente'])
rule27 = ctrl.Rule(tipo_persona['adulto'] & tipo_piel['normal'] & textura['poros_dilatados'], estado_piel['crítico'])
rule28 = ctrl.Rule(tipo_persona['adulto'] & tipo_piel['grasa'] & textura['áspera'], estado_piel['dañada'])
rule29 = ctrl.Rule(tipo_persona['adulto'] & tipo_piel['mixta'] & textura['acné'], estado_piel['muy_dañada'])
rule30 = ctrl.Rule(tipo_persona['adulto'] & tipo_piel['sensible'] & textura['lisa'], estado_piel['buena'])

# Crear sistema de control
sistema_ctrl = ctrl.ControlSystem(
[rule1, rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12,rule13,
rule14,rule15,rule16,rule17,rule18,rule19,rule20,
rule21,rule22,rule23,rule24,rule25,rule25,rule26,rule27,rule28,rule29,rule30])

# Crear simulador
simulador = ctrl.ControlSystemSimulation(sistema_ctrl)

# Crear ventana de la aplicación
app = tk.Tk()
app.title("Asistente Virtual para el cuidado de la piel")
app.geometry("800x600")
app.configure(bg="#FFFFFF") 

# importación de la imagen
imagen = Image.open("arriba.jpg")  # Ruta de tu imagen
imagen = imagen.resize((1600, 400), Image.ADAPTIVE) # tamaño de la imagen
imagen = ImageTk.PhotoImage(imagen)

# Mostrar la imagen en un Label
lbl_imagen = tk.Label(app, image=imagen)
lbl_imagen.image = imagen  # Necesario para evitar que la imagen sea eliminada por el recolector de basura
lbl_imagen.grid(row=0, column=0, columnspan=2)

def cerrar_app():
    app.destroy()
    
#Funcion reiniciar consulta
def reiniciar_consulta():
    # Limpiar campos de entrada
    entry_edad.delete(0, tk.END)
    entry_tipo_piel.delete(0, tk.END)
    entry_textura.delete(0, tk.END)
    
    # Restablecer la etiqueta de resultado
    lbl_resultado.config(text="")
    
# Defenir función validar_entrada
def validar_entrada(valor, valores_permitidos):
    return valor in valores_permitidos

def obtener_estado_piel():

    # Verificar si los campos están llenos
    if not entry_edad.get() or not entry_tipo_piel.get() or not entry_textura.get():
        messagebox.showwarning("Advertencia", "Por favor, completa todos los campos.")
        return
    
    # Mapear etiquetas lingüísticas a valores numéricos
    mapeo_tipo_persona = {'niño': 20, 'joven': 50, 'adulto': 80}
    mapeo_tipo_piel = {'normal': 3, 'sensible': 4, 'seca': 5, 'mixta': 6, 'grasa': 7, 'madura': 8}
    mapeo_textura = {'lisa': 2, 'áspera': 5, 'poros_dilatados': 8, 'acné': 10}

    # Validar las entradas
    if not validar_entrada(entry_edad.get().lower(), mapeo_tipo_persona.keys()):
        messagebox.showwarning("Advertencia", "Valores no permitidos.")
        return
    if not validar_entrada(entry_tipo_piel.get().lower(), mapeo_tipo_piel.keys()):
        messagebox.showwarning("Advertencia", "Valores no permitidos.")
        return
    if not validar_entrada(entry_textura.get().lower(), mapeo_textura.keys()):
        messagebox.showwarning("Advertencia", "Valores no permitidos.")
        return

    edad_val = mapeo_tipo_persona.get(entry_edad.get().lower(), 0)
    tipo_piel_val = mapeo_tipo_piel.get(entry_tipo_piel.get().lower(), 0)
    textura_val = mapeo_textura.get(entry_textura.get().lower(), 0)
    
    simulador.input['tipo_persona'] = edad_val
    simulador.input['tipo_piel'] = tipo_piel_val
    simulador.input['textura'] = textura_val
    
    simulador.compute()
    
    resultado = simulador.output['estado_piel']
    
    # Mapear el resultado numérico a las etiquetas lingüísticas
    if resultado <= 20:
        estado = "crítico"
    elif resultado <= 50:
        estado = "muy dañada"
    elif resultado <= 80:
        estado = "dañada"
    elif resultado <= 100:
        estado = "buena"
    else:
        estado = "excelente"
    
    lbl_resultado.config(text=f"Tu piel se encuentra en estado : {estado}")
    
# Estilo para los widgets
style = ttk.Style()
style.configure('Custom.TLabel', font=('Arial', 12), padding=5)
style.configure('Custom.TEntry', font=('Arial', 12), padding=5)
style.configure('Custom.TButton', font=('Arial', 12), padding=5)

#Etiqueta para la edad
lbl_edad = ttk.Label(app, text="Tipo de persona:", style='Custom.TLabel', font=("Bookman Old Style", 14), background="#FFFFFF")
lbl_edad.grid(row=1, column=0, padx=10, pady=5, sticky='e')
entry_edad = ttk.Entry(app, style='Custom.TEntry')
entry_edad.grid(row=1, column=1, padx=10, pady=5, sticky='w')

#Etiqueta para el tipo de piel
lbl_tipo_piel = ttk.Label(app, text="Tipo de piel:", style='Custom.TLabel', font=("Bookman Old Style", 14), background="#FFFFFF")
lbl_tipo_piel.grid(row=2, column=0, padx=10, pady=5, sticky='e')
entry_tipo_piel = ttk.Entry(app, style='Custom.TEntry')
entry_tipo_piel.grid(row=2, column=1, padx=10, pady=5, sticky='w')

#Etiqueta para la textura de la piel
lbl_textura = ttk.Label(app, text="Textura:", style='Custom.TLabel', font=("Bookman Old Style", 14), background="#FFFFFF")
lbl_textura.grid(row=3, column=0, padx=10, pady=5, sticky='e')
entry_textura = ttk.Entry(app, style='Custom.TEntry')
entry_textura.grid(row=3, column=1, padx=10, pady=5, sticky='w')

#Botón para calcular el estado de la piel
btn_calcular = ttk.Button(app, text="Calcular estado de la piel", command=obtener_estado_piel, style='Custom.TButton')
btn_calcular.grid(row=4, column=0, columnspan=2, padx=10, pady=10)


# Botón para reiniciar la consulta
btn_reiniciar = ttk.Button(app, text="Nueva consulta", command=reiniciar_consulta, style='Custom.TButton')
btn_reiniciar.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

# Crear el botón para cerrar todas las pantallas
btn_cerrar = ttk.Button(app, text="Cerrar", command=cerrar_app, style='Custom.TButton')
btn_cerrar.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Etiqueta del resultado
lbl_resultado = ttk.Label(app, text="", style='Custom.TLabel', font=("Bookman Old Style", 14), background="#FFFFFF", anchor='center', borderwidth=2, relief='groove')
lbl_resultado.grid(row=5, column=0, columnspan=2, padx=10, pady=10)


# Ejecutar la aplicación
app.mainloop()