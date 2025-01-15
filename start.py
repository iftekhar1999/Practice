name = "Evan"
age = 25

print("Hello World !!!")
print("Name: ",name,"\nAge: ",age)
print("Name: ", name)
print("Age: ", age)
print(type(name))


#multiple variables

x,y,z="Dhaka","Chittagong","Khulna"

print(x)
print(y)
print(z)

country = ["USA","UK","UAE"]
a,b,c = country

print(a)
print(b)
print(c)

#conditional statement

p=200
q=300

if p>q:
    print("P is greater than Q")
elif q>p:
    print("Q is greater than P")
else:
    print("Both are equal")


#loop statement

country = ["USA","UK","UAE"]

for x in country:
    print("Country = ", x)

i=1
while i<=5:
    print(i,end=" ")
    i += 1

#store data
#===================================
#list
print()
food=["Pizza","Burger"]
print(food)
food.append("Pasta")
print(food)

num_list=[1,2,3,4,5]
sum_num=sum(num_list)
print("Summation: ",sum_num)


#Tuples

point=(3,4)
x,y=point
print("(x,y)= ",x,y)

fruits=("apple","orange","banana","mango")
print("Fruits: ",fruits)


#Set(curly_braces)

car={"BMW","Audi","Prado","BMW"}
print("Car: ",car)

#Dictionary

bike={"Owner":"Evan","Company":"Honda"}
print("Bike: ",bike)

print(bike["Owner"])#specification

bike["Company"]="Yamaha" #data modified
print("Bike: ",bike)

