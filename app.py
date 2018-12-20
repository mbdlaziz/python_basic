print("Hello World")

# string, interger, double, float, boolean, array, obj
#string
'''x = "x"
food = "apple pie"
my_favourite_food = "nasgor"
myFavouriteFood = "sate"

print(x)
print(food)
print(my_favourite_food)
print(myFavouriteFood)

#interger
number = 1
first_number = 2
second_number = 3

print(number)
print(first_number)
print(second_number)
print(first_number + second_number)

#double dan float
decimal = 1.2
my_decimal = 3.3

print(decimal + my_decimal)

#boolean
is_clean = True

print(is_clean and False)
print(is_clean or False)'''


#list
'''fruits = ["apple", "banana", "mango", "grape"]

print(fruits)
print(fruits[0])
#update list
fruits[3] = "cherry"

#add value on lists
fruits.append("orange")
print(fruits)

#delete value on list
del fruits[2]

print(fruits)'''


#dict
'''profile = {
    "first_name": "Abdul",
    "last_name": 'Aziz',
    "age": 16,
    "gender": "male",
    "is active": True,
    "friends": ["somad", "mamad", "budi"]
}
friends = profile['friends']
my_second_friends = friends[1]
print(my_second_friends)
print(profile)
print(profile["last_name"])
print(profile["friends"])
print(profile["friends"][2])'''


#list of dictionary
'''todos = [
    {"id": 1, "name": "washing car", "is done": False},
    {"id": 2, "name": "helping mom", "is done": True}
]
print(todos)
print(todos[1]['name'])'''


#for loop
'''for i in range(1, 10):
    print(i)

phones = ['xiaomi', 'iphone', 'samsung']
for phone in phones:
    print(phone)

phones = [
    {"id": 1, "name": "xiaomi"},
    {"id": 2, "name": "iphone"},
    {"id": 3, "name": "samsung"},
]
for phone in phones:
    print(phone)
    print(phone['name'])'''


#input
'''name = input("1. Mohon masukan nama anda: ")
address = input("2. mohon masukan alamat anda: ")

print("Hello %s, alamat anda berada di %s" %(name, address))

first_number = input("Masukan angka #1: ")
second_number = input("Masukan angka #2: ")

print(int(first_number) +int(second_number))'''


#if else conditional
'''age = input("Please input  your age: ")

#validation
if age.isdigit() == False:
    print("Please input correct age format")
else:
    age = int(age)

    if age > 13:
        print("You are allowed to wacth this movie")
    elif age <=13:
        print("You are not allowed to wacth this movie")'''


#method/function
'''operator = input("Please input operator (+ - / *): ")
first_number = input("#1: ")
second_number = input("#2: ")
first_number = int(first_number)
second_number = int(second_number)

def calculate(operator, first_number, second_number):
    if operator == "+":
        return first_number + second_number
    if operator == "-":
        return first_number - second_number
    if operator == "/":
        return first_number / second_number
    if operator == "*":
        return first_number * second_number

print(calculate(operator, first_number, second_number))

#     print(first_number + second_number)
#     # return first_number + second_number
# sum()
# print(sum())
'''


#class
'''class Employee():
    name = "Joko"

    def get_name(self):
        return self.name

#instantiate class
employee = Employee()
# employee.name = 'luna'
print(employee.get_name())'''


#error vid 12
'''class Employee():
    name = "Joko"

    def _init_(self, name, salary):
        self.name = name
        self.name = salary

    def get_name(self):
        return self.name

#instantiate class
employee = Employee()
# employee.name = 'luna'
print("%s " % employee.name)'''
