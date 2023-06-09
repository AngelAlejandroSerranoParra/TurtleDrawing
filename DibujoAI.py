import turtle
import random
from PIL import ImageGrab
import os

# Definir una clase para representar los dibujos
class Dibujo:
    def __init__(self, forma, tamaño, color, grosor, x, y, angulo):
        self.forma = forma
        self.tamaño = tamaño
        self.color = color
        self.grosor = grosor
        self.x = x
        self.y = y
        self.angulo = angulo

    def dibujar(self):
        tortuga.width(self.grosor)
        tortuga.penup()
        tortuga.setpos(self.x, self.y)
        tortuga.setheading(self.angulo)
        tortuga.pendown()
        tortuga.color(self.color)

        if self.forma == "cuadrado":
            for _ in range(4):
                tortuga.forward(self.tamaño)
                tortuga.right(90)
        elif self.forma == "triangulo":
            for _ in range(3):
                tortuga.forward(self.tamaño)
                tortuga.right(120)
        elif self.forma == "circulo":
            tortuga.circle(self.tamaño)

# Obtener el número de figuras en la población inicial
tamanio_poblacion = int(input("Ingrese el número de figuras en la población inicial: "))

# Crear una población inicial de dibujos aleatorios
def crear_poblacion_inicial(tamanio_poblacion):
    poblacion = []

    for _ in range(tamanio_poblacion):
        forma = random.choice(figuras)
        tamaño = random.randint(50, 200)
        color = random.choice(colores)
        grosor = random.randint(grosor_minimo, grosor_maximo)
        x = random.randint(-400, 400)
        y = random.randint(-300, 300)
        angulo = random.randint(0, 360)

        dibujo = Dibujo(forma, tamaño, color, grosor, x, y, angulo)
        poblacion.append(dibujo)

    return poblacion

# Parámetros de configuración
cantidad_generaciones = 10
cantidad_seleccion = 5
cantidad_hijos = 10
probabilidad_mutacion = 0.1

# Crear una instancia de la ventana
ventana = turtle.Screen()
ventana.setup(width=800, height=600)

# Crear una instancia de la tortuga
tortuga = turtle.Turtle()

# Definir una lista de figuras
figuras = ["cuadrado", "triangulo", "circulo"]

# Definir una lista de colores
colores = ["red", "blue", "green", "orange", "purple", "yellow"]

# Definir un rango de grosor de dibujo
grosor_minimo = 1
grosor_maximo = 10

# Crear una población inicial de dibujos aleatorios
poblacion = crear_poblacion_inicial(tamanio_poblacion)

# Evolucionar la población durante varias generaciones
for generacion in range(cantidad_generaciones):
    # Borrar los dibujos anteriores
    tortuga.clear()

    # Dibujar la población actual
    for dibujo in poblacion:
        dibujo.dibujar()

    # Seleccionar los mejores dibujos
    mejores_dibujos = sorted(poblacion, key=lambda dibujo: dibujo.tamaño, reverse=True)[:cantidad_seleccion]

    # Generar una nueva generación
    nueva_generacion = []

    for _ in range(cantidad_hijos):
        padre = random.choice(mejores_dibujos)
        madre = random.choice(mejores_dibujos)

        forma = random.choice([padre.forma, madre.forma])
        tamaño = random.randint(50, 200)
        color = random.choice(colores)
        grosor = random.randint(grosor_minimo, grosor_maximo)
        x = random.randint(-400, 400)
        y = random.randint(-300, 300)
        angulo = random.randint(0, 360)

        nuevo_dibujo = Dibujo(forma, tamaño, color, grosor, x, y, angulo)
        nueva_generacion.append(nuevo_dibujo)

    # Reemplazar la población anterior con la nueva generación
    poblacion = nueva_generacion

    # Tomar una captura de pantalla del área de dibujo
    imagen_generacion = ImageGrab.grab(bbox=(0, 0, ventana.window_width(), ventana.window_height()))

    # Guardar la imagen en el escritorio
    ruta_imagen = os.path.join(os.path.expanduser("~"), "Desktop", f"generacion_{generacion}.png")
    imagen_generacion.save(ruta_imagen)

# Cerrar la ventana al hacer clic en ella
ventana.exitonclick()
