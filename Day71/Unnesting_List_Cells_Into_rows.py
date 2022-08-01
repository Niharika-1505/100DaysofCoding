import pandas as pd

data = [
    [0, [1, 2, 3], [4, 5, 6], 7],
    [0, [1, 2, 3], [4, 5, 6], 7],
    [0, [1, 2, 3], [4, 5, 6], 7],
    [0, [1, 2, 3], [4, 5, 6], 7],
    [0, [1, 2, 3], [4, 5, 6], 7]
]

df = pd.DataFrame(data, columns=['one', 'two', 'three', 'four'])
print(df)
# Exploding dataframe lists into rows
df2 = df.explode('two')
print(df2)

data1 = {'product': ['Tablet', "['30072022', '29072022']", 'Laptop', 'Monitor'],
         'price': [250, 100, 1200, 300]
         }

df3 = pd.DataFrame(data1)
# print(df3)

# Converting dataframe to list
products_list = df3.values.tolist()
print(products_list)

