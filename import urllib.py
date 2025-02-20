import urllib.request

def räknaOrd(rad):
    orden = rad.split()
    antal = len(orden)
    return antal

def main():
    url = "https://www.gutenberg.org/cache/epub/4300/pg4300.txt"
    webbfil = urllib.request.urlopen(url)
    ordTotalt = 0
    lista_med_ord = []
    for i, rad in enumerate(webbfil):
        radSomSträng = rad.decode()
        ordTotalt += räknaOrd(rad)
        if i < 5:
            lista_med_ord.append(radSomSträng)
    print(ordTotalt)
    print(lista_med_ord)

if __name__== "__main__":
    main()

#PS C:\Users\joaki\HTMl_projekt> & C:/Users/joaki/AppData/Local/Microsoft/WindowsApps/python3.12.exe "c:/Users/joaki/HTMl_projekt/import urllib.py"
#268086
#['\ufeffThe Project Gutenberg eBook of Ulysses\r\n', '    \r\n', 'This ebook is for the use of anyone anywhere in the United States and\r\n', 'most other parts of the world at no cost and with almost no restrictions\r\n', 'whatsoever. You may copy it, give it away or re-use it under the terms\r\n']

#Om webbsida inte finns så får vi felutskriften: att webbsidan inte finns