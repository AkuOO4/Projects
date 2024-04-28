import numpy as np
import pandas as pd
movies_df= pd.read_excel("./datasets/test.xlsx")

print(movies_df.dtypes)
for i in range(len(movies_df)):
    try:
        movies_df["id"][i] = int(movies_df["id"][i])

    except:
        movies_df.drop(i,inplace=True)

movies_df[['id']]=movies_df[['id']].apply(pd.to_numeric)
movies_df.to_excel('./datasets/new_test.xlsx')
print("\nafter conversion\n")
print(movies_df.dtypes)
print(movies_df)