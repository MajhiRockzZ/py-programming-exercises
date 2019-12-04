with open("txt/example.txt", "a+") as file:
    file.seek(0)
    content = file.read()
    file.write("\nMore New Content")
