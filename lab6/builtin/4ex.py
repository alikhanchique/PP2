from time import sleep
import math
squ = int(input())
mil = int(input())
def dela(fun, mil, *squ):
    sleep(mil / 1000)
    return fun(*squ)
print(dela(lambda x: math.sqrt(x), mil, squ))