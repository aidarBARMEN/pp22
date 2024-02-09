#1
def shop(grams):
    ounces = 28.3495231 * grams
    print(ounces)
shop(2)
#2
def temp(F):
    C = (5 / 9) * (F - 32)
    print(C)
A = int(input())
temp(A)
#3
def legs(head = 35, legs = 94):
    for x in range(100):
        for y in range(100):
            if x + y == head and 4*x + 2*y == legs:
                return x,y
result = legs()
print(result)
#4
from math import sqrt

def ifprime(n):
    if n <= 1:
        return False
    for p in range(2, int(sqrt(n)) + 1):
        if n % p == 0:
            return False
    return True

def filter_prime(spisok):
    primes = []
    for i in spisok:
        if ifprime(i):
            primes.append(i)
    return primes

#Example
spisok = [2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = filter_prime(spisok)
print(prime_numbers)

#5
from itertools import permutations
st = input("input the string you want to permutate - ")
list1 = list(permutations(st))
for x in list1:
  print(x)


#6
def antiw(s = "we are ready"):
    words = s.split()
    antiWORDS = words[::-1]
    reversed_s = ' '.join(antiWORDS)
    print(reversed_s)

antiw()

#7
def has_33(nums):
  for i in range(len(nums) - 1):
    if nums[i] == 3 and nums[i+1] == 3:
       return True
  return False

has_33([1, 3, 3]) #→ True
has_33([1, 3, 1, 3]) #→ False
has_33([3, 1, 3]) #→ False
#8
def spy_game(nums):
  count = 0
  for i in range(len(nums)):
    if nums[i] == 0:
      count += 1
    if count == 2 and nums[i] == 7:
      return True
    elif count != 2 and nums[i] == 7:
      return False
  return False

print(spy_game([1,2,4,0,0,7,5])) #--> True
print(spy_game([1,0,2,4,0,5,7])) #--> True
print(spy_game([1,7,2,0,4,5,0])) #--> False
#9
def volume(r):
    import math
    V = 4/3*(math.pi * r**3)
    print(V)
volume(2)

#10
def unique(li):
    prom = []
    for i in li:
        if i not in prom:
            prom.append(i)
    return prom

li = [1, 1, 1, 1, 4, 4, 4, 5, 5, 5]
print(*unique(li))

#ex11
def ispalindrome(word):
  copy = word[::-1]
  if copy == word:
    return True
  return False
print(ispalindrome("abbad")) # false
print(ispalindrome("abba")) #true
#ex12
def histogram(arr):
  for i in arr:
    strin = '*'
    print(strin * i)
histogram([3, 4, 2])
#ex13
import random
def guess():
  number = random.randint(1, 21)
  name = input("Hello! What is your name?\n")
  print("Well, "+ name + ", I am thinking of a number between 1 and 20.\n")
  count = 0
  for i in range(20):
    count += 1
    x = int(input("Take a guess.\n"))
    if x < number:
      print("Your guess is too low.\n")
    elif x > number:
      print("Your guess is too high.")
    elif x == number:
      print("Good job, " + name +", You guessed my number in "+ str(count)+ " guesses!")
      break
guess()

