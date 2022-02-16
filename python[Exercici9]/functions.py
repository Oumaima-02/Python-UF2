def validate(num):
    i=0
    for x in num:
        if  x!='0' or x!='1':
            print("No és vàlid.")
        break
    return num
def conversor(bin):
    i=0
    dec=0
    bin=bin[::-1]
    for x in bin:
        mult=2**i
        dec+= int(x)*mult
        i+= 1
    return dec
