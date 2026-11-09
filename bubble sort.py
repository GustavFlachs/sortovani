a = [9,5,7,3,1,2]
def buuble_sort(a):
    #převede list na hodnoty se kterýmy můžeme pracovat
    n = len(a)
    for p in range(n-1):
        #kontroluje zda se provedla výměna
        swapped = False
        #prochází páry čísel vedle sebe, pokuď číslo na levo je větší než číslo na pravo tak ho dá na levo a levé číslo dá do prava
        for i in range(n-1-p):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                #kontroluje zda se provedla výměna
                swapped = True
        #jestli se výměna nestala tak cyklus skončí
        if not swapped:
            print(a)
            break
buuble_sort(a)