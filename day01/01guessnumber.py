#用户猜数基本要求
'''
import random
n = random.randint(1,100)
print(n)
while True:
    num = int(input('please input your num:'))
    if n == num:
        print('您猜对了！')
        break
    elif n < num:
        print('您猜大了')
        continue
    else:
        print('您猜小了')
        continue
'''
#升级要求
import random
n = random.randint(1,100)
print(n)
num1 = 100
num2 = 0
while True:
    print("您好，请猜数，范围" +str(num2)+"-"+str(num1)+":")
    num = int(input('please input your num:'))
    if n == num:
        print('您猜对了！')
        break
    elif n < num:
        num1 = num
        print('您猜大了')
        continue
    else:
        print('您猜小了')
        num2 = num
        continue