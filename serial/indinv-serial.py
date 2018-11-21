import pandas as pd

def mining():
    try:
        sub = input("Entrar la palabra entre \" para quitar \"/\" : " )
        if(sub == "/"):
            return 0
        data = pd.read_csv("/opt/datasets/articles1.csv",usecols=[1,2,9])
        data["frec"] = data["content"].str.find(sub)
        print(data)
    except:
        mining()
        


#def insertList():

mining()
