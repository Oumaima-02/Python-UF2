def num_seq(num):
    i, sum = 0, 0
    llista = list()
    while i < num:
        sum = sum + i
        if sum < num:
            llista.append(i)
        i = i + 1
    return llista
