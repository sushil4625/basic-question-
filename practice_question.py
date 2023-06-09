# -*- coding: utf-8 -*-
"""practice_question.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QZY891ZbzONo-NFPXGfe8jEYvFkJTgtc
"""

#1 Write a program to reverse an integer in Python.
def rev(n):
  new,b=0,0
  while n!=0:
    b=n%10
    n=n//10
    new=new*10+b
  print(new)

rev(123456789)

#2 Write a program in Python to check whether an integer is Armstrong number or not.
def arm(n):
  pow=len(str(n))
  sum,b=0,0
  m=n
  while n!=0:
    b=n%10
    n=n//10
    sum=sum+b**pow
  if sum==m:
    print(m,"is armstrong number")
  else:
    print(m,"is not armstrong number")

arm(371)

#3 Write a program in Python to check given number is prime or not.
def prime_check(n):
  for i in range(2,n):
    if n%10==0:
      print(n,"is not prime")
      break
    else:
      print(n,"is prime number") 
      break

prime_check(23)

#4 Write a program in Python to range of prime number.
def pr(m,n):
  l=[]
  for i in range(m,n+1):
    flag=0
    for j in range(2,i):
      if i%j==0:
        flag=1
        break
    if flag==0:
      if i!=0 and i!=1:
        l.append(i)
  print(l)

pr(0,200)

#5 Write a program in Python to print the Fibonacci series using iterative method.
def fib(n):
  a,b=0,1
  sum=0
  for i in range(n):
    if i<=1:
      print(i)
    else:
      sum=a+b
      a=b
      b=sum
      print(sum)

fib(10)

#6 Write a program in Python to print the Fibonacci series using recursive method.
def fibo(n):
  if n<=1:
    return n
  else:
    return fibo(n-1) + fibo(n-2)

for i in range(10):
  print(fibo(i))

#7 Write a program in Python to check whether a number is palindrome 
def pal(n):
  m=str(n)[::-1]
  if int(m)==n:
    print("pallindrome")
  else:
    print(" not pallindrome")

pal(121)

#8 Write a program in Python to check whether a number is palindrome
def pall(n):
  b,rev,m=0,0,n
  while n!=0:
    b=n%10
    n=n//10
    rev=rev*10+b
  if m==rev:
    print(m,"pallindrome")
  else:
    print(m,"not pallindrome")

pall(121)

#9 Write a program in Python to find greatest among three integers.
def gr(p,q,r):
  if p>q and p>r:
    print(p,"is greatest")
  elif q>p and q>r:
    print(q,"is greatest")
  else:
    print(r,"is greatest")

gr(20678,54,589)

#10 Write a program in Python to check if a number is binary?
def bi(n):
  b=0
  while n!=0:
    b=n%10 
    n=n//10
    if b!=0 and b!=1:
      print("not binary")
      break
    if n==0:
      print("binary")

bi(1101111000)

#11.Write a program in Python to swap two numbers ?
def swap(a,b):
  a,b=b,a
  print("a is",a)
  print("b is ",b)

swap(b=10,a=20)

# 12 Write a program in Python to swap two numbers without using third variable?
def sw(a,b):
  a=a+b
  b=a-b
  a=a-b
  print("a is",a)
  print("b is",b)

sw(b=10,a=20)

# 13 Write a program in Python to find prime factors of a given integer.
def prime_num(n):
  c=2
  while (n>1):
    if n%c==0:
      n=n//c
      print(c)
    else:
      c=c+1

prime_num(300)

#14 Write a program in Python to add two integer without using arithmetic operator?
def add(a,b):
  for i in range (1,b+1):
    a=a+1
  print (a)

add(39,8)

#15 Write a program in Python to find given number is perfect or not?
def per(n):
  a,m=0,n
  for i in range(1,n):
    if n%i==0:
      a=a+i
  if a==m:
    print("perfect number is",m)
  else:
    print("not perfect number is",m)

per(28)

#16 Python Program to find the Average of numbers 
l=[37,26,5,3,17,7,2]
print("average =",sum(l)/len(l))

#17 Python Program to calculate factorial using iterative method.
def fac(n):
  f=1
  for i in range(1,n+1):
    f=f*i
  print(f)

fac(5)

#18  Python Program to calculate factorial using recursion.
def fact(n):
  if n<=1:
    return 1
  else:
    return fact(n-1) * n

fact(5)

#19 Python Program to check a given number is even or odd.
def evod(n):
  if n%2==0:
    print("even is",n)
  else:
    print("odd is",n)

evod(8)

#20 Python program to print first n Prime Number with explanation.
def prim(n,m):
  l=[]
  for i in range (n,m+1):
    flag=0
    for j in range(2,i):
      if i%j==0:
        flag=1
    if flag==0 and i>1:
      l.append(i)
  print(l)

prim(0,20)

#21 Python Program to find Smallest number among three.
def sm(a,b,c):
  if a<b and a<c:
    print("smallest number is ",a)
  elif b<a and b<c:
    print("smallest number is ",b)
  else:
    print("smallest number is",c)

sm(28,3,7)

#22 smallest among three
l=[37,77,828]
print("minimum is",min(l))
print("maximum is",max(l))

#23 Python program to calculate the power using the POW method.
n=int(input("enter number"))
m=int(input("enter power"))
pow(n,m)

#24 Python Program to calculate the power without using POW function.(using for loop).
def power(n,m):
  p=1
  for i in range(m):
    p=p*n
  print(p)

power(20,10)

#25 Python Program to calculate the square root of a given number.
def sqroot(n):
  print(n**.5)

sqroot(9)

#26 Python Program to find LCM of two numbers.
def lm(a,b):
  ma=max(a,b)
  mi=min(a,b)
  l=1
  for i in range(ma,mi*ma+1,ma):
    if i%mi==0:
      print(i)
      break

#27 Python Program to find GCD or HCF of two numbers.
def hc(a,b):
  mi=min(a,b)
  ma=max(a,b)
  for i in range(mi,1,-1):
    if a%i==0 and b%i==0:
      print(i)
      break
    else:
      print(1)
      break

#28 Python Program to Convert Decimal Number into Binary.
def bi(n):
  l=[]
  while n!=0:
    b=n%2
    n=n//2
    l.append(b)
  print(l[::-1])

bi(18)

#29 Python Program to convert Decimal number to Octal number.
def oct(n):
  l=[]
  while n!=0:
    b=n%8
    n=n//8
    l.append(b)
  print(l[::-1])

oct(784)

#30 Python Program to check the given year is a leap year or not.
def leap(n):
  if (n%4==0 and n%100!=0) or n%400==0:
    print("leap year is",n)
  else:
    print("not leap year is",n)

leap(2024)

#31 Python Program to convert Celsius to Fahrenheit.
def deg(n):
  return (n*9/5)+32

deg(10)