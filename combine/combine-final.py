import pandas as pd

joined = None

start = 2002
end = 2019

for year in range(start, end+1):
    curr_df = pd.read_csv(f'joined-data/{year}JoinedData.csv', index_col=0)
    if joined is None:
        joined = curr_df
        continue

    print (curr_df.shape)
    joined = pd.concat([joined, curr_df], join='inner', sort=False)

print (joined.shape)

joined.to_csv('FinalJoinedData.csv')