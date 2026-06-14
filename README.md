# Analisis interactivo de senales digitales

Aplicacion desarrollada conjuntamente por Piero Soto y Vicente Barrientos para
el Proyecto 1 de Programacion I. Permite cargar, visualizar, procesar y analizar
senales digitales almacenadas en archivos `.npy` mediante una interfaz
interactiva creada con Matplotlib.

## Funcionalidades

- Detecta automaticamente los archivos `.npy` ubicados junto al programa o en
  la carpeta `data`.
- Permite seleccionar una senal mediante un menu en la consola.
- Muestra la senal original en un grafico interactivo.
- Aplica filtros de media movil y mediana movil con una ventana de 7 muestras.
- Calcula el promedio, maximo, minimo y desviacion estandar de la senal que se
  esta mostrando.
- Permite volver a la senal original mediante un boton.

## Requisitos

- Python 3
- NumPy
- Matplotlib

Instala las dependencias con:

```bash
pip install numpy matplotlib
```

## Ejecucion

Desde la carpeta del proyecto, ejecuta:

```bash
python "MATPLOTLIBDOCUMENTACION (1).py"
```

El programa mostrara en la consola los archivos `.npy` disponibles. Ingresa el
numero de la senal que deseas analizar y se abrira la ventana interactiva.

## Controles

- **Original:** restaura la senal cargada inicialmente.
- **Media Movil:** suaviza la senal mediante un promedio movil.
- **Mediana Movil:** suaviza la senal mediante una mediana movil.
- **Estadisticas:** imprime en la consola las estadisticas de la senal visible.

## Estructura

```text
.
|-- data/                         # Senales digitales de ejemplo
|-- MATPLOTLIBDOCUMENTACION (1).py
`-- README.md
```

## Autores del proyecto

- [Piero Soto](https://github.com/PieroSotoUCT)
- [Vicente Barrientos](https://github.com/mimikyu313k)

Ambos autores participaron en el desarrollo completo del proyecto.
