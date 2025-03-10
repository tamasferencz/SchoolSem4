### Task 0
"""
x = int(input("Give me a number: "))
print(x)
"""

### Task 1
"""
x = int(input("Give me a number: "))
print(x >= 100)
"""

### Task 2
"""
user_input = input("Give me a number:")
if user_input.isdigit():
    print("It's a number")
else:
    print("It's not a number!")
"""

### Task 3
"""
year = int(input("Give me a year: "))
if(year % 4 != 0):
    print("Common year!")
elif(year % 100 != 0):
    print("Leap year!")
elif(year % 400 != 0):
    print("Common year!")
else:
    print("Leap year!")
"""

### Task 4
secret_number = 777
print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
""""
while True:
    guessed_number = int(input("Guess the number: "))
    
    if guessed_number == 777 :
        break
    
print("You're correct :)")
"""

### Task 5
"""
while True:
    input_word = input("Give me the exit word: ")
    
    if input_word == "chupacabra" :
        break
    
print("You've successfully left the loop.")
"""

### Task 6
"""
word_without_vowels = ""
user_word = input("Give me a word: ")
user_word = user_word.upper()

for letter in user_word:
    if letter not in ['A', 'E', 'I', 'O', 'U'] :
        word_without_vowels += letter


print(word_without_vowels)
"""

### Task 7
"""
c0 = int(input("Give me a number: "))
step = 0

while c0 > 1 :
    if c0 % 2 == 0 :
        c0 = c0 // 2
    else :
        c0 = 3 * c0 + 1
    step+=1
    print(c0)
    
print("Steps: ", step)
"""
### Task 7
"""
hat_list = [1, 2, 3, 4, 5]
replace = int(input("Give me the number that you want to replace with the middle number: "))
middle_index = len(hat_list) // 2
hat_list[middle_index] = replace
print(hat_list)

hat_list.pop()

print("The length of the list is", len(hat_list))

print(hat_list)
"""

### Task 8
"""
beatles = []

beatles.append("John")
beatles.extend(["Lennon", "Paul McCartney", "George Harrison"])
print(beatles)

new_members = ["Stu Sutcliffe", "Pete Best"]

for member in new_members:
    beatles.append(member)
print(beatles)

del beatles[beatles.index("Stu Sutcliffe")]
del beatles[beatles.index("Pete Best")]
print(beatles)

beatles.insert(0, "Ringo Starr")
print(beatles)
"""

### Task 9
"""
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

seen = set()

for element in my_list[:]:
    if element in seen:
        my_list.remove(element)
    else:
        seen.add(element)

print(my_list)
"""

## Task 3.9
"""
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

unique_list = []

for num in my_list:
    if num not in unique_list:
        unique_list.append(num)

print("The list with unique elements only:")
print(unique_list)
"""

## Task 3.10

import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")

print()
