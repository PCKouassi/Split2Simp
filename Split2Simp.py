import pandas as pd
import matplotlib as mp
import numpy as np
import sys
from datetime import date
from pathlib import Path

paths = [path for path in Path('/Users/peter/Documents/Finance/').resolve().glob("**/*export*.csv")]

print(paths)
split_expt= pd.read_csv(paths[0])

today = date.today()

input_date = str(sys.argv[1])

for i, a_date in enumerate(split_expt["Date"]):
    if a_date == input_date:
        print(a_date)
        date_index = i
        print(date_index)


split_expt_to_date = split_expt.iloc[date_index:split_expt.size-3]
print(split_expt_to_date)


split_expt_to_date.to_csv(index= False, path_or_buf='simp_import.csv',columns=['Date','Description','Peter Kouassi','Category'],header=['Date','Payee','Amount','Tags'])

