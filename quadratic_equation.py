#Solving a quadratic equation

a = int(input("Enter A: "))
b = int(input("Enter B: "))
c = int(input("Enter C: "))

if(a == 0):
    print("Sorry dude, but this ain't a quadratic equation then.")
    

elif(b != 0 and c != 0):
    xi = ((-1*b)+(((b*b)-(4*a*c))**(1/2)))/(2*a)
    xii = ((-1*b)-(((b*b)-(4*a*c))**(1/2)))/(2*a)

    print("x1",xi,"\nxii",xii)

elif(b == 0 and c == 0):
    xi = 0
    xii = 0

    print("x1",xi,"\nxii",xii)

elif(b == 0):

    xi = ((-1*c)/a)**(1/2)
    xii = -1*((-1*c)/a)**(1/2)

    print("x1",xi,"\nxii",xii)

elif(c == 0):
    xi = 0
    xii = (-1*b)/a

    print("x1",xi,"\nxii",xii)


