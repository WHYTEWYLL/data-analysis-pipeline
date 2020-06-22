from argparse import ArgumentParser
from dotenv import load_dotenv
import requests
from selenium import webdriver
import os 
import time 
from fpdf import FPDF

def getobjetives():
    """
    Funcion, que captura los parametro de la terminal
    """
    parser= ArgumentParser(description="Encuentra peliculas de un actor y donde verlas. ")
    parser.add_argument("--Name",dest="name",type=str,help="Type a name  Capitalize form")
    parser.add_argument("--Platform",dest="platform",type=str,help="(Netflix | Hulu | Prime Video |Disney+) Default = *")
    return parser.parse_args()

def apicall(pelicula,apikey):
    """
    Conexion a la API, y obtencion de los datos seleccionados
    """
    try:
        res=requests.get("http://www.omdbapi.com/",{"t":f"{pelicula}","apikey":f"{apikey}"})
        data=res.json()
        datos={
        "Actors":data["Actors"].split(",")[0],
        "imdbID":data["imdbID"],
        "Cartel":data["Poster"],
        "IMDBp":data["imdbRating"]}
        return datos
    except Exception as e:
        datos={
        "Actors":None,
        "imdbID":None,
        "Cartel":None,
        "IMDBp":None}
        return datos

def queplataforma(row):
    """
    Creacion de una nueva columna en funcion de los valores lineas del dataframe
    """
    platforms = ["Netflix","Hulu","Prime Video","Disney+"]
    if all([row[plat]]==1 for plat in platforms):
        return "All platforms" 
    else:
        return "/".join([plat for plat in platforms if row[plat]])

def fotopeli(pelisdisponibles):
    """
    Despliega una ventana , permitiendo visualizar los cartesles de las peliculas
    """
    for enlace in pelisdisponibles:
        print(enlace)
        driver = webdriver.Safari()
        driver.get(enlace)
        time.sleep(4)
        driver.close()

def grafico(name,platform,datamovie):
    """

    """
    if name==None:
        print(datamovie)
        graf2=datamovie["Platform"].value_counts().plot.pie(legend=False)
        fig = graf2.get_figure()
        plot=fig.savefig("Output/Plot.png")
    else:
        print(datamovie)
        graf1=datamovie[datamovie["Actors"]==name].groupby(["Platform","Title"]).size().unstack().plot.bar(stacked=True)
        fig = graf1.get_figure()
        fig.savefig('Output/Plot.png')

def pdfecito(name,platform):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(40, 10, 'Report: Platforms')
    pdf.ln(10)
    pdf.set_font('Arial', '', 14)
    pdf.ln(10)
    pdf.set_font('Arial', '', 14)
    pdf.cell(40, 15, f'Parametros de Busqueda: 1-{name} , 2-{platform}')
    pdf.ln(10)
    pdf.cell(40, 20, 'Los datos reflejan cual es la plataforma que más se asemeja a tus deseos.')
    pdf.ln(20)
    pdf.image(x=pdf.get_x(),y=pdf.get_y(),w=320/2 ,h=240/2,type="png",name="Output/Plot.png")
    pdf.output('Output/Report.pdf', 'F')
    return True