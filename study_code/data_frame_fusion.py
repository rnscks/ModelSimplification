import pandas as pd

df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df2 = pd.DataFrame({'A': [7, 8, 9], 'B': [10, 11, 12]})

result = pd.concat([df1, df2], axis=0, ignore_index=True)  # 위아래로 연결

print(result)