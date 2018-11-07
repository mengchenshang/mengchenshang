#!/usr/bin/env python
# coding: utf-8

# In[168]:


import pandas as pd
import numpy as np
data_csv = pd.read_csv('D:/Matlab/in.csv', encoding='GBK')
leng           = 10;
fastlen       = 2;
slowlen       = 30;
AMAvalue = np.zeros(200)


# MAIN FUNCTION
def AMA(Price, leng, fastlen, slowlen, prv_AMAvalue):
    # init AMA parameters
    fast = 2/(fastlen + 1);
    slow = 2/(slowlen + 1);

    # calculate EMAvalue
    direction = np.abs( Price.iloc[-1]- Price.iloc[-1-leng] );
    p1        = np.array(Price[-1-leng+1:Price.size]);
    p2        = np.array(Price[-1-leng:-1]);
    volatility = sum(abs(p1-p2));

    # the Efficiency_Ratio
    ER         = direction/volatility;
    smooth     = ER*(fast-slow)+slow;
    c          = smooth*smooth;
    return prv_AMAvalue + c*(Price.iloc[-1]-prv_AMAvalue);

# END

for t in range(leng+1, data_csv.size+1):
    AMAvalue[t-1] = AMA(data_csv.iloc[t-(leng+1):t], leng, fastlen, slowlen, AMAvalue[t-2])

data = pd.DataFrame(AMAvalue)
data.to_csv('D:/Matlab/test.csv')