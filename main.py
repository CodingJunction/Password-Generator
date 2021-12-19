import random

special = ['!','#','$','%','&','(',')','*','+']
print('''Welcome to Password Generator
Enter the details to generate password \n''')
a=int(input('Enter number of capital letter :\n'))
b=int(input('Enter number of small letter :\n'))
c=int(input('Enter number of digits :\n'))
d=int(input('Enter number of special characters :\n'))

password=[]
for i in range(a):
    password.append(chr(random.randint(65,90)))
for i in range(b):
    password.append(chr(random.randint(97,122)))
for i in range(c):
    password.append(str(random.randint(0,9)))
for i in range(d):
    password.append(random.choice(special))
random.shuffle(password)
s=""
for i in password:
    s+=i
print('The password is:',s)

