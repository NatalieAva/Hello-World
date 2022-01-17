names = ["John","Andrew","Natalie","Emma"]

for i in names:
    print("Congratulations " + i)
    if isinstance(i, str):
        print("index " + i + " was a string, not an integer")

print(names[0])

lst1 = [3, 7, 8, 9, "11", 15, 25]
lst2 = []
lst2.append(lst1[5])
print(lst2)

for r in lst1:
    if isinstance(r, str):
        print("index " + r + " was a string, not an integer")
"""def my_function2():
   name = input("Please write your name")
   print("Hi, my name is" + name)
   return name"""

"""name = my_function2() # calling the function"""

"""def calculate_percentage(total_marks, marks):
    return (marks/total_marks)*100

def calculate_band(grade):
    if grade < 40:
        return "fail"
    if 40 <= grade <= 60:
        return "good"
    if grade > 90:
        return "excellent"
    else:
        return "very good"

grade = calculate_percentage(60,45)
band = calculate_band(grade)
print(band)"""

def f_1(Message):
    print(Message)
    return Message

returnedmessage = f_1("Hello World")
print(returnedmessage)

def f_2 ():
    return 100

returnednumber = f_2()
print(returnednumber)

def f_3 (List):
    return list(reversed(List))

returnedlist = f_3(["John","Andrew","Natalie","Emma"])
print(returnedlist)

def f_4(number):
    return number + 5

def f_5(number):
    return f_4(number)*2

out3 = f_5(2)
print(out3)




# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#get user input and assign to x (Temperature in Farenheight)
x = int(input('Temperature in Farenheight? '))
#Convert x to Celsius
converted = (x - 32) / 1.8
#output message displaying displaying celsius temperature
print(f'this is {converted} in celsius')

#print boxes black and white like a chessboard

'''column = 8
row = 8

for row if r < 8
    for column <8
        if c number is even
            print white box
        else
            print black box
            c + 1
r + 1'''

#psudocode for creating an 8x8 chess board with alternating black and white boxes

'''create 8x8 array
loop through x-axis [0-7]
loop through y-axis [0-7]
if sum of index locations even
black
if sum of index locations odd
white'''



