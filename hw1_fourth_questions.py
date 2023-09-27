###############
# Use the data in covid.csv for this exercise
#
# 10) In a separate file, write a piece of code that
# loads the covid.csv file and prints the list of countries
#  and the total average of death/confirmed among those countries
# for those countries that have more than 500, 1000 and 5000
# active cases respectively.
# Follow DRY principles in order to complete this exercise.

import pandas as pd


def load_data(filename):
    return pd.read_csv(filename)


def get_info(df, active_cases):
    df["death/confirmed"] = df.Deaths / df.Confirmed
    df_filtered = df[df.Active > active_cases]
    print(list(df_filtered.Country))
    print(f'Total average of deaths for countries that have more than {active_cases} active cases: '
          f'{round(df_filtered.Deaths.mean())}')
    print(f'Total average of confirmed cases for countries that have more than {active_cases} active cases: '
          f'{round(df_filtered.Confirmed.mean())}')
    print(f'Total average of death/confirmed cases for countries that have more than {active_cases} active cases: '
          f'{round(df_filtered["death/confirmed"].mean(),2)}\n')


data = load_data('data/covid.csv')
for c in [500, 1000, 5000]:
    print(f'Number of active cases: {c}')
    get_info(data, active_cases=c)

