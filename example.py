print("hello world")
print("hello again")
print('hello')

print(3e30)

print(1+2*3)

print(2>5)


name=input("Who do you think I am?")
print(name,",","oh,yes!")

age=eval(input("how old are you?"))
print(age,"is too young!")

#打印自己的英文昵称
#打印一个含有加减乘除的数学表达式
#使用两次 print 语句，但只显示一行
#使用一次 print 语句，但显示在两行中

print("Jack")
print(2+3-4*5/2)
print("yy", end="")
print("zz")
print("rr \nss")

# 创建一个值为2.5的变量price，并将其输出

price = 2.5
print(price)



# 将 money 变量的值乘以 2 再加上 50
# 赋值给 result
money = 20
result = money * 2 + 50
print(result)

# 判断 a 是否大于 b，输出结果 result
a = 2.7 * 3.3
b = 2.3 * 3.7
result = a > b
print(result)

# 通过 % 将 name, age, code 拼接成一句话
# 输出 Crossin is 18, he write Python.
name = 'Crossin'
age = 18
code = 'Python'
result = "%s is %s, he write %s." % (name,age,code)
print(result)


num1 = '3.3'
num2 = 2.5

# 将 num1 转换为浮点数
num1 = float (num1)

# 再和 num2 相加后输出
print (num1+num2)

# 猜数字
num = 10
print ('Guess what I think?')
answer = int(input())

result = answer<num
print ('too small?')
print (result)

result = answer>num
print ('too big?')
print (result)

result = answer==num
print ('equal?')
print (result)


a = True
b = not a
#想想下面这些逻辑运算的结果，然后用print看看你想的对不对：
print(b)  #False
print(not b) #True
print(a == b) #False
print(a != b) #True
print(a and b) #False
print(a or b) #True
print(1<2 and b==True) #False