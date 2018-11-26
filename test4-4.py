# 输出 1 到 10
count = 1
while count <= 10:
    print (count)
    count = count + 1

# 输出 1 到 10
for count in range(1,11):
    print (count)


# 把 nums 里的值从前向后累加
# 当总和超过 100 时则不再继续累加
nums = [23, 45, 8, 13, 50, 43, 21]
sum = 0
for n in nums:
    sum += n
    if sum > 100:
       break
# 满足条件时跳出循环
print(sum)

# 输出九九乘法口诀表
# 1 x 1 = 1
# 1 x 2 = 2, 2 x 2 = 4
# ...
for i in range(1, 10):
    for j in range (1,10):
        k = i * j
        print ('%d x %d = %d' %(i,j,k))
    print

for i in range(1, 10):
    for j in range (1,i+1):
        k = i * j
        print ('%d x %d = %d' %(i,j,k))
    print

for i in range(1, 10):
    for j in range(1,10):
        if i > j:
            print('%d x %d = %d' % (j, i, i * j))
        elif i == j:
            print('%d x %d = %d' % (j, i, i * j))
        else:
            continue