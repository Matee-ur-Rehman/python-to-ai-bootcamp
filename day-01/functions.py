def greet(name="Student"):
    print(f"Hello, {name}!")
greet("Akif")
greet()


def introduce(name, age):
    print(f"My name is {name}, and I am {age}.")
introduce(age=20, name="Akif")



//practice

# Default parameter ke saath
def greet(name="Student", city="Pakistan"):
    print(f"Hello {name}, welcome from {city}!")

greet("Matee", "Islamabad")
greet()


# Keyword arguments ke saath
def introduce(name, age, city):
    print(f"My name is {name}, I am {age} years old, and I live in {city}.")

introduce(age=22, city="Rawalpindi", name="Matee")
