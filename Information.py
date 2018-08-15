#Simple Password Code

passwordFile = open('SecretPasswordFile.txt')
secretPassword = passwordFile.read()
print('Enter your password.')
typedPassword = input()
if typedPassword == secretPassword:
	print('Access granted')
	if typedPassword == '12345':
		print('That password is one that an idiot puts on their luggage.')
else:
	print('Access denied')

-----------------------------------------------------------------------------------

Functions:
print() displays the value passed to
input() lets user type in a value
len() takes the string value and returns an integer value of the strings length
int(), str(), and float() convert values data type 

# How str(), int(), and float() Functions work 
myAge=input() #in this case 26
print('You will be ' + str(int(myAge) +1) + ' in a year.')
print('You will be ' + str(int('26') +1) + ' in a year.')
print('You will be ' + str(26 +1) + ' in a year.')
print('You will be ' + str(27) + ' in a year.')
print('You will be ' + '27' + ' in a year.')
print('You will be 27' + ' in a year.')
print('You will be 27 in a year.')


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-- Boolean value = True / False -- 

Comparison (These evaluate down to the Boolean value)
== Equal to
!= Not equal to 
<  Less than
>  Greater than
<= Less than or equal to 
=> Greater than or equal to 

42 == 42
True

42 != 41
True

42 <= 50 
True

myAge = 26 
myAge < 30
True 

Intergers and strings are not equal 
42 == '42'
False 

Float values and integers can be equal 
42.0 == 42 
True 

Boolean Operators:
and, or, not 

Operators Truth/Or/Not Tables:
True and True = True 
True and False = False
False and True = False
False and False = False 

True or True = True 
True or False = True 
False or True = True 
False or False = False 

not True = False
not False = True 

#example
myAge = 26 
myPet = 'Cat'
myAge > 20 and mypet == 'Cat'
True 

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-- Flow control statements -- 

if and else and elif 
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
if statement example: 
name = 'Alice'
if name == 'Alice':     <---- This is a condition, if this condition is true it reads the indented code, if this is false it skips the indented code 
	print('Hi Alice')
print('Done')
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
if + else statement exaple:
password = 'swordfish'
if password == 'swordfish'
	print ('Access Granted')
else:
	print ('Wrong password')
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
elif example
name = 'Bob'
age = 3000
if name == 'Alice':
	print ('Hi Alice')
elif age < 12:
	print ('You are not Alice.') 
elif age > 2000:
	print ('Unlike you, Alice is not an Immortal')
elif age > 100:
	print ('You are not Alice, oldie')

This example, the first True sttement is elif age > 2000 so this elif statement is used. Order for statements matters, Python stops at the FIRST True statement 
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-- Truthy and Falsy for string & integer values --
print('Enter a name.')
name = input()
if name:
	print('Thank you for entering a name.')
else:
	print('You did not enter a name.')

Blank string is falsey, all others are truthy - In this example anything other than blank will use the IF statement. This can also be achieved with this line 
if name != '': 

Integer values
0 is falsey - 0.0 is falsey - everything else is truthy 
This can be checked by passing them to the bool() Functions 
i.e
bool(0)
False
bool(1)
True 
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-- while loop --

spam = 0 
while spam < 5:
	print('Hello world!')
	spam = spam + 1 

This prints Hello world 5 times, after the 5th time 'spam = 5' and the while statement is now false 

name = ''
while name != 'Bossdawg':
	print ('Please type your name')
	name = input()
print ('Thank you')

This will keep looping until 'Bossdawg' is entered. If you enter anything but 'Bossdawg' it will keep looping to the while statement

-- Infinite Loops-- 
Infinite loop example - This will print Hello infinitely because True is always True 
While True:
	print ('Hello')

-- Break Statements --

name = ''
while True:
	print ('Please type your name')
	name = input()
	if name = 'Bossdawg'
		break
print ('Thank you')

This program loops until Bossdawg is entered, the break statement breaks out of the while True loop 

-- Continue Statement -- 

spam = 0
while spam < 5:
	spam = spam + 1
	if spam == 3
		Continue
	print('spam is ' + str(spam))

This will print
spam is 1
spam is 2
spam is 4
spam is 5 

spam is 3 is skipped because when spam equals 3 we use the continue statement.
A continue statement causes the execution to immediately jump back to the start of the loop and re-check the condition, thus skipping the print function  
 

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-- for loop -- 

print ('My name is')
for i in range(5):
	print ('Jimmy Five Times ' + str(i))

This prints: 
My name is 
Jimmy Five times 0
Jimmy Five times 1
Jimmy Five times 2
Jimmy Five times 3
Jimmy Five times 4

1st time i = 0
2nd time i = 1 etc etc  
Once it hits 5 it stops, the range function dictates the end of the for loop 

-- New script --
total = 0
for num in range (101) 
	total = total + num
print (total)

At the start total = 0
It then starts the for loop, runs total = total + num - forevery integer up to 101 (the range)

-- while Loop equivalent of a for Loop -- 

print ('My name is')
for i in range(12, 16):
	print ('Jimmy Five Times ' + str(i))

for Loops will loop a specific number of times.
The range() function called one function range(5) This shows numbers 0 through 5 
The range() function called two functions range(0, 10) This shows numbers 0 through 10 whilst skipping 10
The range() function called two functions range(0, 10, 2) This shows numbers 0 through 10 whilst skipping 10 but increasing by 2 each time 
break and continue can be used in for loops 


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-- built in functions -- 

Modules called The Standard Library

import statements to pull the function from a module 

import sys 
sys.exit() 

Third-Party Modules 
such as Praw or pyperclip

pyperclip.copy('Hello World!')
pyperclip.paste

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def hello():
	print('Howdy')
	print('Howdy!!')
	print('Howdy!!!!')

hello()
hello()
hello() 



def plusOne(number):
	return numer + 1

numberNumber = plusOne(5)
print(newNumber)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-- global and local scopes -- 

spam = 42 # global variable

def eggs():
	spam = 42 #local variable 

print('Some code here')
print('Some more coder here') 