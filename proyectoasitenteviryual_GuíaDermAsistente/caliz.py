import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import tkinter as tk

# Definir las variables de entrada
edad = ctrl.Antecedent(np.arange(0, 101, 1), 'edad')
tipo_piel = ctrl.Antecedent(np.arange(0, 11, 1), 'tipo_piel')
textura = ctrl.Antecedent(np.arange(0, 11, 1), 'textura')

# Definir las variables de salida
estado_piel = ctrl.Consequent(np.arange(0, 101, 1), 'estado_piel')

# Definir las funciones de pertenencia para cada variable
edad.automf(3, names=['niño', 'joven', 'adulto'])
tipo_piel.automf(7, names=['normal', 'sensible', 'seca', 'mixta', 'grasa', 'madura'])
textura.automf(4, names=['lisa', 'áspera', 'poros_dilatados', 'acné'])

estado_piel['crítico'] = fuzz.trimf(estado_piel.universe, [0, 0, 20])
estado_piel['muy_dañada'] = fuzz.trimf(estado_piel.universe, [10, 30, 50])
estado_piel['dañada'] = fuzz.trimf(estado_piel.universe, [40, 60, 80])
estado_piel['buena'] = fuzz.trimf(estado_piel.universe, [70, 90, 100])
estado_piel['excelente'] = fuzz.trimf(estado_piel.universe, [80, 100, 100])

# Definir reglas

rule1 = ctrl.Rule(edad['niño'] & tipo_piel['normal'] & textura['lisa'], estado_piel['buena'])#correcta

rule2 = ctrl.Rule(edad['niño'] & tipo_piel['sensible'] & textura['áspera'], estado_piel['dañada'])#correcta

rule3 = ctrl.Rule(edad['niño']& tipo_piel['seca'] & textura['poros_dilatados'], estado_piel['muy_dañada'])#correcta

rule4 = ctrl.Rule(edad['niño']& tipo_piel['mixta'] & textura['acné'],estado_piel['crítico'])#correcta

rule5 = ctrl.Rule(edad['niño']& tipo_piel['grasa'] &textura['lisa'], estado_piel['buena'])#correcta



rule6 = ctrl.Rule(edad['joven'] & tipo_piel['seca'] & textura['lisa'], estado_piel['excelente'])#correcta

rule7 = ctrl.Rule(edad['joven'] & tipo_piel['normal'] & textura['lisa'], estado_piel['buena'])#correcta

rule8 = ctrl.Rule(edad['joven'] & tipo_piel['madura'] & textura['áspera'], estado_piel['dañada'])



# Crear sistema de control
sistema_ctrl = ctrl.ControlSystem([rule1, rule2,rule3,rule4,rule5,rule6,rule7,rule8])
# Crear simulador
simulador = ctrl.ControlSystemSimulation(sistema_ctrl)

# Crear ventana de la aplicación
app = tk.Tk()
app.title("Asistente Virtual para el cuidado de la piel")


# Función para obtener el estado de la piel
def obtener_estado_piel():
    # Mapear etiquetas lingüísticas a valores numéricos
    mapeo_edad = {'niño': 20, 'joven': 50, 'adulto': 80}
    mapeo_tipo_piel = {'normal': 3, 'sensible': 4, 'seca': 5, 'mixta': 6, 'grasa': 7, 'madura': 8}
    mapeo_textura = {'lisa': 2, 'áspera': 5, 'poros_dilatados': 8, 'acné': 10}

    edad_val = mapeo_edad.get(entry_edad.get().lower(), 0)
    tipo_piel_val = mapeo_tipo_piel.get(entry_tipo_piel.get().lower(), 0)
    textura_val = mapeo_textura.get(entry_textura.get().lower(), 0)
    
    simulador.input['edad'] = edad_val
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
    
    lbl_resultado.config(text=f"El estado de tu piel es: {estado}")

    
# Interfaz gráfica
lbl_edad = tk.Label(app, text="Edad:")
lbl_edad.grid(row=0, column=0)
entry_edad = tk.Entry(app)
entry_edad.grid(row=0, column=1)

lbl_tipo_piel = tk.Label(app, text="Tipo de piel:")
lbl_tipo_piel.grid(row=1, column=0)
entry_tipo_piel = tk.Entry(app)
entry_tipo_piel.grid(row=1, column=1)

lbl_textura = tk.Label(app, text="Textura:")
lbl_textura.grid(row=2, column=0)
entry_textura = tk.Entry(app)
entry_textura.grid(row=2, column=1)

btn_calcular = tk.Button(app, text="Calcular estado de la piel", command=obtener_estado_piel)
btn_calcular.grid(row=3, column=0, columnspan=2)

lbl_resultado = tk.Label(app, text="")
lbl_resultado.grid(row=4, column=0, columnspan=2)

app.mainloop()
