#Horoskop
from flask import Flask
from random import randrange

def hämta_förutsägelser(filnamn):
    x = ""
    förutsägelselista = []
    try:
        with open(filnamn,"r") as infil:
            for rad in infil:
                förutsägelselista.append(rad.strip())
    except FileNotFoundError:
        x = "Filen fanns inte"
    return förutsägelselista

def slumpa(förutsägelselista):
    antal = len(förutsägelselista)
    slump = randrange(antal)
    förutsägelse = förutsägelselista[slump]
    return förutsägelse

app = Flask(__name__)

@app.route('/')
def horoskop():
    filnamn = "static/texter.txt"
    förutsägelselista = hämta_förutsägelser(filnamn)
    förutsägelse = slumpa(förutsägelselista)

    htmlkod = " "
    htmlkod += ""
    htmlkod += "  "
    htmlkod += förutsägelse
    htmlkod += " "
    return htmlkod