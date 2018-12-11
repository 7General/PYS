# encoding: utf-8
def funname(parameter_list):
    print(parameter_list)


funname("dddddd")
   
def person(name,age,**kw):
    print('name',name,'age',age,'other',kw)    

person('M','D',city='bj')

def calc(*numbers):
    sum = 0         
    for n in numbers:
        sum = sum + n * n          
    print('sum',sum)
    return sum
    
bs=calc

def dddd(dd):
    print(dd)

bs(1,2,3,4,5,6)


dddd('ddddddssssssssss')

def power(x,n = 2):
    s = 1
    while n > 0:
        n = n - 1;
        s = s * x
    return s

print(power(10,3))
    
def enroll(name,gender,age = 6,city = 'beijing'):
    print('name',name)
    print('gender',gender)
    print('age:',age)
    print('city:',city)
enroll('wwww','F',14)
enroll('wwww','F',city='henan')
   

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
print('L:',add_end())
print('L:',add_end())
print('L:',add_end())

  
    
