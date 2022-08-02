"""Advanced - Data Visualization with Matplotlib: Programming Languages"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("QueryResults.csv", header=0, names=["DATE", "TAG", "POSTS"])

'''Challenge: Look at the first and last 5 rows of the DataFrame.'''
print(f"First 5 rows:\n{df.head()}\n\nLast 5 rows:\n{df.tail()}\n")

'''Challenge: Check how many rows and how many columns there are. What are the dimensions of the dataframe?'''
print(f"No. of columns and rows: {df.shape}\n")

'''Challenge: Count the number of entries in each column of the dataframe'''
print(f"Count of number of entries in each column:\n{df.count()}\n")

'''Challenge: Calculate the total number of post per language. Which Programming language has had the highest total 
number of posts of all time? '''
total_post_per_lang_df = df.groupby('TAG').sum()
pl_with_more_posts = total_post_per_lang_df['POSTS'].idxmax()
print(
    f"Total no. of posts per language:\n{total_post_per_lang_df}\n\nand {pl_with_more_posts} is the programming language with more posts\n")

'''Challenge: How many months of data exist per language? Which language had the fewest months with an entry?'''
total_months_of_data_per_lang = df.groupby('TAG').count()
pl_with_few_months_entry = total_months_of_data_per_lang['POSTS'].idxmin()
print(
    f"No. of months of data per language:\n{total_months_of_data_per_lang}\n\nand {pl_with_few_months_entry} is the programming language with few months of entry\n")

'''Data Cleaning'''

'''Change Date format to datetime object'''
print(f"Type of the Date: {type(df['DATE'][1])}")
pd.to_datetime(
    df["DATE"][1])  # This will change the datatype to datetime but also print the date in this 2022-07-01 00:00:00
df["DATE"] = pd.to_datetime(
    df["DATE"])  # This will change the datatype to datetime but print the date in this 2022-07-01
print(f"Changing date format from str to datetime:\n\n{df['DATE']}\n")

'''Data Manipulation'''

reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')
'''Challenge: What are the dimensions of our new dataframe? How many rows and columns does it have?'''
print(
    f"No. of columns and rows in reshaped: {reshaped_df.shape}\nFirst 5 rows:\n{reshaped_df.head()}\n\nLast 5 rows:\n{reshaped_df.tail()}\n\nPrints column names:{reshaped_df.columns}\n")
print(f"Count of number of entries in each column:\n{reshaped_df.count()}\n")

# replace NaN values
reshaped_df.fillna(0, inplace=True)
# confirm that there are no NaN values
print(f"Are there any Nan values: {reshaped_df.isna().values.any()}")
print(reshaped_df)

"""Data Visualization with with Matplotlib"""
# change the size of the graph
plt.figure(figsize=(10, 6))

# Increase x and y axis labels size
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)

# Add label names to x and y axis
plt.xlabel("Year", fontsize=13)
plt.ylabel("Posts", fontsize=13)

# Plot the data on the graph
plt.plot(reshaped_df.index, reshaped_df["python"])

'''Challenge: Show two line (e.g. for Java and Python) on the same chart.'''
plt.figure(figsize=(10, 6))
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)
plt.xlabel("Year", fontsize=13)
plt.ylabel("Posts", fontsize=13)

# Changing y-axis limit from 30000 to 40000
plt.ylim(0, 40000)

plt.plot(reshaped_df.index, reshaped_df["python"])
plt.plot(reshaped_df.index, reshaped_df["java"])

'''Challenge: Multi-line charts with matplotlib'''
plt.figure(figsize=(10, 6))
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)
plt.xlabel("Year", fontsize=13)
plt.ylabel("Posts", fontsize=13)
plt.ylim(0, 40000)

# Loops through the dataframe columns and plot all the columns on the graph and add
for column in reshaped_df.columns:
    plt.plot(reshaped_df.index, reshaped_df[column],
             linewidth=3, label=reshaped_df[column].name)

# include a legend
# loc=2 means "upper left"
plt.legend(fontsize=12, loc=2)

# smooth out the data using rolling mean
# The window is number of observations that are averaged here is 6
roll_df = reshaped_df.rolling(window=6).mean()

plt.figure(figsize=(10, 6))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)

# plot the roll_df instead
for column in roll_df.columns:
    plt.plot(roll_df.index, roll_df[column],
             linewidth=3, label=roll_df[column].name)

plt.legend(fontsize=16)

# using a smaller window
# The window is number of observations that are averaged here is 3
roll_df = reshaped_df.rolling(window=3).mean()

plt.figure(figsize=(10, 6))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)

# plot the roll_df instead
for column in roll_df.columns:
    plt.plot(roll_df.index, roll_df[column],
             linewidth=3, label=roll_df[column].name)

plt.legend(fontsize=16)

# using a larger window
# The window is number of observations that are averaged here is 12
roll_df = reshaped_df.rolling(window=12).mean()

plt.figure(figsize=(10, 6))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)

# plot the roll_df instead
for column in roll_df.columns:
    plt.plot(roll_df.index, roll_df[column],
             linewidth=3, label=roll_df[column].name)

plt.legend(fontsize=16)
