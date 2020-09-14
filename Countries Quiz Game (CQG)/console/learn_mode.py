import temp
import search_lib as sl
import pandas as pd
from numpy import isnan

df = pd.DataFrame()
continents = temp.continents


def clear_screen():
    temp.clear()


def mode_message():
    temp.clear()
    print(temp.line())
    print(temp.title('Learning Mode'))
    print(temp.line())


def initialization():
    data = temp.read_data()
    return data


def choices(a, n):
    return temp.choices_to_n(a, n)


def sub_mode():
    print("1 - continents statistics")
    print("2 - countries information")
    choice = choices(1, 2)
    return choice


def n_countries(n):
    continent = continents[n - 1]
    number = df.query('continent == "{}"'.format(continent)).count()['country']
    return int(number)


def has_no_capital(n):
    continent = continents[n - 1]
    number = df.query('continent == "{}"'.format(continent))['capital'].isna().sum()
    return number


def unique_languages(n):
    continent = continents[n - 1]
    frame = df.query('continent == "{}"'.format(continent))['language']
    ls = []
    for i in frame:
        if str(i) != 'nan':
            l = i.split(',')
            for j in l:
                ls.append(j.strip())
    return pd.Series(ls)


def print_language_details(n):
    languages = pd.Series()
    if n == 7:
        for continent_number in range(6):
            languages = languages.append(unique_languages(continent_number + 1), ignore_index=True)
    else:
        languages = unique_languages(n)
    des = languages.describe()
    unique = des['unique']
    print("{:{align}{width}} languages".format(unique, align='<', width='5'))
    top = des['top']
    freq = des['freq']
    print('the most spoken languages:')
    print('-' * (40 + 4))
    rest_top_languages = dict()
    if n == 7:
        rest_top_languages = dict(languages.value_counts()[:10])
    else:
        rest_top_languages = dict(languages.value_counts()[:3])
    print("{:{align}{width}} | {:{align}{width}}|".format('language', 'number of countries', align='^', width=20))
    print('-' * (40 + 4))
    for language in rest_top_languages:
        freq = rest_top_languages[language]
        print("{:{align}{width}} | {:{align}{width}}|".format(language.strip(), freq, align='^', width=20))
    print('-' * (40 + 4))


def all_continents():
    continent = "All the continents"
    countries, no_capital = 0, 0
    for i in range(6):
        countries += n_countries(i + 1)
        no_capital += has_no_capital(i + 1)
    return continent, countries, no_capital


def print_continent_info(continent, countries, no_capital):
    print(temp.line('-', 44))
    print(temp.title(continent, '^', 44))
    print(temp.line('-', 44))
    print(temp.prefix_word(countries, 'countries', position='<', width='5'))
    print(temp.prefix_word(no_capital, 'countries has no official capital', position='<', width='5'))


def continent_info(n):
    clear_screen()
    if n == 7:
        continent, countries, no_capital = all_continents()
        print_continent_info(continent, countries, no_capital)
    else:
        continent = continents[n - 1]
        countries = n_countries(n)
        no_capital = has_no_capital(n)
        print_continent_info(continent, countries, no_capital)
    print_language_details(n)


def continents_mode():
    clear_screen()
    print("select:")
    for i in range(len(continents) + 1):
        if i < 6:
            print("{} - {}".format(i + 1, continents[i]))
        else:
            print("7 - All")
    choice = choices(1, len(continents) + 1)
    continent_info(choice)


def print_suggestions(suggestions):
    print('Showing results for')
    n = len(suggestions)
    for i in range(n):
        print(temp.prefix_word(i + 1, suggestions[i], width=3))
    print(temp.prefix_word(0, 'to enter another country instead', width=3))


def print_country_info(country):
    clear_screen()
    print(temp.line())
    print(temp.title(country))
    print(temp.line())
    row = df.query('country == "{}"'.format(country))
    columns = row.columns[1:]
    row_values = row.values[0][1:]
    zp = dict(zip(columns, row_values))
    for i in zp:
        if pd.isna(zp[i]):
            zp[i] = 'no official {}'.format(i)
    for i in zp:
        print(temp.prefix_word(word=i, sentence=zp[i], width=15))
    print(temp.line())


def search():
    suggestions = []
    while not suggestions:
        print("please enter country name:")
        country_input = input()
        suggestions = sl.conclusion(country_input, df['country'])
        n = len(suggestions)
        if n == 0:
            print('please enter country name correctly')
        elif len(suggestions) == 1:
            country = suggestions[0]
            if not sl.exact_match(country, country_input):
                print("Do you mean {}?".format(country))
                temp.print_yes_no()
                response = temp.choices_0_1()
                if not response:
                    suggestions = []
        else:
            print_suggestions(suggestions)
            choice = choices(0, len(suggestions))
            if choice == 0:
                suggestions = []
            else:
                country = suggestions[choice - 1]
                break
    return country


def countries_mode():
    clear_screen()
    country = search()
    print_country_info(country)


def again():
    print('Do you want to stay at learning mode?\n')
    return temp.again()


def main():  # TODO
    global df
    mode_message()
    df = initialization()
    Continue = True
    while Continue:
        s_mode = sub_mode()
        if s_mode == 1:
            continents_mode()
        else:
            countries_mode()
        Continue = again()
        clear_screen()
