file = open("example.txt")
content = file.read()
print(content)

content = file.readlines()
print(content)

file.seek(0)
content = file.readlines()
print(content)

content = [i.rstrip("\n") for i in content]
print(content)
