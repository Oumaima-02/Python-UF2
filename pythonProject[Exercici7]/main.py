import functions as f
def main():
    s=f.size()
    num=f.list_num(s)
    mitj=f.mitj_num(num)
    max=f.val_max(num)
    min=f.val_min(num)

    print("La mitjana és: ", mitj)
    print("El valor máxim és: ", max)
    print("El valor mínim és: ", min)
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
