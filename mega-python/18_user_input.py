# planet = input(f"What planet are you from? ")
# print(planet)

def currency_converter(rate, euros):
    dollar = euros * rate
    return dollar

r = float(input("Enter rate: "))
e = float(input("Enter euros: "))
result = currency_converter(r,e)
print(result)

