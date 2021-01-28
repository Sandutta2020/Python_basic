def generator(num):
    while num > 0:
        yield num-1
        num =num -1

for value in generator(10):  
    print(value) 

x =generator(10)
print(x.__next__()) 
print(x.__next__()) 

def generator_batch(num):
    lst =[]
    while num > 0:
        lst.append(num)
        if len(lst)==20:
            yield lst
            lst =[]
        num -=1   
for value in generator_batch(100):  
    print(value) 

lst =['a','b','c','d']

def getting_list(lst):
    for item in lst:
        yield item

X =getting_list(lst)
print(X.__next__()) 
print(X.__next__()) 