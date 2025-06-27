#stage one is complete
name = input("Whats your name : ")
age = int(input("How old are you? "))
heght = float(input("Whats your height in CM ? "))

print(f"Hello {name}, You are {age} years old and {heght}cm tall")
print(type(name))
print(type(heght))
print(type(age))

is_adult = age >=18
print(is_adult)

