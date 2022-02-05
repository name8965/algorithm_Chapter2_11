import sys
input = sys.stdin.readline




N = int(input())
lst = list(map(int, input().split()))
money = int(input()) # 예산
start = 0
end = max(lst)

while start <= end:
    mid = (start + end) // 2
    total = 0

    for i in lst:
        total += min(i, mid)
    if total>money:
        end = mid - 1
    if total <= money:
        start = mid + 1
print(end)



