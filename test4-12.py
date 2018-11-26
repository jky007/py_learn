#BMI 指数（即身体质量指数，简称体质指数又称体重，英文为Body Mass Index，简称BMI），是用体重公斤数除以身高米数平方得出的数字

#BMI < 18.5 体重偏轻
#18.5 <= BMI < 24 体重正常
#BMI >= 24 体重偏重
#设计一个BMI计算器吧，看看自己体重是否正常。

#输入：身高、体重值
#输出：BMI 指数、是否正常

height=eval(input('请输入身高(m):'))
weight=eval(input('请输入体重(kg):'))
BMI=weight/height**2
if BMI<18.5:
	print('BMI=',BMI,'体重偏轻')
elif BMI>=24.5:
	print('BMI=',BMI,'体重偏重')
else:
	print('BMI=',BMI,'体重正常')
