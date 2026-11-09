def insertionSort(a):
    n = len(a)
    if n <= 1:
        return
    for i in range(1, n):
        key = a[i]         
        j = i - 1
        #prochází čisla a hledá jestli čislo které momentálně našel je menší než předchozí číslo
        while j >= 0 and key < a[j]: 
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key 
a = [9,5,7,3,1,2]
insertionSort(a)
print(a)