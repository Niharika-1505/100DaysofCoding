import numpy as np
import pandas as pd


def isNaN(string):
    return string != string


# create DataFrame1
data1 = [[1, 'Niha', 42000], [2, 'Karthik', 40000], [3, 'Ajay', 50000], [114, 'Sam', 60000], [80, "Vasantha", 35000],
         [56, "Sri", 46000], [325, "Prem", 80000]]
df1 = pd.DataFrame(data1, columns=['ID', 'Name', 'Salary'])

# create DataFrame2
data2 = [[1, 'Niha', "GL51"], [80, 'VasanthaMenon', "LS11"], [56, 'Sri', "E12"], [114, 'Sam', "BH1"]]
df2 = pd.DataFrame(data2, columns=['ID', 'Name', 'Postcode_Sector'])

# Use this if you want to merge both the data frame columns and then set status
# df3 = pd.merge(df1, df2, how="left", on="ID") # Merge based on one column
df3 = pd.merge(df1, df2, how="left", on=["ID", "Name"])  # Merge based on more than one column
df3.shape
# df3["Status"] = np.where(df3["Name_x"] == df3["Name_y"], True, False)
df3["Status"] = np.where(isNaN(df3["Postcode_Sector"]), False, True)
print(df3)

# Use this if you only want dataframe 1 values but set status based on dataframe 2 values
df1["Status"] = df1["ID"].isin(df2["ID"])
print(df1)
