
num = int(input('please enter full number with 4 digit\n'))
while num > 9999 or num < 1000:
    num = int(input('wrong!please enter full number with 4 digit\n'))

print('the sum of the digits in the number is 4')

x=num%10
y=(num//10)%10
z=(num//100)%10
t=(num//1000)
reversNum=x*1000+y*100+z*10+t
print('the revers number is:' , reversNum)
if int(x) == int(t) and int(y) == int(z):
    print('the number is palindrom\n')
else:
    print('the number is not a palindrom\n')




