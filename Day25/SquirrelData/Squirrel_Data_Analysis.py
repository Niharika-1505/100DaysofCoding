import pandas

squirrel_data = pandas.read_csv("Squirrel_data.csv")
gray_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

squirrel_data_dict = {
    "Squirrel_Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}
squirrel_dataframe = pandas.DataFrame(squirrel_data_dict)
squirrel_dataframe.to_csv("squirrel_count_based_on_colour.csv")
