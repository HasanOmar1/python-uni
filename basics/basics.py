import os
#1
def greet():
    print("Hello, Python student!")
#2
def square(number:int):
    return number * number
#3
def is_even(number:int):
    if number % 2 == 0:
        return True
    return False

print("------------------- #1 -----------------")
greet()
print("------------------- #2 -----------------")
print("6^2 = " , square(6))
print("------------------- #3 -----------------")
print("is 4 even ? " , is_even(4))
print("is 7 even ? " , is_even(7))


#4
print("------------------- #4 -----------------")
numbers = [3,8,2,10,5]
for n in numbers:
    if n > 5:
        print(n)

#5
print("------------------- #5 -----------------")
student = {'name': 'Alice', 'grade': 88}
print("student name : " , student["name"])
print("student grade : " ,student["grade"])

#6
print("------------------- #6 -----------------")
car = {'brand': 'Toyota', 'year': 2020}
for key,value in car.items():
    print(key, " : ", value)

#7
print("------------------- #7 -----------------")
coordinates = (4,7)
print("coordinates x : ", coordinates[0])
print("coordinates y : ", coordinates[1])

#8
print("------------------- #8 -----------------")
set_list = {1,2,2,3,4,4,5}
print("set_list : ", set_list)
# it removes the duplicates

#10
def divided_number():
    try:
        num = int(input("Enter a number: "))
        result = 100 / num
        print(result)
    except ZeroDivisionError :
        print("You can't divide by zero")
        with open("error_log.txt", "a" , encoding="utf-8") as file:
            file.write("You can't divide by zero\n")
    except ValueError:
        print("You didn't enter a number")
        with open("error_log.txt", "a", encoding="utf-8") as file:
            file.write("You didn't enter a number\n")
    except Exception as e:
        print(e)
        with open("error_log.txt", "a", encoding="utf-8") as file:
            file.write(e , "\n")


#9+10
print("------------------- #9 -----------------")
def main():
    list_students = [
        {'name': 'Alice', 'grade': 88},
        {'name': 'Bob', 'grade': 90},
    ]

    for student in list_students:
        print(student)

    print("------------------- #10 -----------------")
    divided_number()
if __name__ == '__main__':
    main()