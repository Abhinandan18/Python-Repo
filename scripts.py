import sys
import requests

print (sys.version)
print(sys.executable)

def Greet(whom_to_greet):
    greeting='Hello,{}'.format(whom_to_greet)
    print(greeting)
    return greeting

print (Greet('abhinandan'),end=" ") 
print('Patil')
print("Welcome to Python programming")
print("Push to local branch")
print("Push to local branch2")

 
a:int
a='1'
if a=='1':
    print ('a is 1')
elif a==3:
    print('a is 3')
else:
    print('not match')