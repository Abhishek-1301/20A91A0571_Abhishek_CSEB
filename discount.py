n=int(input('Enter total amount:'))
print('Your total bill amount is:',n)
if 1000<=n<2000:
    d=0.1*n
    print('Your discount is ',d)
    print('Dear customer,your total bill payable is ',n-d)
elif 2000<=n<3000:
    d=0.2*n
    print('Your discount is ',d)
    print('Dear customer,your total bill payable is ',n-d)
elif 3000<=n<5000:
    d=0.3*n
    print('Your discount is ',d)
    print('Dear customer,your total bill payable is ',n-d)
elif n<=5000:
    d=0.4*n
    print('Your discount is ',d)
    print('Dear customer,your total bill payable is ',n-d)
else n<1000:
    print('Sorry!your total bill payable is ',n)
'''
Output:
Enter total amount:1500
Your total bill amount is: 1500
Your discount is  150.0
Dear customer,your total bill payable is  1350.0
