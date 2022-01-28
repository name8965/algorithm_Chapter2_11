def fac(n):
    if n<=1:
        print(1)
        return

    result = 1
    for i in range(n):
        result *= n-i
    print(result)

"""
def fac2(num):
    if num<=1:
        return 1

    return num * fac2(num-1)
"""


fac(1)
# print(fac2(5))
