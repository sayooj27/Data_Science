import pandas as pd
import numpy as np
num={'Set_of_NUmbers':[2,3,5,7,11,13,np.nan,19,23,np.nan]}
df=pd.DataFrame(num,columns=['Set_of_NUmbers'])
df['Set_of_NUmbers']=df['Set_of_NUmbers'].fillna(0)
print(df)
