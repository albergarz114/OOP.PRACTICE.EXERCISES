#if statement
#temperature = int(input("what is the temperature? "))

#if temperature <= 20:
#    print("You need boots")
#elif temperature <= 30:
#    print("You need a coat")
#elif temperature <= 70:
#    print("you need a jacket")
#else:
#    print("It's nice outside!")

#for loop

string = "Alberto Garza"

for i in string:
    print(i)

# Lists/For loop

my_list = ["item1", "item2", "item3"]

for i in my_list:
    print(i)

# practice random loop/list

my_family = ["Ulrike", "Michael", "Michelle", "Alberto" ]

for i in my_family:
    print(i)

# While loop

on = True
i = 0
while on:
    var = input("continue running while loop y or no")
    i += 1
    print(i)
    if var == "n":
        on = False


