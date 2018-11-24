from mpi4py import MPI
import pandas as pd

#inicializacion de variables
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
direc = "/opt/datasets/articles" + str(rank+1) + ".csv"

#ciclo infinito
while(True):
    #pedir la palabra y enviarla
    if rank == 0:
        sub = input("Ingrese la palabra, para salir ingrese \"/\" : " )
        comm.send(sub,dest=1)
        comm.send(sub,dest=2)

    #recibir la palabra    
    elif rank == 1:
        sub = comm.recv(source = 0)

    elif rank == 2:
        sub = comm.recv(source = 0) 

    #si se ingresa / terminar el programa
    if(sub == "/"):
        return 0

    if rank <= 2:
        #inicializando el archivo correspondiente
        data = pd.read_csv(direc,usecols=[1,2,9])

        #calculando la frecuencia de la palabra
        data["frec"] = data["content"].str.count(sub.upper()) + data["content"].str.count(sub.lower()) + data["content"].str.count(sub.capitalize())
        
        #organizando de menor a mayor el archivo
        data = data.sort_values(by='frec',ascending=False)

        # enviando al rank 0 las 10 primeras filas de la data
        if rank != 0:
            comm.send(data.iloc[0:10,[3,0,1]], dest = 0)
        
        #reciviendo las tablas
        else:

            data = data.iloc[0:10,[3,0,1]]
            data1 = comm.recv(source = 1)
            data2 = comm.recv(source = 2)
            
            #uniendo las tres tablas
            data = pd.concat([data, data1, data2])

            #ordenando de mayor a menor por frecuencia
            data = data.sort_values(by='frec',ascending=False)
            
            #mostrar los datos en pantalla
            with pd.option_context('display.max_rows', None, 'display.max_columns', None):     
                print(data.iloc[0:10])
