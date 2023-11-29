import pycountry
all_countries = list(pycountry.countries)
country_choices = [(country.alpha_2, country.name) for country in all_countries]
