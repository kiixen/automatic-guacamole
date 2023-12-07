x=lambda a,b: a/b;
print(x(30,2))

def myfunc(n):
    return lambda a: int (a/n);
double=myfunc(2)
print(double(20))
    