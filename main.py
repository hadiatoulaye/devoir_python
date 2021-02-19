# exercice1 traité
def tableau():
    tab = [1,2,3,4,5]
    tab.reverse()
    print(tab)
tableau()


#exercice2 traité
def chaine_caractere (ch = "alpha", ch2 = "mamadou"):
    m = []
    for i in ch:
        for j in ch2:
            if i == j:
                if i not in m:
                    m.append(i)
    print(m)
    return m
chaine_caractere()


def chaine_caractere (ch = "klbc", ch2 = "kaba"):
    hadia = []
    for i in ch:
         for j in ch2:
             if i == j:
                if i not in hadia:
                    hadia.append(i)
    print(hadia)
    return hadia
chaine_caractere()


# exercice3 traité

def table_return(nombre1, nombre2):

    table_return = []
    for hadia in nombre1:
        if hadia not in nombre2:
            if hadia not in table_return:
                table_return.append(hadia)
    for hadia in nombre2 :
        if hadia not in nombre1:
            if hadia not in table_return:
                table_return.append(hadia)
    return table_return
result = table_return([2, 4, 7, 8, 2], [1, 3, 9, 4, 6, 7])
print(result)
