def notas():
    notes = list()
    i = 0
    while i < 15:
        nota = int(input("Introdueix una nota: "))
        while nota < 1 or nota > 10:
            nota = int(input("Introdueix una nota: "))

        notes.append(nota)
        i = i + 1
    return notes
def validate(n):
    apro_sum,i_apro, sus_sum, mit_apro, i_sus, mit_sus=0,0,0,0,0,0
    for x in n:
        if x>=5:
            apro_sum=apro_sum+x
            i_apro=i_apro+1
        else:
            sus_sum=sus_sum+x
            i_sus=i_sus+1

    mit_apro=apro_sum/i_apro
    mit_sus=sus_sum/i_sus

    return mit_apro, mit_sus, i_apro, i_sus