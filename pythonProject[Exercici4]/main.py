import functions as f
def main():
    n=f.notas()
    mit_apro, mit_sus, i_apro, i_sus = f.validate(n)
    print("LA mitja d'aprovats es: ", mit_apro)
    print("La quantitat d'aprovats: ", i_apro)
    print("LA mitja de suspesoses: ", mit_sus)
    print("La quantitat de suspesos: ", i_sus)
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
