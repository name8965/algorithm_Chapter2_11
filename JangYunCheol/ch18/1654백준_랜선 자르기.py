k,n = map(int,input().split())

lans = []
for _ in range(k):
    lans.append(int(input()))
start =1
end = max(lans)

while start<=end:
    total =0
    mid = (start + end) // 2
    for i in lans:
        total+=i//mid
    if total >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)