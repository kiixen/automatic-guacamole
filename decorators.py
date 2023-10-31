import time;

def timer(fn):
    print('timer performed');
    def t(*arg, **kwargs):
        startTime = time.time();
        fn(*arg, *kwargs);
        endTime = time.time();
        print(endTime - startTime);
    return t;

def love(fn):
    print('я люблю Мохинур');
    def l(*arg, **kwargs):
        return fn(*arg, **kwargs);
    return l;

@love
@timer
def main(a) :
    for x in range(1000000):
        print(x, a);


# timer(main)('a')

main;