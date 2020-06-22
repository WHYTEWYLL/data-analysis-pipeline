import pandas as pd
import requests
import numpy as np
from dotenv import load_dotenv
from Cosas.tools import *
from selenium import webdriver


#Cleaning Data
def datos():
    load_dotenv()
    df=pd.read_csv("Input/Movies.csv")
    movies=df.drop(["ID","Unnamed: 0","IMDb","Age","Genres","Language","Runtime","Directors","Country","Type"],axis=1)
    apiKey = os.getenv("ombKey")
    paraanadir=[apicall(x,apiKey) for x in movies["Title"][:1000]]
    plus=pd.DataFrame(paraanadir)
    movies_2=pd.concat([movies,plus] ,axis=1,sort=False)
    datamovie=movies_2[:991]

    lala=datamovie.apply(lambda row: queplataforma(row) ,axis=1)
 
    lolo=pd.DataFrame({"Platform":lala})
    final=pd.concat([datamovie,lolo] ,axis=1,sort=False)
    print(final)
    final.to_csv('Input/MoviesFull.csv',index=False)


#Filtering Data
def respuestapara(name,platform):
    try:
        datamovie=pd.read_csv("Input/MoviesFull.csv")
        
        if name==None and platform==None:
            pelisdisponibles=datamovie["Cartel"].sample()
            print("MATCH:")
            fotopeli(pelisdisponibles)
            print("Inicio de la creacion de graficos")
            grafico(name,platform,datamovie)
        elif len(np.where(datamovie["Actors"]==name))==0:
            print("No lo conozco ,prueba con otro y usa su nombres completo ")
            print(datamovie["Actors"])
        else:
            if platform:
                pelisdisponibles=datamovie[(datamovie[platform]==True) & (datamovie["Actors"]==name)]["Cartel"]
                fotopeli(pelisdisponibles)

            else:
                pelisdisponibles=datamovie[datamovie["Actors"]==name]["Cartel"]
                fotopeli(pelisdisponibles)
                grafico(name,platform,datamovie)

    except FileNotFoundError as e:
        print("El documento, no se ha encontrado.")
        print("Se procede a la creacion del archivo inexistente")
        datos()
        print("Completada la instalacion, ejecute de nuevo el programa")



