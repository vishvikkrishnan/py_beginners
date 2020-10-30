def compute_distance(x1, y1, x2, y2):
    distance = 0
    x=(x2-x1)
    y=(y2-y1)
    d=float((x*x)+(y*y))
    distance=float(pow(d,0.5))
    return distance+1

print("enter test case")
T = int(input())
if T<=25 and 1<=T:
    for i in range(0,T):
        print("enter values for case",i+1)
        x1=int(input())
        y1=int(input())
        x2=int(input())
        y2=int(input())
        if ((int(x1)<=20) and (-20<=int(x1))) and  ((int(y1)<=20) and (-20<=int(y1))) and  ((int(x2)<=20) and (-20<=int(x2))) and  ((int(y2)<=20) and (-20<=int(y2))):
            z=compute_distance(x1, y1, x2, y2)
            print('distance is ', "{0:.2f}".format(z))
        else:
            print("values out of range")
else:
    print("test case out of range")





        

