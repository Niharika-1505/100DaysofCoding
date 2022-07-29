import pandas as pd

# Reading page1 table content
Page_url = "https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors"
table = pd.read_html(Page_url)
payscale_df = table[0].copy()
payscale_df.columns = ["Rank", "Major", "Degree Type", "Early Career Pay", "Mid-Career Pay", "% High Meaning"]
# Reading through the table contents from page2 until the end
for page_number in range(2, 35):
    table = pd.read_html(f"{Page_url}/page/{page_number}")
    page_df = table[0].copy()
    page_df.columns = ["Rank", "Major", "Degree Type", "Early Career Pay", "Mid-Career Pay", "% High Meaning"]
    payscale_df = payscale_df.append(page_df, ignore_index=True)

print(f"24. Prints count, No. of unique rows, Top, frequency\n\n{payscale_df.describe()}")

# Cleaning the data
payscale_df["Rank"] = payscale_df["Rank"].str.replace("Rank:", "")
payscale_df["Major"] = payscale_df["Major"].str.replace("Major:", "")
payscale_df["Degree Type"] = payscale_df["Degree Type"].str.replace("Degree Type:", "")
# so $ gets treated as a character
payscale_df["Early Career Pay"] = payscale_df["Early Career Pay"].str.replace("Early Career Pay:$", "", regex=False)
payscale_df["Early Career Pay"] = payscale_df["Early Career Pay"].str.replace(",", "")
payscale_df["Mid-Career Pay"] = payscale_df["Mid-Career Pay"].str.replace("Mid-Career Pay:$", "", regex=False)
payscale_df["Mid-Career Pay"] = payscale_df["Mid-Career Pay"].str.replace(",", "")
payscale_df["% High Meaning"] = payscale_df["% High Meaning"].str.replace("% High Meaning:", "")
payscale_df["% High Meaning"] = payscale_df["% High Meaning"].str.replace("%", "")

print(f"25. Prints types of each column in the dataframe:\n{payscale_df.dtypes}")

# Converting the data types
payscale_df["Rank"] = payscale_df["Rank"].astype(int)
payscale_df["Early Career Pay"] = payscale_df["Early Career Pay"].astype(int)
payscale_df["Mid-Career Pay"] = payscale_df["Mid-Career Pay"].astype(int)

# Dataframe to csv
payscale_df.to_csv("salaries_by_college_major_29072022.csv", index=False)
