'''
print('文能提笔安天下，\n'
      '武能上马定乾坤，\n'
      '心存谋略何人胜，\n'
      '古今英雄唯是君。')
'''

'''
age = int(input("please input your age:"))
if age < 10:
    print('小屁孩')
elif age < 20:
    print('青春期')
elif age < 30:
    print('dingxing')
elif age < 40:
    print('结婚')
elif age < 50:
    print('不听话的小屁孩')
elif age < 60:
    print('自己变成老屁孩')
elif age < 70:
    print('或者不错的老屁孩')
elif age < 90:
    print('快结束了了')
else:
    print('在家了这个世界')
'''

#
#.求100以内所有数的和
#1+2+3+4+...+100

# n = 0
# s = 0
# while n <= 100:
#     print(n)
#     s = s + n
#     n += 1
# print(s)

1,3,5,7,9

# i = 0
# while i < 100:
#     if i %2 == 1:
#         print(i)
#     i += 1


# i = 0
# while i < 100:
#     if i %2 == 0:
#         print(i)
#     i += 1


#1-2+3-4+5 ... 99的所有数的和
# n = 1
# s = 0
# while n < 100:
#     if n % 2 == 0:
#         s = s - n
#     else:
#         s = s + n
#     n += 1
# print(s)


# n = 1
# s = 0  # s是之前所有数的总和
# while n < 100:
#     temp = n % 2
#     if temp == 0:
#         s = s - n
#     else:
#         s = s + n
#     n = n + 1
#
# print(s)
# start = 1
# sum = 0
# while start <100:
#     temp = start % 2
#     if temp ==1:
#         sum = sum + start
#     else:
#         sum = sum - start
#     #print(start)
#     #sum = sum + 1
#     start += 1
# print(sum)

# i = 361
# temp = 0
# while i <= 460:
#     temp = temp + i
#     i +=1
# print(temp)


#1 - 3 + 5 - 7 + 9…99 = ?
print(sum(range(1,99,4))-sum(range(3,100,4)))