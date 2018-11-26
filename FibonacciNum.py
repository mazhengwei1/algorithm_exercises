"""
用递归算法打印出前200位斐波那契额数
 1 1 2 3 5 8 13 21 34 55 ...

算法思路: n+n1=n2 , n,n1 = n1,n2
"""

total = 50   #50个数
times = 2      #当前个数
def Fib(num1,num2):
    global times, total
    if times == total:
        return True
    times += 1
    num3 = num1 + num2
    print(num3, ",", end="")
    Fib(num2,num3)
    


if __name__ == "__main__":
    num1 = 1
    num2 = 1
    print(num1, ",", num2, ",", end="")
    Fib(num1, num2)

    




