import pandas as pd

def mining():
    try:
        a = []
        sub = input("Entrar la palabra entre \" para quitar \"/\" : " )
        
        #Saliendo
        if(sub == "/"):
            return 0

        #Abiendo documentos
        data = pd.read_csv("/opt/datasets/articles1.csv",usecols=[1,2,9])
        data1 = pd.read_csv("/opt/datasets/articles2.csv",usecols=[1,2,9])
        data2 = pd.read_csv("/opt/datasets/articles3.csv",usecols=[1,2,9])
        
        #concatenar documentos
        dataFinal = pd.concat([data, data1, data2])
        
        #creando datos
        sub = sub.lower()
        subMax = sub.upper()
        subCap = sub.capitalize()
        
        #calculando el numero que esta la palabra
        dataFinal["frec"] = dataFinal["content"].str.count(sub) + dataFinal["content"].str.count(subMax) + dataFinal["content"].str.count(subCap)
        #ordenando de mayor a menor por numero de palabra
        dataFinal = dataFinal.sort_values(by='frec',ascending=False)
        
        #imprimiendo
        print(dataFinal.iloc[0:10,[3,0,1]])
    except:
        mining()
        

mining()
