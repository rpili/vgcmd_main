# tg_transcript_parser.py
# ryan pili 20191114
#
# program to read in the tg transcripts, and count backchannels and word counts

import pathlib 
import pandas as pd
from loguru import logger as log

# log.disable(log.DEBUG)

def transcript_parse():
    folder = pathlib.Path("transcripts") 
    files = folder.glob("*.txt")
    ao_list = []
    av_list = []
    for tc in files:
        tc_string = tc.read_text()
        tc_string = tc_string.replace("\n", " ")
        tc_split = tc_string.split(" ")  
        words = [item for item in tc_split if ":" not in item]
        av_idx = words.index("[av]")
        ao_idx = words.index("[ao]")
        if av_idx > ao_idx:
            av_ao = True
            ao_av = False
        else: 
            ao_av = False
            av_ao = True
        if av_ao is True:
            av_words = words[0:ao_idx]
            ao_words = words[ao_idx:]
        else: 
            av_words = words[av_idx:]
            ao_words = words[0:av_idx]
        av_words = [item for item in av_words if "[" not in item]
        av_words = [item for item in av_words if len(item) > 0]
        ao_words = [item for item in ao_words if "[" not in item]
        ao_words = [item for item in ao_words if len(item) > 0]
        ao_list.append(ao_words)
        av_list.append(av_words)
    return av_list, ao_list


def bc_counter(words: list)->int:
    bcs = [bc for bc in words if "*" in bc]
    bc_count = len(bcs)
    return bc_count


av_list, ao_list = transcript_parse()

ao_bcs = [bc_counter(item) for item in ao_list]
av_bcs = [bc_counter(item) for item in av_list]

log.debug((ao_bcs, av_bcs))

print("av word count is", len(av_list[0])) 
print("ao word count is", len(ao_list[0])) 




