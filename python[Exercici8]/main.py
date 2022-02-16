import functions as f
MSG ="Introdueix el número de la base: "
ASK_EXPO="Introdueix el número d'exponent: "
def main():
    num=int(input(MSG))
    y=int(input(ASK_EXPO))
    x=f.potencia(num, y)
    print(f"{num}^{y}")
    print ("El resultat és :", x)
if __name__ == '__main__':
    main()