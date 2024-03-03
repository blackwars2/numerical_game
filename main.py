import random
n = random.randint(1, 100)
print("Добро пожаловать в угадайку")
count = 0
a = n
while n>=1:
    count +=1
    n = n//2
if a == 2**(count - 1):
    print(count - 1)
else:
    print(count)
