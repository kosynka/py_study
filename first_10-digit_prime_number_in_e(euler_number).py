import operator
import decimal as dc

def edigits(p):
    dc.getcontext().prec = p
    factorial = 1
    euler = 2
    for x in range(2, 150):
        factorial *= x
        euler += dc.Decimal(str(1.0))/dc.Decimal(str(factorial))
    return euler

estring = edigits(150).to_eng_string()[2:]

for i in range(len(estring)-10):
    x = int(reduce(operator.add,estring[i:i+10]))
    if isprime(x):
        print x
        print i
        break
