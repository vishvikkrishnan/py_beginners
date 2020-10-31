#find the second lowest element.
def secondlowest(arr):
    c=0
    arr.sort()
    lowest=arr[0]
    for i in range(len(arr)):
        if arr[i]==lowest:
            c+=1
    return arr[c]
arr=list(map(float,input("Enter elements ").strip().split()))
print(secondlowest(arr))
