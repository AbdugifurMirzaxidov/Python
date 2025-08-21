
# Python Homeworks

## Lesson 2
1. Extract car names from the following text:
car = 'MsaatmiazD'
car[::2]
car[::-2]
2. Extract the residence area from the following text:
txt = "I'am John. I am from London"

yashash_joyi = txt[21:27]
print(yashash_joyi)
residence = txt.split("from")[1]
print(residence)
3. Write a Python program that takes a user input string and prints it in reverse order.
txt = "O'ktam dim O'ktamsan" 
txt[::-1]
4. Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).
word = input("Enter a word:")
word = word.lower()

if word == word[::-1]:
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")
5. Create and Access List Elements. Create a list containing five different fruits and print the third fruit.
ls = ["aplle", "melon", "grape", "banana", "orange"]
print(ls[2])
print(ls[3])
6. Concatenate Two Lists. Create two lists of numbers and concatenate them into a single list.


ls = [435,571,527]
ls2 = ["lemon", "banana", "orange"]
ls.extend(ls2)
ls
7. Extract Elements from a List. Given a list of numbers, extract the first, middle, and last elements and store them in a new list.
ls = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
first = ls[0]
middle = ls[len(ls)//2]
last = ls[-1]
ls2 = [first, middle, last]
print(ls2) 
8. Check Element in a List. Given a list of cities, check if "Paris" is in the list and print the result.
ls = ["London", "Tashkent", "Urgench", "Moscow", "Paris"]

if "Paris" in ls:
    print(ls)

9. Duplicate a List Without Using Loops. Create a list of numbers and duplicate it without using loops.
ls = [1,2,3,4,5,6,7]
ls2 = ls * 2
print(ls2)
10. Swap First and Last Elements of a List. Given a list of numbers, swap the first and last elements.


ls = [1,2,3,4,5,6,7,8,9,10]
ls[0], ls[-1] = ls[-1], ls[0]
print(ls)
