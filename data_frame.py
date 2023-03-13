import pandas as pd
data = {
    "calories":[33,44,55],
    "duration":[2,4,6]
}
#dataframe => convert python dictionary to pandas data frame
df = pd.DataFrame(data)
print(df)

#locate
print(df.loc[0])