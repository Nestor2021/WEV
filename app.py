from flask import Flask, render_template, request
from motor_inferencia import evaluar
from datetime import datetime

app = Flask(__name__)

nombres_areas = [
    "Servicio Social", "Persuasivo", "Literario", "Artistico-Plastico", "Musical",
    "Trabajo de Oficina", "Cientifico", "Calculo", "Mecanico", "Aire Libre"
]

def procesar_fila(fila):
    elementos = fila.split('\t') if '\t' in fila else fila.split()
    
    if len(elementos) < 10:
        raise ValueError("La fila no contiene suficientes datos")
    
    # Extraer datos fijos (índices ajustados)
    fecha = elementos[0]
    email = elementos[1]
    nombre = elementos[2]
    telefono = elementos[4]  # 5to elemento (índice 4)
    edad = elementos[5]
    
    # Extraer primeros 10 números (ignorando los primeros 6 campos que son datos personales)
    numeros_encontrados = []
    for elem in elementos[6:]:  # Saltamos los primeros 6 elementos (datos personales)
        if elem.replace('.', '').isdigit():
            numeros_encontrados.append(int(float(elem)))
            if len(numeros_encontrados) == 10:
                break
    
    if len(numeros_encontrados) != 10:
        raise ValueError("No se encontraron 10 puntajes válidos después de los datos personales")
    
    return {
        'fecha': fecha,
        'email': email,
        'nombre': nombre.title(),
        'telefono': telefono,
        'edad': edad,
        'puntajes': numeros_encontrados
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    datos_personales = None
    resultado = []
    areas_destacadas = []
    error = None
    psicopedagogo = "Lic. "  
    
    if request.method == 'POST':
        fila = request.form.get('fila_datos', '').strip()
        psicopedagogo = request.form.get('psicopedagogo', psicopedagogo)
        try:
            datos = procesar_fila(fila)
            datos_personales = {
                'nombre': datos['nombre'],
                'edad': datos['edad'],
                'fecha': datos['fecha'],
                'email': datos['email'],
                'telefono': datos['telefono'], 
                'psicopedagogo': psicopedagogo
            }
            resultado, areas_destacadas = evaluar(nombres_areas, datos['puntajes'])
        except ValueError as e:
            error = f"Error en los datos: {str(e)}"
        except Exception as e:
            error = f"Error inesperado: {str(e)}"

    return render_template('index.html',
                         datos=datos_personales,
                         resultado=resultado,
                         areas_destacadas=areas_destacadas,
                         error=error, psicopedagogo=psicopedagogo)

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))  # Para Render
    app.run(host='0.0.0.0', port=port)
