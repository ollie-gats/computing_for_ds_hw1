##############

# Now imagine you have a certain data structure that
# contains information about different countries and
# the number of people who was registered with covid
# in a weekly basis.
# e.g. {'Spain': [4, 8, 2, 0, 1], 'France': [2, 3, 6],
#       'Italy': [6, 8, 1, 7]}
# Assuming that the moment they started reporting the
# number of registered cases is not the same (thus
# the length of the lists can differ)


def total_registered_cases(dict_countries: dict, country: str) -> int:
    """ Returns the total number of cases registered so far in the specific country

    Args:
        dict_countries (dict): A dictionary that contains information about different countries and
        the number of people who was registered with covid in a weekly basis
        country (str): Country name

    Returns:
        int: The total number of cases registered so far in the specific country
    """
    return sum(dict_countries[country])


dict_1 = {'Spain': [4, 8, 2, 0, 1], 'France': [2, 3, 6], 'Italy': [6, 8, 1, 7]}
print(total_registered_cases(dict_1, 'Spain'))


def total_registered_cases_per_country(dict_countries: dict) -> dict:
    """ Returns a dictionary with a key per each country and as value the total number of cases
        registered so far that the country had

    Args:
        dict_countries (dict): A dictionary that contains information about different countries and
        the number of people who was registered with covid in a weekly basis

    Returns:
        dict: A dictionary with a key per each country and as value the total number of cases
        registered so far that the country had
        """
    return {country: total_registered_cases(dict_countries, country) for country in dict_countries}


print(total_registered_cases_per_country(dict_1))


def country_with_most_cases(dict_countries: dict) -> str:
    """ Returns the country with the greatest total amount of cases

    Args:
       dict_countries (dict): A dictionary that contains information about different countries and
       the number of people who was registered with covid in a weekly basis

    Returns:
       str: The country with the greatest total amount of cases
    """
    d = total_registered_cases_per_country(dict_countries)
    return max(d, key=d.get)


print(country_with_most_cases(dict_1))
