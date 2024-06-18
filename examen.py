import tkinter as tk
from PIL import Image, ImageTk
import random
import numpy as np

# Definir una paleta de colores parecida a los de una galaxia
colores_galaxia = ['#1B03A3', '#3C1A73', '#6C2DC7', '#8D38C9', '#A74AC7', '#F6358A', '#FF0090', '#FF66CC', '#FF99FF', '#FFFFFF']

def dibujar_lineas(canvas, puntos):
    for i in range(len(puntos)-1):
        x1, y1 = puntos[i]
        x2, y2 = puntos[i+1]
        color = random.choice(colores_galaxia)
        canvas.create_line(x1, y1, x2, y2, fill=color, width=2)

def generar_galaxia():
    # Cargar la imagen
    imagen = Image.open('img/meme.png').convert('L')  # Convertir a escala de grises
    imagen = imagen.resize((500, 500))  # Redimensionar la imagen a 500x500
    ancho, alto = imagen.size
    imagen_tk = ImageTk.PhotoImage(imagen)
    
    # Mostrar la imagen original a la izquierda
    canvas_original.create_image(0, 0, anchor=tk.NW, image=imagen_tk)
    canvas_original.image = imagen_tk
    
    # Obtener los puntos blancos de la imagen
    puntos = [(x, y) for x in range(ancho) for y in range(alto) if imagen.getpixel((x, y)) < 200]
    np.random.shuffle(puntos)  # Barajar los puntos para un trazado aleatorio
    
    # Mostrar los puntos y líneas en el canvas de la galaxia
    canvas_galaxia.delete('all')
    canvas_galaxia.create_rectangle(0, 0, ancho, alto, fill='black')

    # Dibujar las líneas que formen la imagen
    if len(puntos) > 0:
        num_segmentos = min(10000, len(puntos) - 1)  # Ajustar el número de segmentos según el número de puntos disponibles
        for i in range(num_segmentos):
            x1, y1 = puntos[i]
            x2, y2 = puntos[(i + 1) % len(puntos)]
            color = random.choice(colores_galaxia)
            canvas_galaxia.create_line(x1, y1, x2, y2, fill=color, width=1)
            canvas_galaxia.update_idletasks()
            canvas_galaxia.after(1)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Generador de Galaxia")
ventana.geometry("1050x550")  # Ajustar el tamaño de la ventana

# Crear dos canvas uno para la imagen original y otro para la galaxia
canvas_original = tk.Canvas(ventana, width=500, height=500, bg='white')
canvas_original.pack(side=tk.LEFT)

canvas_galaxia = tk.Canvas(ventana, width=500, height=500, bg='black')
canvas_galaxia.pack(side=tk.RIGHT)

# Botón para generar la galaxia
boton_generar = tk.Button(ventana, text="Generar Galaxia", command=generar_galaxia)
boton_generar.pack()

ventana.mainloop()
