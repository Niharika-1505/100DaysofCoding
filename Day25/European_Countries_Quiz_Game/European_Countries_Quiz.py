import turtle
import pandas

screen = turtle.Screen()
chinky = turtle.Turtle()
screen.title("European Countries Game")
image = "european_countries_img.gif"
screen.addshape(image)
turtle.shape(image)

countries_data = pandas.read_csv("european_countries.csv")
all_country_names_list = countries_data.country.to_list()
guessed_countries = []

while len(guessed_countries) < len(countries_data):
    answer_country = screen.textinput(title=f"{len(guessed_countries)}/{len(countries_data)} countries correct",
                                      prompt="What's another country name?").title()
    if answer_country == "Exit":
        missing_countries = []
        for country in all_country_names_list:
            if country not in guessed_countries:
                missing_countries.append(country)
        learning_file = pandas.DataFrame(missing_countries)
        learning_file.to_csv("learn_the_countries_here.csv")
        break
    if answer_country in all_country_names_list:
        guessed_countries.append(answer_country)
        chinky.hideturtle()
        chinky.penup()
        countries = countries_data[countries_data.country == answer_country]
        chinky.goto(int(countries.x), int(countries.y))
        chinky.write(answer_country)

# """Below code is to get coordinates on click...helps to get coordinates of each country where we want to display the
# name """
#
#
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
