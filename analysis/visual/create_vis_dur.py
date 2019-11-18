# create_vis_dur.py
# 20191117 - ryan pili
# 
# program to read in all /visual_locationCSVs/dyad*_vis.csv
# computes the duration based on onset and offset
# adds in dyadno, pptno, condition, event_type based on the pointerCSV

from pathlib import Path
import loguru as log
import pandas as pd
import numpy as np
from pprint import pprint
import csv

def read_in_pointers():
    data_files = list(Path('visual_locationCSVs').glob('*.csv'))
    dyads = []
    for dyadno, dyad in enumerate(data_files):
        data = pd.read_csv(dyad, names=["CONDITION","ONSET","PPTNO","VISTYPE","EVENT_TYPE","OFFSET","ROLE"])
        data["DYADNO"] = dyadno + 1
        dyads.append(data)
    dyads = pd.concat(dyads)
    dyads["DURATION"] = dyads["OFFSET"] - dyads["ONSET"]
    return dyads

def dyads_to_vis_dur():


# read in all the pointers
#   add dyadno into each pointer
# sort columns
# compute duration as a new column
# create a new dataframe
#   columns: dyadno, pptno, onset, duration, condition, event_type, role

print(read_in_pointers())
