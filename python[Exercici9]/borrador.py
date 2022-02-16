def val_bin(bin):
    xifres=0
    if bin==0:
        xifres=1
    elif bin<0:
        num=num*-1
    else:
        while bin !=0:
            bin=bin//10
            xifres+=1
        if xifres>7:
            print("El número no és vàlid.")
    return bin




bin=f.validate(num)

bin2 = f.val_bin(bin)
