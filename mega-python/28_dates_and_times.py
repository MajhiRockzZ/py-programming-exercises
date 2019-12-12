import time
import datetime

"""DATETIME"""

datetime.datetime.now()
print(datetime.datetime.now())

yesterday = datetime.datetime(2016, 5, 13, 11, 0, 0, 0)
now = datetime.datetime.now()
print(yesterday)
print(now)
print(now - yesterday)

"""
This script creates a file.
"""

filename = datetime.datetime.now()

# Create file


def create_file():
    """This function creates an file"""
    with open(filename.strftime("%Y-%m-%d-%H-%M-%S-%f") + ".txt", "w") as file:
        file.write("")


create_file()


# strftime.org ----> site for formating character list
print(now.strftime("%Y-%m-%d-%H-%M-%S-%f"))

after = now + datetime.timedelta(days=2)
print(after)
after = now + datetime.timedelta(seconds=2)
print(after)

"""TIME"""

lst = []
for i in range(5):
    lst.append(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f"))
    time.sleep(1)

print(lst)
