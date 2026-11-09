cisla = [9,5,7,3,1,2]
def selection_sort(cisla):
    m = len(cisla)
    for i in range(m-1):
        min_cislo = i
        #prochází čísla postupně a a hledá nejmenší číslo
        for j in range(i+1, m):
            if cisla[j] < cisla[min_cislo]:
                min_cislo = j
                #když najde nejmenší číslo tak ho hodí na první pozici
        min_hodnota = cisla.pop(min_cislo)
        cisla.insert(i, min_hodnota)
selection_sort(cisla)
print(cisla)