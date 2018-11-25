# Versión paralela indiv (con MPI)

## Pre-requisitos

### instalar python3

        
        $ sudo apt-get update
        $ sudo apt-get install python3
        

### instalar pip

        
        $ sudo apt-get install python-pip3
        

### instalar libreria pandas con pip

        
        $ pip3 install pandas
        

### instalar libreria numpy con pip

        
        $ pip3 install numpy
        

### instalar libreria mpi4py con pip

        
        $ pip3 install mpi4py
        

### crear un archivo hosts_mpi con el host

    en nuestro caso se creo en la carpeta src/paralelo/

    para verlo en la carpeta src/paralelo/

        
        $ cat hosts_mpi
        
### preparar el master y los esclavos (esta parte es tomada del documento Readme.md del laboratorio de MPI)
autor original
Edwin Montoya M. – emontoya@eafit.edu.co

#### 1. conectar a la VPN
        
        $ ssh user-vpn@192.168.10.80
        Password: pass-vpn
        

#### 2. verificar que se conecte a los 2 slaves SIN password.
        
        $ ssh user-vpn@192.168.10.81

        $ ssh user-vpn@192.168.10.82
        

SI le pide password alguno de los 2 slaves anteriores, por favor realice el paso de la Instalación Manual de las claves. (numeral 3)

#### 3. instalar las claves ssh para cada usuario (solo se hace una vez):

// conectar a master:
        
        $ ssh user-vpn@192.168.10.80
        Password: pass-vpn
        $ mkdir ~/.ssh
        $ ssh-keygen -t rsa -b 4096 -C "your_username@eafit.edu.co"

// de enter a todas las opciones

        $ cd .ssh
        $ cp id_rsa.pub authorized_keys
        $ scp ~/.ssh/id_rsa ~/.ssh/id_rsa.pub user-vpn@192.168.10.81:
        Password: pass-vpn
        $ scp ~/.ssh/id_rsa ~/.ssh/id_rsa.pub user-vpn@192.168.10.82:
        Password: pass-vpn

// conectar a slave1:
       
        $ ssh user-vpn@192.168.10.81
        Password: pass-vpn        
        $ mkdir ~/.ssh
        $ cp ~/id_rsa ~/id_rsa.pub ~/.ssh
        $ cd ~/.ssh
        $ cp id_rsa.pub authorized_keys
        $ exit


// conectar a slave2:
        
        $ ssh user-vpn@192.168.10.82
        Password: pass-vpn
        $ mkdir ~/.ssh
        $ cp ~/id_rsa ~/id_rsa.pub ~/.ssh
        $ cd ~/.ssh
        $ cp id_rsa.pub authorized_keys
        $ exit



## Ejecutar


    En el cluster de hpc - src/paralelo ejecutar

        
	$ mpiexec -f hosts_mpi -np 3 /opt/anaconda3/bin/python3 ./indinv-mpi.py
        
