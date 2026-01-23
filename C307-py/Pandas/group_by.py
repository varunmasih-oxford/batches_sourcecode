import pandas as pd


read_csv = pd.read_csv('weather_by_cities.csv',parse_dates=['day'])

# print(read_csv.info())

gd = read_csv.groupby('city')
# print(gd)

# for c,d in gd:
#     print("\n")
#     print("\n")
#     print(c)
#     print(d)


# for a,b in gd:
#     print(a)


# paris = gd.get_group("paris")
# print(paris)



# print(gd.size())
# print(gd.describe())
# print(gd.min())
# print(gd.max())
# print(gd.count())
# print(gd['temperature'].mean())

# print(read_csv)