a = 3
b = 3
c = 3
#a= float(input('5: '))
#b= float(input('6: '))
#c= float(input('7: '))
s = (a + b + c) / 2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)
