from time import time 
import io;
def logger(fn, ):
    print('decorator')
    def log(k):
        start = time();
        
        print('run');
        fn('a');
        print(f'ending with time: {time() - start}');
    return log;

def a (b):
    print('is a')
@logger(a)
def main(param):
    for x in range(10000000):
        print(x, param);

main()