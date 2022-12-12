import Calculator as cc
picture1=input('Please enter first picture like picture1.jpg: ')
picture2=input('Please enter second picture like picture1.jpg: ')
operator=input('Please add the math operator(+, -, *, /, ^): ')

import img2int as i2
first_number=i2.img2int(picture1)
second_number=i2.img2int(picture2)
result=cc.calculate(first_number,second_number,operator)
print(first_number,operator,second_number,'=',result)
f=[]
for i in str(first_number):
    f.append(i)
s=[]
for i in str(second_number):
    s.append(i)
r=[]
for i in str(result):
    r.append(i)
from number import *
for i in range(len(f)):
    if(f[i]=='0'):
        rectangle(i)
        zero(i)
        time.sleep(1)
    elif(f[i]=='1'):
        rectangle(i)
        one(i)
        time.sleep(1)
    elif(f[i]=='2'):
        rectangle(i)
        two(i)
        time.sleep(1)
    elif(f[i]=='3'):
        rectangle(i)
        three(i)
    elif(f[i]=='4'):
        rectangle(i)
        four(i)
    elif(f[i]=='5'):
        rectangle(i)
        five(i)
    elif(f[i]=='6'):
        rectangle(i)
        six(i)
    elif(f[i]=='7'):
        rectangle(i)
        seven(i)
    elif(f[i]=='8'):
        rectangle(i)
        eight(i)
    elif(f[i]=='9'):
        rectangle(i)
        nine(i)

# Additiion (+)
if(operator=='+'):
    plus(len(f))
# Substraction (-)
elif(operator=='-'):
    minus(len(f))
# Multiplication (*)
elif(operator=='*'):
    multiplication(len(f))
# Division(/)
elif(operator=='/'):
    division(len(f))
# Power 2 (**)
elif(operator=='^'):
    square(len(f))

for i in range(len(s)):
    if(s[i]=='0'):
        rectangle(i+len(f)+1)
        zero(i+len(f)+1)
    elif(s[i]=='1'):
        rectangle(i+len(f)+1)
        one(i+len(f)+1)
    elif(s[i]=='2'):
        rectangle(i+len(f)+1)
        two(i+len(f)+1)
    elif(s[i]=='3'):
        rectangle(i+len(f)+1)
        three(i+len(f)+1)
    elif(s[i]=='4'):
        rectangle(i+len(f)+1)
        four(i+len(f)+1)
    elif(s[i]=='5'):
        rectangle(i+len(f)+1)
        five(i+len(f)+1)
    elif(s[i]=='6'):
        rectangle(i+len(f)+1)
        six(i+len(f)+1)
    elif(s[i]=='7'):
        rectangle(i+len(f)+1)
        seven(i+len(f)+1)
    elif(s[i]=='8'):
        rectangle(i+len(f)+1)
        eight(i+len(f)+1)
    elif(s[i]=='9'):
        rectangle(i+len(f)+1)
        nine(i+len(f)+1)

equal(len(f)+len(s)+1)

for i in range(len(r)):
    if(r[i]=='0'):
        rectangle(i+len(f)+len(s)+2)
        zero(i+len(f)+len(s)+2)
    elif(r[i]=='1'):
        rectangle(i+len(f)+len(s)+2)
        one(i+len(f)+len(s)+2)
    elif(r[i]=='2'):
        rectangle(i+len(f)+len(s)+2)
        two(i+len(f)+len(s)+2)
    elif(r[i]=='3'):
        rectangle(i+len(f)+len(s)+2)
        three(i+len(f)+len(s)+2)
    elif(r[i]=='4'):
        rectangle(i+len(f)+len(s)+2)
        four(i+len(f)+len(s)+2)
    elif(r[i]=='5'):
        rectangle(i+len(f)+len(s)+2)
        five(i+len(f)+len(s)+2)
    elif(r[i]=='6'):
        rectangle(i+len(f)+len(s)+2)
        six(i+len(f)+len(s)+2)
    elif(r[i]=='7'):
        rectangle(i+len(f)+len(s)+2)
        seven(i+len(f)+len(s)+2)
    elif(r[i]=='8'):
        rectangle(i+len(f)+len(s)+2)
        eight(i+len(f)+len(s)+2)
    elif(r[i]=='9'):
        rectangle(i+len(f)+len(s)+2)
        nine(i+len(f)+len(s)+2)
    
