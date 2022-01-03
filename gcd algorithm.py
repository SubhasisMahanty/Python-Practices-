#Using recursion
''' G C D 
a=input('number1:')
b = input('number2:')
def gcd(a,b):
    if(a==b):
        return a
    elif(b==0):
        return a
    else:
        return gcd(b,a%b)
print('The Gcd of a and b is:)
print(gcd(a,b))
    '''

#Without Recursion
def gcd(a,b):
    if (a == b):
        gcd = a
    if(a>b):
        small = b
    else:
        small = a
    for i in range(1,small+1):
        if((a%i==0) and (b%i==0)):
            gcd = i
    return gcd
print('gcd of a and b: ')
print(gcd(a,b))
