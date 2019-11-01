username = "alex"
password = "123"
num = 1
while num <= 3:
    user = input('please input you are username:')
    passw = input('please input you are password:')
    if user == username and passw == password:
        print('登录成功,您的登录次数为:',num)
        break
    else:
        print('用户名或者密码错误,您的可用登录次数为',3-num)
        num += 1
