#retornar una seqüència de números que sumant-los el resultat ha de ser >= al num introduït.
import functions as f

def main():
    num= int(input ("Introdueix un número: "))
    x=f.num_seq(num)
    print("La seqüència és: ", x)

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
