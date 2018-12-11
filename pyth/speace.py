# encoding: utf-8

# 参数平方相加
def calc(numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum

print(calc([5,2]))


# 可变参数平方相加
def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum
print(calc(1,2,3,4,5,6,6,9,10,11,12))		

# 前面加一个*号，把list或tuple的元素变成可变参数传进去
nums = [1,2,3,4,5,6,7]
print(calc(*nums))

# *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见
	


# 关键字参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
def person(name,age,**kw):
	# if kw.get('job'):
	# 	kw.pop('job')
	if 'job' in kw:
		kw.pop('job')
		
	print('name',name,'age',age,'other',kw)

person('wang','28')
person('wang','28',city='beijing')
person('wang','28',sg='180')
person('wang','28',sg='180',city='beijing')
extra = {'names':'wanghuizhou','job':'sf'}
           
person('wang','28',**extra)

print(extra)
	
# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，
# kw将获得一个dict，
# 注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。

# 调用者仍可以传入不受限制的关键字参数
person('jack',24,city='beijinbg',addr='bveiujikng',zipos= 123456)

# ************************
#  命名关键字参数
# ************************

# 限制关键字参数的名字，可以用命名关键字参数，


def f2(names,city='beijing',*jobs):
	print('names',names,'jobs',jobs,'city:',city)

f2('ssss',(1,2,3),{'city':'beijing'},(3,4,5,88),'adsfsadfsadfsd',[10,209,300],6)

# def f3(name,age,*city,job):
# 	print('name:',name,'ages:',age,'city:',city,'job:'job)
# f3('ddd','23',city='beijing','ddd')

# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊的分隔符“*”了


# ************************
#  命名关键字参数
# ************************
# def f1(a,b,c=0,*args,**kw):
# 	print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

# f1(1,2,3,(12,34,56),{'city':'beijing'},tity='beijing',jos='ss',adds='dddd')

# ************************
# PS:

# 1：*args 是可变参数，可接受字符串，数组,int，(1,2,3),[数组],{字典}
# 2：**kw 关键字参数，接受的是一个字典

#  调用函数时，如何传入可变参数和关键字参数的语法
# 1:通过可变参数传值是fun(1,2,3),也可以先组装list货trple，在通过*args 传入fun(*(1,2,3))
# 2:关键字参数可以直接传入fun(a=1,b=2),也可以先组装dict，在通过**kw传入fun(**{'a'=1,'b'=2})
# ************************

def f4(name,*oper):
	print('name:',name,'oper:',oper)

f4('wanghiuzhou',*(1,2,3,4,4))