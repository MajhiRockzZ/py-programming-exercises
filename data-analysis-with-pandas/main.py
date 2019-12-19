import pandas

df1 = pandas.DataFrame([[2, 4, 6], [10, 20, 30]])

df1 = pandas.DataFrame([[2, 4, 6], [10, 20, 30]], columns=[
                       "price", "Age", "Valuse"], index=["First", "Second"])

print(df1)

df2 = pandas.DataFrame([{"Name": "John"}, {"Name": "Jack"}])

print(df2)

df2 = pandas.DataFrame([{"Name": "John", "Surname": "John"}, {"Name": "Jack"}])

print(df2)

print(df1.mean())

print(df1.mean().mean())