file = open("hello.txt", 'w')
file.write("Hello 1")
file.close()

file = open("hello.txt", 'w')
file.write("Hello 1\n")
file.write("Hello 2")

file.close()

file = open("line.txt", 'w')
line = ["Line 1", "Line 2", "Line 3"]
for item in line:
    file.write(item + "\n")
file.close()
