# encoding: utf-8

#  函数的递归
def fact(n):
	if n==1:
		return 1
	return n * fact(n - 1)

print(fact(4))



def f1(n):
	return f2(n, 1)

def f2(num,product):
	if num == 1:
		return product
	return f2(num - 1,num * product)

print('fact_iter',f2(4,1))
print('fact_iter',f1(4))







# def fact(n):
#     return fact_iter(n, 1)

# def fact_iter(num, product):
#     if num == 1:
#         return product
#     return fact_iter(num - 1, num * product)

# print('fact_iter',fact_iter(4,1))


# 使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出。