# 一定要学会编程
# 一定要坚持下去
# 编写时间：2024/8/23 00234:20
#数据类型转换函数
#str（）将其他数据类型转成字符串  注意事项 也可以用引号转换'123'                                         str是字符串
#int（）将其他数据类型转成整数    注意事项 文字类型和小数类字符串，无法转化成整数  2.浮点数转化成整数；抹零取整   int是数字串
#float()将其他数据类型转成浮点数  注意事项 文字类无法转换成整数 ，2.整数转成浮点数，末尾为0                 Float为浮点数
name='张三'
age=20
print(type(name),type(age))#说明name与age的数据类型不同
#print('我叫'+name+'今年，'+str(age)+'岁')#当将str类型与int类型进行连接时，报错，解决方案，类型转换

#将其他类型转成---str（）---转成str类型
a=10
b=198.8
c=False
print(type(a),type(b),type(c))
print(str(a),str(b),str(c),type(str(a)),type(str(b)),type(str(c)))

s1='128'
f1=98.7
s2='76.77'  #为浮点多数位，所以转换不了为int数据类型
ff=True
s3='hello'

print(type(s1),type(f1),type(s2),type(ff),type(s3))
print(int(s1),type(int(s1)))                        #将str转成int类型，字符串为 数字串
print(int(f1),type(int(f1)))                        #Float转成int类型，截取整数部分，舍掉小数部分
#print(int(s2),type(int(s2)))                       #将str转成int类型，报错，因为字符串为小数串
print(int(ff),type(int(ff)))                        #True本身可作为基础数值1使用  False为基础0
#print(int(s3,type(int(s3))))                       #将str转成int类型时，字符串必须为数字串(整数）非数字串是不允许转换的 否则会报错

s1='128.98'
s2='76'
ff=True
#s3='hello'
i=98
print(type(s1),type(s2),type(ff),type(s3),type(i))
print(float(s1),type(float(s1)))
print(float(s2),type(float(s2)))
#print(float(ff),type(float(ff)))#字符串不能转成str和float  #字符串中的数字如果是非数字串，则不允许转换
print(float(s3),type(float(s3)))
print(float(i),type(float(i)))


#下一章节pychrm的注释指定格式     coding：gbk或者coding：utf-8