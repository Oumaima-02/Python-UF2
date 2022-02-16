import functions as f
def main():
    num1=int(input("Introdueix el primer número:"))
    num2=int(input("Introdueix el segon número: "))

    num1,num2=f.intercanvi(num1,num2)

    print("Els numeros intercanviats: ")
    print( "Número 1:", num1)
    print("Número 2:",num2)

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
