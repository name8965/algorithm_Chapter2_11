

def quicksort(lst, start,end):
    def partition(plst,ps,pe):
        pivet = plst[pe]
        i = ps -1
        for j in range(ps,pe):
            if lst[j]<=pivet:
                i+=1
                lst[i],lst[j] = lst[j],lst[i]
        lst[i+1],lst[pe] = lst[pe],lst[i+1]
        return i+1



    if start>=end:
        return None

    p = partition(lst,start,end)
    quicksort(lst,start,p-1)
    quicksort(lst,p+1,end)

    return lst








assert quicksort([4, 6, 2, 9, 1], 0, 1) == [4, 6, 2, 9, 1]
assert quicksort([4, 6, 2, 9, 1], 0, 2) == [2, 4, 6, 9, 1]
assert quicksort([4, 6, 2, 9, 1], 0, 3) == [2, 4, 6, 9, 1]
assert quicksort([4, 6, 2, 9, 1], 0, 4) == [1, 2, 4, 6, 9]
assert quicksort([3, 2, 1, 5, 3, 2, 3], 0, 1) == [2, 3, 1, 5, 3, 2, 3]
assert quicksort([3, 2, 1, 5, 3, 2, 3], 0, 2) == [1, 2, 3, 5, 3, 2, 3]
assert quicksort([3, 2, 1, 5, 3, 2, 3], 0, 3) == [1, 2, 3, 5, 3, 2, 3]
assert quicksort([3, 2, 1, 5, 3, 2, 3], 0, 4) == [1, 2, 3, 3, 5, 2, 3]
assert quicksort([3, 2, 1, 5, 3, 2, 3], 0, 5) == [1, 2, 2, 3, 3, 5, 3]
assert quicksort([3, 2, 1, 5, 3, 2, 3], 0, 6) == [1, 2, 2, 3, 3, 3, 5]