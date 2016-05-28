import mincemeat
import math
import time

start = time.time()

number = dict()
##for i in range(2,2000):
##    number [i] = i

i =0


for k in range(1,10+1):
    batch = []
    for j in range(1,(10000000/10)+1):
        i = i+1
        batch.append(i)
        number [k] = batch

datasource = number

def mapfn(k,v):
    import math
    for i in range(0,(10000000/10),2):
        x = int(v[i])
        def is_prime(n):
##            if x % 2 == 0 and x > 2: 
##                return False
            for i in range(3, int(math.sqrt(x)) + 1, 2):
                if x % i == 0:
                    return False
            return True
        if(str(x) == str(x)[::-1]):           
            status = is_prime(x)
            if status:
                yield x,x


def reducefn(k, vs):
    result = vs
    return result

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")

end = time.time()

timetaken = end-start
results = sorted(results)
del results[0]
print 'Numbers' , results
print 'Length', len(results)
print 'Sum', sum(results)
print 'timetaken', timetaken

    
