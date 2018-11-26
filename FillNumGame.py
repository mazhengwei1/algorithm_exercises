'''
    算法描述题
x           算
--------------
  题题题题题题
  
填数游戏,共有5个汉字,每个汉字都可以为数字0-9中一个,分别用0-9替换汉字,验证计算结果
是否和列出的等式相等,若想等,找到一个正确答案
解题思路:要使算式成立,"算"和"题"不能为0
n1 = 算,n2=法,n3=描,n4=述,n5=题
'''
import time
def main():
    Stime = time.time()
    for n1 in range(1,10):
        for n2 in range(0,10):
            for n3 in range(0,10):
                for n4 in range(0,10):
                    for n5 in range(1,10):
                            multi = n1*10000 + n2*1000 + n3*100 + n4*10 + n5
                            result = int(str(n5)*6)
                            if multi * n1 == result:
                                if n1 != n2 != n3 != n4 != n5:
                                    Etime = time.time()
                                    UseTime = Etime - Stime
                                    print("一共花费",UseTime,"秒的时间!")
                                    print("原式为:")
                                    print("%7d"%multi)
                                    print("x%6d"%n5)
                                    print("%s"%("-"*7))
                                    print("%7d"%result)

if __name__ == "__main__":
    main()
