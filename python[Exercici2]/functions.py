def time():
    num = int(input("introdueix el nombre de segons: "))
    s = num
    min = num // 60
    h = num // 3600
    d = num // 86400
    return s,min,h,d