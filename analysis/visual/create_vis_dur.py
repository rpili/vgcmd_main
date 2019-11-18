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

def dyads_to_vis_dur(dyads):
    vis_dur = dyads[["DYADNO","PPTNO","ONSET","DURATION","CONDITION","EVENT_TYPE"]]
    vis_dur.columns = [colname.lower() for colname in vis_dur.columns]
    return vis_dur

def vis_dur_mags_only(vis_dur):
    mags_only = vis_dur[vis_dur.event_type.str.contains("head")]
    return mags_only


# read in all the pointers
#   add dyadno into each pointer
# sort columns
# compute duration as a new column
# create a new dataframe
#   columns: dyadno, pptno, onset, duration, condition, event_type, role

dyads = read_in_pointers()
dyads = dyads_to_vis_dur(dyads)
print(dyads)
print(vis_dur_mags_only(dyads))
