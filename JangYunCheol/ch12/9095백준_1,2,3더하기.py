

def myplus(n:int):

#1 1
#2 2
#3 4 1+1+1/ 1+2/2+1/3
#4 7
#5 13
#6 24

    if n ==1:
        return 1
    elif n == 2:
        return 2
    elif n==3:
        return 4
    else:

        return myplus(n-1)+myplus(n-2)+myplus(n-3)

def myplus2(sum,n):
    count = 0
    if sum==n:
        count +=1
        return count
    if sum>n:
        return count
    for i in range(1,4): #1부터 3까지
        count += myplus2(sum+i,n)
    return count


print(myplus2(0,4))
#
# n = int(input())
#
# a = [-1] * n
#
# for i in range(n):
#     a[i] = int(input())
#
# for i in range(n):
#     print(myplus(int(a[i])))