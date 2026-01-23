import pandas as pd
import numpy as np



read_csv = pd.read_csv('handling missing data fillna dropna/weather_data.csv',parse_dates=['day'])

# print(read_csv.info())

print(read_csv)

read_csv.set_index('day',inplace=True)
# print(read_csv)

# fillna

# read_csv = read_csv.fillna(0)
# print(read_csv)


# fillna in diff columns
# read_csv = read_csv.fillna({
#     'temperature': 0,
#     'windspeed': 0,
#     'event': 'no event'
# })
# print(read_csv)

# fill na with forward fill
# read_csv = read_csv.fillna(method='ffill')
# print(read_csv)

# fill na with backward fill
# print(read_csv)
# read_csv = read_csv.fillna(method='bfill')
# print(read_csv)



# fill na  with axis 
# print(read_csv)
# read_csv = read_csv.fillna(method='bfill', axis=1)
# print(read_csv)

# fill na  with limit 
# print(read_csv)
# read_csv = read_csv.fillna(method='bfill', axis=1)
# print(read_csv)

# drop na
# print(read_csv)
# read_csv = read_csv.dropna()
# print(read_csv)


print(read_csv)
read_csv = read_csv.dropna(how='all')
print(read_csv)
