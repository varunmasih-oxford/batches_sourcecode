import pandas as pd

# marks_hindi = [10,20,30]
# series_pd = pd.Series(marks_hindi)

# lable

# series_pd = pd.Series(data = marks_hindi, index = [10,20,30])

# lbl = [10,20,30]
# series_pd = pd.Series(data = marks_hindi, index = lbl)

data = {
'marks_hindi' : [10,20,30],
'marks_english' : [40,50,60],
'marks_maths' : [70,80,90]
}


# dataframe_pd = pd.DataFrame(data)
dataframe_pd = pd.DataFrame(data, index=['ritu','aditya','mayank'])


print(dataframe_pd)
