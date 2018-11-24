from mpi4py import MPI
import pandas as pd

#inicializacion de variables
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
direc = "/opt/datasets/articles" + str(rank+1) + ".csv"

#inicializando el archivo correspondiente
if rank <= 2:
    data = pd.read_csv(direc,usecols=[1,2,9])
    data["frec"] = dataFinal["content"].str.count(sub.upper()) 
    + dataFinal["content"].str.count(sub.lower()) 
    + dataFinal["content"].str.count(sub.capitalize())

#pedir la palabra
if rank == 0:
    sub = input("Ingrese la palabra, para salir ingrese \"/\" : " )
    comm.send(sub,dest=1)
    comm.send(sub,dest=2)
    
elif rank == 1:
    sub = comm.recv(source = 0)

elif rank == 2:
    sub = comm.recv(source = 0) 

if rank <= 2:
    data = data.sort_values(by='frec',ascending=False)
    if rank != 0:
        comm.send(data.iloc[0:10], dest = 0)
    else:
        data = data.iloc[0:10]
        data1 = comm.recv(source = 1)
        data2 = comm.recv(source = 2)
        print( "------------0------------")
        print (data)
        print ("-------------1--------------")
        print (data1)
        print ("---------------------2---------------")
        print (data2)
