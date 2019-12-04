def age_foo(age):
    new_age = float(age) + 50
    return new_age


age = int(input("Enter your age: "))

if age < 150:
    age_foo(age)
else:
    print("How is that possible?")
