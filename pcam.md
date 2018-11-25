# DISEÑO REALIZADO BAJO LA METODOLOGIA PCAM

Este caso se puede abordar desde diferentes enfoques en razon a la finalidad del programa segun la información.
Un primer enfoque de paralelismo se presenta en que cada columna debe ser contada de manera independiente, es decir, su resultado no depende del la información de la celda anterior, es asi como se puede considerar que segun la cantidad de celdas en la columna un numero determinado de procesadores se encargue del conteo de la palabra en cada noticia. El otro enfoque se da a partir de la cantidad de archivos a analizar, es por esto que se puede descomponer el numero de procesadores a utlizar basados en la cantidad de archivos a analizar basados en este problema especifico.

### ![Texto Alt](/propuesta.png "Propuestas")
Figura 1. Propuestas

La solución implementada se sustenta bajo la segunda propuesta, esta propuesta será desarrollada en base a las 4 faces que propone la metodologia PCAM.

## Descomposición de tareas
Proceso parcial 
### ![Texto Alt](/proceso.png "Descomposición")
Figura 2. Descomposición

### Descomposición del dominio:
Encontramos:
* Lectura de archivos (Entrada):
  En este punto, el proceso de lectura de archivos según la propuesta mencionada en la introducción del ducumento, cada archivo sera leido y despues procesado por un procesado como se muestra en la propuesta 2 de la figura 1.
* Archivos con las 10 mayores frecuencias: 
  Posterior del procesamiento de los archivos y encontrado las 10 mejores frecuencias en cada uno, se hace una ultima comparación con el objetivo de generar solo las 10 mejores frecuencias entre todo los archivos. Esto puede ser evidenciado en la figura 2.

### Descomposición funcional:
Haciendo el desglose funcional de las tareas encontramos las siguientes, este proceso se evidencias en la figura 2.
1. Ingreso de la palabra a buscar
2. Generar posibles combinaciones de la palabra, por ejemplo si se ingresa "casa" los terminos a buscar serian "casa", "Casa" y "CASA". 
3. Lectura de archivos que contiene las noticias
4. Conteo de palabras por noticia.
5. Generación de las 10 noticias con el mayor numero de palabras por archivo
6. Recopilación de datos por cada archivo
7. Generación de las 10 noticias con el mayor numero de palabras por todos los archivos.
8. Ordenar de mayor a menor segun el numero
9. Impresión de resultados. 


## Asignación de tareas
Siguiendo en linea de la fase de descomposición funcional se denota entonces segun la necesidad del problema, teniendo en cuenta la cantidad de datos y archivos a procesar, siguiendo entonces el estandar del mpi para definir un esquema de comunicación estructura de las funciones se identificaron entonces las siguientes funciones que deberan ser asignadas a un procesador o maquina esclava con el objetivo de aumentar el rendimiento.

### ![Texto Alt](/procesador.png "Procesador")
Figura 3. Ilustraccion de tareas para el procesador

## Aglomeración

Para el tercer paso, es necesario entender la posibilidad de particionar las tareas repetitivas pero independientes en diferentes procesadores, para asi obtener mejores velocidades en el momento de buscar la frecuencia de una palabra en una noticia, posterior a esto, recopilar estas frecuencias y definir las 10 con mayor numero.

## Mapeo

### ![Texto Alt](/diMaEs.png "Esquema Maestro-Esclavo")
Figura 3. Esquema Maestro-Esclavo

En esta etapa se definen y reestructuran las tareas que seran realizadas por cada nucleo, en la figura 4 se muestra un esquema donde se tiene un nodo maestro y 3 esclavos. En este caso el nodo maestro tendra a cargo el proceso de captar la palabra a buscar y a convertila en las diferentes posibilidades, el paso de las transformaciones a los nodos esclavos y a la recopilación de las frecuencias generadas por los nodos esclavos para que posterior dar las 10 mejores frecuencias. Los nodos esclavos tendrán la tarea de acceder, recopilar y analizar la frecuencia de la palabra ingresada en cada noticia y de recopilar las 10 mejores ordenadas de forma descendente. De esta manera, no se tiene comunicación entre los nos nodos esclavos con el fin de evitar la dependencia entre procesos.



### Referencias

* PARALELIZACION DE ALGORITMOS EN PLATAFORMAS DISTRIBUIDAS: CASO DE ESTUDIO EN PROCESAMIENTO SISMICO EN LA INDUSTRIA PETROLERA, Universidad Javerina, https://repository.javeriana.edu.co/bitstream/handle/10554/15073/LinaresMorenoCamiloAntonio2014.pdf?sequence=1

* Getting Started with Parallel Computing and Python
* Memorias del curso de topicos de telematica, modulo HPC
