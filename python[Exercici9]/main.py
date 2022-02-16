#Demanar per teclat un nombre en format binari (<=7 dígits) i retornar el valor en decimal.
import functions as f
MSG="Introdueix el nombre binari de 7 dígits com a màxim: "
def main():
    llista=list()
    num= (input(MSG))
    llista.append(num)
    while len(num) > 7:
        print("Número no vàlid")
        num = (input(MSG))
        llista.append(num)
    bin = f.validate(num)
    result=f.conversor(bin)
    print(result)
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
