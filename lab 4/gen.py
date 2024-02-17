#1
n = int(input())
a = (k**2 for k in range(n))

print(list(a))
#2
n = int(input())
c = (i for i in range (n))
even = (i for i in c if i%2==0)
print(*even, sep = ",")
#3
def delim(n):
    for i in range(n):
        if i % 3 == 0 and i % 4 == 0:
            yield i
n = int(input())
for num in delim(n):
    print(num)

#4
    


