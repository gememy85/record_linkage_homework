#%%
import pandas as pd
import pickle 
import numpy as np

#%%
A = pd.read_csv('FileA.csv')
B = pd.read_csv('FileB.csv')

A.isna().sum() # middlename에 86개
B.isna().sum() # middlename에 65개

#%%
# 두 데이터셋의 컬럼은 같다.
A.columns.tolist()
B.columns.tolist()

# %%
# 1. 먼저 record pair 만든다
all_pairs = []
for _, rowA in A.iterrows():
    for _, rowB in B.iterrows():



# 2. record pair에 대해서 r vector만든다.
# 매칭 벡터를 만든다.


#%%
