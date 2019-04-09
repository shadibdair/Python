
"""
def rev(self):
    b=""
    for i in self:
        b=i+b
    self=b
    return self


func=rev("shadi")
print(func)

```
```
a, b = 0,1
for i in range(0,10):
    print(a)
    a, b = b, a + b
```
```
aa={10,20,30,40,50,10,20,30,40,50}
for i in aa:
    print(i)
```
```
# give me each number in a list square.
listt=[1,2,3,4,5,6,7,8,9,10]
square=[num*num for num in listt]
print(square)

```
```
# fibonacci Generator
def fib(num):
    a,b=0,1
    for i in range(0,num):
        yield "{}: {}".format(i+1,a)
        a,b = b,a+b
for item in fib(10):
    print(item)
"""