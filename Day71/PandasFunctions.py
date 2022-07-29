"""Advanced - Data Exploration with pandas: College Major vs Your Salary"""
import pandas as pd

df = pd.read_csv("salaries_by_college_major.csv")
# print(f"1. Head prints first 5 rows in the dataframe\n\n {df.head()}\n")
# print(f"2. Shape prints number of rows and columns in the dataframe{df.shape}\n")
# print(f"3. Column names: {df.columns}\n")
# print(f"4. Are there any missing values in the dataframe:\n {df.isna()}\n")
# print(f"5. Tail prints last 5 rows of the dataframe:\n {df.tail()}\n")
clean_df = df.dropna()
# print(f"6. Last 5 rows after dropping rows with NaN in the dataframe:\n {clean_df.tail()}\n")
# print(f"7. To access one column data in the dataframe:\n {clean_df['Starting Median Salary']}")
# print(f"8. Prints maximum value in that column: {clean_df['Starting Median Salary'].max()}\n")
# print(f"9. Prints index of the maximum value in that column: {clean_df['Starting Median Salary'].idxmax()}\n")
# print(f"10. Prints cell value of a specific column and row: {clean_df['Undergraduate Major'].loc[43]}\n")
# print(f"11. Prints cell value of a specific column and row: {clean_df['Undergraduate Major'][43]}\n")
# print(f"12. Prints entire row data:\n\n{clean_df.loc[43]}\n")

'''What college major has the highest mid-career salary? How much do graduates with this major earn?'''
# College_Major_With_Highest_Mid_Career_Salary=clean_df['Undergraduate Major'].loc[clean_df['Mid-Career Median Salary'].idxmax()]
# print(f"13. What college major has the highest mid-career salary? {College_Major_With_Highest_Mid_Career_Salary}")

'''Which college major has the lowest starting salary and how much do graduates earn after university?'''
# print(clean_df)
# College_Major_With_Lowest_Starting_Salary=clean_df['Undergraduate Major'][clean_df['Starting Median Salary'].idxmin()]
# print(f"14. Which college major has the lowest starting salary? {College_Major_With_Lowest_Starting_Salary}")

'''Which college major has the lowest mid-career salary and how much can people expect to earn with this degree?'''
# College_Major_With_Lowest_Mid_Career_Salary=clean_df.loc[clean_df['Mid-Career Median Salary'].idxmin()]
# print(f"15. What college major has the lowest mid-career salary?\n {College_Major_With_Lowest_Mid_Career_Salary}")

# print(f"16. Prints all the rows that meets the condition:\n\n {clean_df.loc[clean_df['Mid-Career 10th Percentile Salary'] >= 26000]}")

'''17. Lowest Risk Majors
A low-risk major is a degree where there is a small difference between the lowest and highest salaries. In other words, if the difference between the 
10th percentile and the 90th percentile earnings of your major is small, then you can be more certain about your salary after you graduate.'''
# difference_in_salaries=clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
'''OR can use subtract method '''
# clean_df['Mid-Career 90th Percentile Salary'].subtract(clean_df['Mid-Career 10th Percentile Salary'])
# clean_df.insert(5,'difference_in_salaries',difference_in_salaries)
# low_difference_in_salaries=clean_df.sort_values('difference_in_salaries')
# low_difference_in_salaries[['Undergraduate Major', 'difference_in_salaries']].head()


'''18. Find the top 5 degrees with the highest values in the 90th percentile. OR Majors with the Highest Potential'''
# top_5_degrees=clean_df.sort_values("Mid-Career 90th Percentile Salary", ascending=False)
# top_5_degrees[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head()

'''19. Find the degrees with the greatest spread in salaries. Which majors have the largest difference between high and low earners after graduation. OR 
Majors with the Greatest Spread in Salaries'''
# difference_in_salaries=clean_df['Mid-Career 90th Percentile Salary'].subtract(clean_df['Mid-Career 10th Percentile Salary'])
# clean_df.insert(5,'difference_in_salaries',difference_in_salaries)
# high_difference_in_salaries=clean_df.sort_values('difference_in_salaries', ascending=False)
# high_difference_in_salaries[['Undergraduate Major', 'difference_in_salaries']].head()

'''20.Grouping and Pivoting Data with Pandas'''
# print(f"20. Groups By based on columns specified and returns count:\n\n{clean_df.groupby('Group').count()}\n")
# print(f"21. Groups By based on columns specified and returns sum:\n\n{clean_df.groupby('Group').sum()}\n")
pd.options.display.float_format = '{:,.2f}'.format  # Tells the pandas to round off float values to 2 decimals.
print(f"22. Groups By based on columns specified and returns mean:\n\n{clean_df.groupby('Group').mean()}\n")
