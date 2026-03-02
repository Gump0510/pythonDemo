    # 11.py
import sys

def jia(x, y):
    """This function adds two numbers"""
    return x + y

def jian(x, y):
    """This function subtracts two numbers"""
    return x - y

def cheng(x, y):
    """This function multiplies two numbers"""
    return x * y

def chu(x, y):
    """This function divides two numbers"""
    if y == 0:
        #raise ValueError("除数不能为")
        print("除数不能为0")
        sys.exit(1)
    return x / y

if __name__ == "__main__":
    print("加减乘除")
    shu1= float(input("输入第一个数: "))
    shu2 = float(input("输入第二个数: "))
    
    print("输入: 1.加2.减3.乘4.除")
    xuanze= input("请选择: ")
    
    if xuanze == '1':
        print(f"{shu1} + {shu2} = {jia(shu1, shu2)}")
    elif xuanze == '2':
        print(f"{shu1} - {shu2} = {jian(shu1, shu2)}")
    elif xuanze == '3':
        print(f"{shu1} * {shu2} = {cheng(shu1, shu2)}")
    elif xuanze == '4':
        print(f"{shu1} / {shu2} = {chu(shu1, shu2)}")
    else:
        print("选择错。")
