from mpi4py import MPI
import pandas as pd

comm = MPI.COMM_WORLD
rank = comm-Get_rank()

if rank == 0:
    sub = input("Ingrese la palabra, para salir ingrese \"/\" : " )
    comm.send(sub,dest=1)
    comm.send(sub,dest=2)

    data = pd.read_csv("/opt/datasets/articles1.csv",usecols=[1,2,9])
else if rank == 1:
    sub = comm.recv(source = 0)
    data = pd.read_csv("/opt/datasets/articles2.csv",usecols=[1,2,9])

else if rank == 2:
    sub = comm.recv(source = 0)
    data = pd.read_csv("/opt/datasets/articles3.csv",usecols=[1,2,9]) 
