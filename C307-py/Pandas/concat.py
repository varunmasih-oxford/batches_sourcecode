import pandas as pd


data1 = pd.DataFrame({
    'city':["delhi","Chandighar","A&N"],
    'temp':[32,45,30],
    'hum':[80,60,78]
})

data2 = pd.DataFrame({
    'city':["Haryana","Rajasthan","UP"],
    'temp':[12,50,30],
    'hum':[80,60,78]
})

# print(data1)
# print(data2)


# fullData = pd.concat([data1,data2])
# fullData = pd.concat([data1,data2],ignore_index=True)
# fullData = pd.concat([data1,data2],keys=["UT","ST"])
fullData = pd.concat([data1,data2],keys=["UT","ST"])
# print(fullData.loc['UT'])
# print(fullData.loc['ST'])


data3 = pd.DataFrame({
    'city':["Haryana","Rajasthan","UP"],
    'temp':[12,50,30]
})
data4 = pd.DataFrame({
    'city':["Haryana","Rajasthan","UP"],
    'hum':[80,60,78]
})

# fullData = pd.concat([data3,data4],axis=0)
# fullData = pd.concat([data3,data4],axis=1)
# print(fullData)
