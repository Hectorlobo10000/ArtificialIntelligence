from __future__ import print_function
import random
#Python
a = 5
print(a, "is of type", type(a))

a = 2.05
print(a, "is of type", type(a))

a = 1 + 2j
print(a, "is a complex number?", isinstance(a,complex))

x = y = z = 5
print("z has value", z)

print(1, 2, 3, 4, sep = '*',  end = '\n')

print("x has value {} and y has value {}".format(x,y))

print("I love {0} and {1}".format('bread', 'butter'))

print(5-7)

print(10 - 4 * 2)

print((10 -4 ) * 2)

print(5 * 2 // 3)

print (5 * (2 // 3))

print(2 ** 3 ** 2)

print ((2 ** 3) ** 2)

number = 3
if number > 0:
    print(number, "is a number positive")
print ("This is always printed")

number = -1
if number > 3:
    print(number, "is a number positive")
print("This is also always printed")

number = 3
if number >= 0:
    print("Positive or zero")
else:
    print("Negative number")

number = 3.4
if number > 0:
    print("Positive number")
elif number == 0:
    print("Zero")
else:
    print("Negative number")

number = float(raw_input("Enter a number: "))
if number >= 0:
    if number == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")

numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
sum = 0
for val in numbers:
    sum = sum + val
print("The sum is", sum)

print(range(10))

print(list(range(10)))

print(list(range(2, 8)))

print(list(range(2, 20, 3)))

genre = ['pop', 'rock', 'jazz']
for val in range(len(genre)):
    print("I like", genre[val])

digits = [0, 1, 5]
for val in digits:
    print(val)
else:
    print("No items left.")

for val in genre:
    print("I like", val)

n = 10
sum = 0
i = 1
while i <=n:
    sum = sum + i
    i = i + 1

print("The sum is", sum)

counter = 0
while counter < 3:
    print("Inside loop")
    counter = counter + 1
else:
    print("Inside else")

for val in "string":
    if val == "i":
        break
    print(val)
print("The end")

for val in "string":
    if val == "i":
        continue
    print(val)
print("The end")

sequence = {'p', 'a', 's', 's'}
for val in sequence:
    pass

'''while True:
    num = int(raw_input("Enter an integer: "))
    print("The double  of", num, "is", 2 * num)'''

vowels = "aeiouAEIOU"
while True:
    val = raw_input("Enter a vowel: ")
    if val in vowels:
        break
    print("That is not a vowel. Try again!")

print("Thank you!")

while True:
    raw_input("Press enter to roll the dice")
    num = random.randint(1,6)
    print("You got",  num)
    option = raw_input("Roll again?(y/n)")
    if option == 'n':
        break
