def size():
    s=int(input("Quants números vols introduir?"))
    while s<1 or s>50:
        print("El valor no es vàlid: ")
        s=int(input("Quants números vols introduir?"))
    return s

def list_num(s):
    llista= list()
    i=0
    while i<s:
        num=int(input("introdueix un valor entre 0 al 10:"))
        while num<0 or num>10:
            print("El valor no és vàlid.")
            num = int(input("introdueix un valor entre 0 al 10:"))
        llista.append(num)
        i = i + 1
    return llista

def mitj_num(num):
    sum, i=0,0
    for x in num:
        sum=sum+x
        i+=1
    return sum/i

def val_max(num):
    max_value = None
    for x in num:
        if max_value is None or x > max_value:
            max_value = x
    return max_value


def val_min(num):
    min_value=None
    for x in num:
        m=min(num)
    return m