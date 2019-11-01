# #  ctrl+?  全注释
# print('shuaiqi')
# print(10/3)
# print(1000/300)
#
# print(-10%3)
# print("问能提笔安天下，\n"
#       "武能上马定乾坤。\n"
#       "心存谋略何人胜,\n"
#       "古今英雄唯是君。")
#
# print('''
#       问能提笔安天下，
#       武能上马定乾坤。
#       心存谋略何人胜,
#       古今英雄唯是君。
# ''')
#
# a  = """
#       文能提笔安天下，
#       武能上马定乾坤。
#       心存谋略何人胜,
#       古今英雄唯是君。
# """
#
# aa = "文能提笔安天下，\n" \
#      "武能上马定乾坤。\n" \
#      "心存谋略何人胜,\n" \
#      "古今英雄唯是君"
#
#
# print("a得值是:%s " % a)
# print("aa得值是:%s" % a)
'''
shui = input('请输入您得月工资：')
a = int(int(shui)* 0.8)
print('您得税后工资是%s元'% a)

salary = input(input('please input your salary:'))


print(salary)

number_one = int(input('请输入第一个数字：'))
number_two = int(input('请输入第二个数字:'))
if number_one > number_two:
    print("比较大得数字是第一次输入得数：",number_one)
else:
    print("比较大得数字是第二次输入得数：",number_two)
'''
####
# money = int(input('请输入你得工资:'))
# if money < 6000:
#     print('只能吃泡面了')
# elif money < 8000:
#     print('小包间')
# elif money < 12000:
#     print('大保健')
# else:
#     print('买个房子')


'''
username = 'alex'
password = '123'
user = input('请输入您得用户名:')
if user == username:
    pass1 = input('请输入您得密码:')
    if pass1 == password:
        print('恭喜您，认证通过')
    else:
        print('您得密码输入错误，请重试！')
else:
    print('没有这个用户，请重新输入')
    user = input('请输入您得用户名:')
    if user == username:
        pass1 = input('请输入您得密码:')
        if pass1 == password:
            print('恭喜您，认证通过')
        else:
            print('密码不正确')
    elif user != username:
        print('账号不存在')
    else:
        print('您得账户已经锁定')
'''


# counter = 1
# while counter <= 100:
#     print(counter,'次我爱你')
#     counter = counter + 1

#1-2+3-4+5..99 的所有数的和
counter = 1
temp = 0
while counter <= 100:
    if counter %2:
        temp = temp + counter
    else:
        temp = temp - counter
    counter = counter + 1
print(temp)


print(bool(0))








