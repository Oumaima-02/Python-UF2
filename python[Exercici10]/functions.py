import functions as f
def make_dict():
    dict={}
    titol=input("Introdueix el títol del llibre :")
    autor=input("Introdueix l'autor/a: ")
    edit=input("Indica l'editorial:")
    data=f.date()
    unit=int(input("Unitats disponibles="))
    usr=input("Usuaria que el té: ")
    temps=int(input("Indica en dies el temps prestat: "))
    dict["Títol"]=titol
    dict["Autor/a"]=autor
    dict["Editorial "] = edit
    dict["Data"] = data
    dict["Unitats disponibles"] = unit
    dict["Usuari que ho ha agafat"] = usr
    dict["Temps prestat"] = temps
    return dict
def date():
    print("Data ==> ")
    any=int(input("any: "))
    mes=int(input("Mes:"))
    while mes<1 or mes>12:
        print("T'has equivocat al introduir el mes. Torna a itroduir-lo.")
        mes = int(input("Mes:"))
    dia=int(input("dia : "))
    if mes==2:
        while dia<1 or dia>28:
            print("Dia incorrecte. Torna a introduir-lo.")
            dia = int(input("dia : "))
    elif mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
        while dia<1 or dia>31:
            print("No es correcte, torna a introduir-lo.")
            dia = int(input("dia : "))
    else:
        while dia<1 or dia>30:
            print("No es correcte, torna a introduir-lo.")
            dia = int(input("dia : "))
    return dia, mes, any
