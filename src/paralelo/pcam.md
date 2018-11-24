# DISEÑO REALIZADO BAJO LA METODOLOGIA PCAM

Este caso se puede abordar desde diferentes enfoques en razon a la finalidad del programa segun la información.
Un primer enfoque de paralelismo se presenta en que cada columna debe ser contada de manera independiente, es decir, su resultado no depende del la información de la celda anterior, es asi como se puede considerar que segun la cantidad de celdas en la columna un numero determinado de procesadores se encargue del conteo de la palabra en cada noticia. El otro enfoque se da a partir de la cantidad de archivos a analizar, es por esto que se puede descomponer el numero de procesadores a utlizar basados en la cantidad de archivos a analizar basados en este problema especifico.

![Texto Alt](/src/paralelo/propuesta.png "Propuestas")

La solución implementada se sustenta bajo la segunda propuesta, esta propuesta será desarrollada en base a las 4 faces que propone la metodologia PCAM.

## Descomposición de tareas
Proceso parcial 
![Texto Alt](/src/paralelo/proceso.png "Propuestas")

### Descomposición del dominio:
Encontramos:
* Lectura de archivos (Entrada)
  En este punto, el proceso de lectura de archivos según la propuesta mencionada en la introducción del ducumento, cada archivo sera leido y despues procesado por un procesado como se muestra en la propuesta 2 de la figura 1.
* Archivos con las 10 mayores frecuencias
  Posterior del procesamiento de los archivos y encontrado las 10 mejores frecuencias en cada uno, se hace una ultima comparación con el objetivo de generar solo las 10 mejores frecuencias entre todo los archivos. Esto puede ser evidenciado en la figura 2.

### Descomposición funcional:

## Asignación de tareas

## Aglomeración

## Mapeo



### Referencias

* PARALELIZACION DE ALGORITMOS EN PLATAFORMAS DISTRIBUIDAS: CASO DE ESTUDIO EN PROCESAMIENTO SISMICO EN LA INDUSTRIA PETROLERA, Universidad Javerina, https://repository.javeriana.edu.co/bitstream/handle/10554/15073/LinaresMorenoCamiloAntonio2014.pdf?sequence=1
