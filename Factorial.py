"""
求N的阶乘(n!).
n! = n * (n-1) * (n-2) * ..... * 2 * 1
如:
6的阶乘为: 6*5*4*3*2*1 = 720

"""
def main(num):
    if num == 1:
        return 1
    return num * main(num - 1)
    

if __name__ == "__main__":
    num = int(input("请输入要计算阶乘的数字:"))
    num1 = main(num)
    print(num, '的阶乘为:', num1)
