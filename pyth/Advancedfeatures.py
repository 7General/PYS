# encoding: utf-8
# 高级特性
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack','caiwu','function','resoult','jian','file','go','mongy']

print(L[0:3])
print(L[-2:-1])
#******************* 
#正数第一个元素的索引是0。
#倒数第一个元素的索引是-1。
#******************* 

# 取出一段数列 比如前5个
print(L[:5])            
# 取出一段数列 比如后4个    
print(L[:-4])  
#  取出前2-5的数据
print(L[2:5])

# 取出前10个数，每2个取一个
print(L[:10:2])
# 所有数每4个取一个
print(L[::4])

# 甚至什么都不写，只写[:]就可以原样复制一个list：
print(L[:])
 
#  对元组进行操作
M = (1,2,3,4,5,6,7,8,9,0,11)
# tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
print(M[:5])

# 对字符串进行操作
# 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：
STR = 'WANGHUIZHOU'
print(STR[:10:2])

# PS:
# 在很多编程语言中，针对字符串提供了很多各种截取函数（例如，substring），其实目的就是对字符串切片。
# Python没有针对字符串的截取函数，只需要切片一个操作就可以完成，非常简单。
# 




# 迭代
#  要有严格的缩进控制
d = {'a':1,'b':2,'c':3,'d':4,'e':5}

# 迭代key
for ite in d:
    print('key',ite)

# 迭代value
for values in d.values():
    print('value',values)
    
# 同时迭代key和value
for k,v in d.items():
    print('key',k,'value',v)
    
# 字符串也是可迭代对象
for ch in 'ABC':
    print(ch)

# PS:
# 当我们使用for循环时，只要作用于一个可迭代对象，
# for循环就可以正常运行，而我们不太关心该对象究竟是list还是其他数据类型
# 

#  *********
# 如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断
#  *********
from collections import Iterable
ab = isinstance('abs',Iterable)
print('char',ab)
ab = isinstance((1,2,3,4,5,6),Iterable)
print('T',ab)
ab = isinstance([1,2,3,4,5,6],Iterable)
print('list',ab)
ab = isinstance({'a':1},Iterable)
print('dict',ab)


list = [10,20,30,40,40,5,6]
for itesm in list:
    print(itesm)

# Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
for key,value in enumerate(list):
    print('key',key,'values',value)
    