#Generate all rotations of a given string
def cyclicshift(s,n):
    for i in range(n):
        print(s[-i:]+s[:-i])
s=input("Enter string")
n=len(s)
cyclicshift(s,n)
