
import functions as f
MSG="Introdueix quants llibres es volen registrar:"
def main():
    reg=int(input(MSG))
    i=0
    while i<reg:
        dict=f.make_dict()
        print(dict)
        i+=1
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
