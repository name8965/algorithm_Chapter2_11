n,m = map(int,input().split())
lst = list(map(int,input().split()))

end=max(lst)
start =1
while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in lst:
        if(i>=mid):
            total+=(i-mid)
    if total>=m:
        start = mid+1
    else:
        end = mid-1
print(end)
