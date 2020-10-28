# Eulers totient function is the count of numbers from 1-n that are its relative primes (hcf = 1)
def hcf(x,y):
    if (x==0):
      return y
    return hcf(x,y)

def eulers_function(n):
# since hcf with 1 is always 1 we set res=1
    res = 1
    for i in range (2,n):
      res+=1
    return res
n=5
#hcf(1, 5) is 1, hcf(2, 5) is 1, 
#hcf(3, 5) is 1 and hcf(4, 5) is 1
print (" Eulers totient function (" + str(n) + ") =" + str(eulers_function(n)))
