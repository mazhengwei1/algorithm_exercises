'''
在下面的算式中适当的添加"+,-,*,/"运算符,使等式成立(不适用括号)

            5  5  5  5  5  =  5

算法分析:通过训话你程序可枚举填入这4个运算符之一,然后再判断成立与否
    注意:1,当填入除号的时候,要求右侧的数不能为0
         2,乘除的运算级别比加减高
         第一点,在程序中添加一个判断语句,如果试算时填入的运算符是除,则其后面的数
                不能小于0,若为0,则跳过该次试算,直接进行下一轮计算
         第二点,需要考虑5+5-5*5/5=5
                在程序中可设置两个变量left和right,left用来保存上次的运算结果
                right用来保存下次将参加运算的数据

'''

import time

def main(nums, cos, result):
    cos = cos
    nums = nums
    result = result
    times = 0
    left = 0
    right = 0
    #print(co, nums)
    for c1 in cos:
        if c1 == "/" and right != 0:
            for c2 in cos:
                if c2 == "/" and right != 0:
                    for c3 in cos:
                        if c3 == "/" anf right != 0:
                            for c4 in cos:
                                if c4 == "/" anf right != 0:
                                    
                                    




if __name__ == "__main__":
    cos = ["+", "-", "*", "/"]
    nums = []
    for _ in range(5):
         num = int(input("请输入需要运算的数字:"))
         nums.append(num)
    result = int(input("请输入计算结果:"))
    #print(nums)
    main(nums,cos,result)
