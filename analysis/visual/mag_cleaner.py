# mag_cleaner.py
# 20191118 - ryan pili
# 
# program to run after visMagnitude.m
# reads in ao_mag.csv and av_mag.csv
#   gives clear headers
#   computes dx & dy mean per dyad 
#   computes dx & dy mean per participant
#   computes dx & dy grand mean
# possibly graphs? good pract with seaborn 

from pathlib import Path
import loguru as log
import pandas as pd
from pprint import pprint
from matplotlib import pyplot as plt
# import seaborn as sns

def read_in_mags():
    ao_mag = Path("mag_csvs","ao_mag.csv")
    av_mag = Path("mag_csvs","av_mag.csv")
    ao_df = pd.read_csv(ao_mag, names = ["dyadno", "pptno", "dx", "dy", "dz"])
    av_df = pd.read_csv(av_mag, names = ["dyadno", "pptno", "dx", "dy", "dz"])
    return [ao_df, av_df]

# now create function that removes zeros

mag_list = read_in_mags()
ao_df = mag_list[0]
av_df = mag_list[1]
print(ao_df)
print(av_df)
