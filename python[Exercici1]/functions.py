def validate():
    i = 0
    while i < 3:
        num = int(input("Introdueix un número entre 10 i 5000: "))
        if num < 10 or num > 5000:
            num = int(input("Introdueix un número entre 10 i 5000: "))
            i=i+1
        else:
            i = 3
    return num, i