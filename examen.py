import tkinter as tk
from PIL import Image, ImageOps
import random

# Configuración inicial
ancho, alto = 800, 600
colores_espacio = ['#FFD700', '#FFFFFF', '#FF4500', '#00BFFF', '#4B0082', '#9400D3', '#FF69B4', '#00FF7F']

# Crear la ventana y el canvas
ventana = tk.Tk()
ventana.title("Dibujo de Imagen")
canvas = tk.Canvas(ventana, width=ancho, height=alto, bg='black')
canvas.pack()

# Función para cargar y procesar la imagen
def cargar_imagen(filepath):
    imagen = Image.open(filepath)
    imagen = imagen.convert('L')  # Convertir a escala de grises
    imagen = imagen.resize((ancho, alto))
    puntos = [(x, y) for y in range(imagen.height) for x in range(imagen.width) if imagen.getpixel((x, y)) < 128]
    return puntos

# Función para dibujar los puntos y líneas en el canvas
def dibujar_puntos(puntos):
    num_puntos = len(puntos)
    color_anterior = random.choice(colores_espacio)
    for i in range(num_puntos):
        x, y = puntos[i]
        color = random.choice(colores_espacio)
        canvas.create_oval(x, y, x+10, y+10, fill=color, outline=color)
        if i > 0:
            x_prev, y_prev = puntos[i-1]
            canvas.create_line(x_prev, y_prev, x, y, fill=color_anterior, width=5)
        color_anterior = color

# Función para generar la galaxia
def generar_galaxia():
    canvas.delete("all")  # Limpiar el canvas
    puntos = cargar_imagen('img/meme.png')  # Cambiar a la ruta de tu imagen
    dibujar_puntos(puntos)

# Botón para iniciar el proceso
btn_generar = tk.Button(ventana, text="Generar Galaxia", command=generar_galaxia)
btn_generar.pack()

# Iniciar el loop de Tkinter
ventana.mainloop()
