#TRABAJO DE PIERO SOTO Y VICENTE BARRIENTOS
from pathlib import Path                    # Leer carpetas
import numpy as np                         # Leer archivos .npy
import matplotlib.pyplot as plt            # Graficar
from matplotlib.widgets import Button      # Botones

# LEER CARPETA

carpeta = Path(__file__).parent #Carpeta donde esta este archivo .py
carpeta_data = carpeta / "data" #Carpeta data dentro del proyecto, si existe

archivos = list(carpeta.glob("*.npy")) #Guardar archivos .npy que esten junto al codigo

if carpeta_data.exists():
    archivos += list(carpeta_data.glob("*.npy")) #Guardar archivos .npy que esten dentro de data

print("Archivos disponibles:\n") # Mostrar archivos disponibles

n = 1

for i in archivos:
    print(f"{n}. {i.name}") #imprime un numero y luego el nombre del archivo
    n += 1

# SELECCIONAR ARCHIVO

opcion = int(input("\nSeleccione el archivo a cargar: "))

archivo_seleccionado = archivos[opcion - 1]

# CARGAR DATOS

datos = np.load(archivo_seleccionado)

senal_actual = datos


# CREAR GRAFICO

fig, ax = plt.subplots(figsize=(10,5))


plt.subplots_adjust(top=0.82) #Dejar espacio para botones


# Graficar señal original   
linea, = ax.plot(datos, label="Señal Original") #La coma en la variable hace que saque el numero entero del valor resultante


ax.set_title(archivo_seleccionado.name) #Etiquetas
ax.set_xlabel("Muestras") #Etiqueta para el eje x
ax.set_ylabel("Amplitud") #Etiqueta para el eje y


ax.grid(True) #Grid/Cuadricula

ax.legend(loc="upper right") #Posicion de leyenda


# FUNCIONES


# Volver a señal original
def original(event):

    global senal_actual

    senal_actual = datos

    linea.set_ydata(datos) #Cambia los datos de Y para el nuevo grafico (ya que lo unico que cambia es la y, la x siempre seguira avanzando)

    linea.set_label("Señal Original") #Titulo

    ax.relim() #Relimitacion en razon a la funcion nueva (calcula los nuevos limites)

    ax.autoscale_view() #Actualiza el zoom para que quede con los limites ya calculados

    ax.legend() #Leyenda

    plt.draw()#Actualizar la señal en pantalla, la "dibuja"


# Media movil
def media_movil(event):

    global senal_actual

    ventana = 7 #Cantidad de suavizado

    suavizada = np.convolve(datos,np.ones(ventana) / ventana,mode="same") #np.ones(ventana) / ventana: actua como un promedio ponderado equitativo
    #mode = "same": hace que la señal nueva sea igual de larga que la original

    linea.set_ydata(suavizada)

    senal_actual = suavizada

    linea.set_label(f"Media móvil ({ventana})")

    ax.relim()
    ax.autoscale_view()

    ax.legend()

    plt.draw()


# Mediana movil
def mediana_movil(event):

    global senal_actual

    ventana = 7 #Cantidad de suavizado aplicado

    suavizada = []

    for i in range(len(datos)):

        inicio = max(0, i - ventana // 2)
        fin = min(len(datos), i + ventana // 2) #Funcion para crear los datos de la señal suavizada

        mediana = np.median(datos[inicio:fin]) 

        suavizada.append(mediana) #Los datos nuevos se guardan en la lista suavizada

    linea.set_ydata(suavizada)

    senal_actual = suavizada

    linea.set_label(f"Mediana móvil ({ventana})") 

    ax.relim()

    ax.autoscale_view()

    ax.legend()

    plt.draw() 


# Estadísticas
def estadisticas(event):

    promedio = np.mean(senal_actual) #Funcion para sacar el promedio/media aritmetica (mean en ingles)
    maximo = np.max(senal_actual)
    minimo = np.min(senal_actual)
    desviacion = np.std(senal_actual) #Funcion que saca la desviacion estandar (standar deviation)

    print("\n----- ESTADÍSTICAS -----")
    print(f"Promedio: {promedio:.2f}") # El .2f sirve para mostrar un float con exactamente dos puntos
    print(f"Maximo: {maximo:.2f}")
    print(f"Mínimo: {minimo:.2f}")
    print(f"Desviación estándar: {desviacion:.2f}")



#BOTONES 


# Boton para la señal original
ax_boton1 = plt.axes([0.08, 0.9, 0.15, 0.06]) #Posicion de boton

boton1 = Button(ax_boton1, "Original") #Nombre de display

boton1.on_clicked(original) #La accion que hara al ser clickeada, en este caso llama a la func(original)


# Boton Media Móvil
ax_boton2 = plt.axes([0.28, 0.9, 0.15, 0.06])

boton2 = Button(ax_boton2, "Media Móvil")

boton2.on_clicked(media_movil)


# Boton Mediana Móvil
ax_boton3 = plt.axes([0.50, 0.9, 0.18, 0.06])

boton3 = Button(ax_boton3, "Mediana Móvil")

boton3.on_clicked(mediana_movil)


# Boton Estadísticas
ax_boton4 = plt.axes([0.75, 0.9, 0.15, 0.06]) #Posicion de boton

boton4 = Button(ax_boton4, "Estadísticas") #Nombre Display

boton4.on_clicked(estadisticas) #Funcion que hara al ser clickeada


plt.show() #Esta funcion siempre va al final para que se muestre todo lo que este dentro (la ventana emergente)

