### Functions

def add(x, y=1):
    return x + y

a = add(10, 20)
b = add(10)
print(a)
print(b)


# Keyword Arguments
def student(name, age):
    print(f"Name: {name}, Age: {age}")

student(age=21, name="Alice")  # order doesn’t matter