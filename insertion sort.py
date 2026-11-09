a = [9,5,7,3,1,2]
def insertion_sort(a):
    #prochází čísla v listu
    for i in range(1, len(a)):
        j=i
        #hledá dokuď nenajde číslo které je menší než číslo predchozí
        while j > 0 and a[j-1] > a[j]:
            #přemění čislo v pravo na číslo vlevo a číslo vlevo na číslo na pravo
            a[j-1], a[j] = a[j], a[j-1]
            #koukne se jesli je číslo které momentálně přeměníl menší než číslo předchozí, pokuď ano znovu ho přemění
            j -= 1
    return a
insertion_sort(a)
print(a)