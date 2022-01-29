import sys

def check(a):
    for i in range(len(a) - 1):
        if a[i + 1] is not None and a[i] == a[i + 1][:len(a[i])]:
            return "NO"
    return "YES"


tc = int(sys.stdin.readline())

for _ in range(tc):
    n = int(sys.stdin.readline())
    a = []

    for i in range(n):
        a.append(sys.stdin.readline().split())
        # a.append(str(int(sys.stdin.readline())))
    a.sort()


    print(check(a))
