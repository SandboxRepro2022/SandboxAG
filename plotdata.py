#! /bin/python3

import pandas as pd

coviddata = pd.read_table("covid_aggregated.txt")
print(coviddata.head())
#plot(coviddata[1],coviddata[2])
#lines(coviddata[1],coviddata[2])
