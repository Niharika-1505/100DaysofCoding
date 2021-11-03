def add_new_country(country_visited, no_of_visits, cities_visited):
    another_country = {"country": country_visited, "visits": no_of_visits, "cities": cities_visited}
    travel_log.append(another_country)


travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
