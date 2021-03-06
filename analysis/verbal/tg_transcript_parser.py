# tg_transcript_parser.py
# ryan pili 20191114
#
# program to read in the tg transcripts, and count backchannels and word counts

import pathlib 
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from loguru import logger as log
import re

# log.disable(log.DEBUG)

def transcript_parse():
    folder = pathlib.Path("transcripts") 
    files = folder.glob("*.txt")
    ao_list = []
    av_list = []
    dyad_ids = []
    for tc in files:
        dyadid = int(re.search(r"\d+", str(tc)).group())
        tc_string = tc.read_text()
        tc_string = tc_string.replace("\n", " ")
        tc_split = tc_string.split(" ")  
        words = [item for item in tc_split if ":" not in item]
        av_idx = words.index("[av]")
        ao_idx = words.index("[ao]")
        if av_idx > ao_idx:
            av_ao = False
            ao_av = True
        else: 
            av_ao = True
            ao_av = False
        # log.debug((av_ao, ao_av, "av_idx:", av_idx, "ao_idx", ao_idx))
        if av_ao is True:
            av_words = words[av_idx:ao_idx]
            ao_words = words[ao_idx:]
        elif ao_av is True: 
            av_words = words[av_idx:]
            ao_words = words[ao_idx:av_idx]
        # log.debug(("av_words", av_words, "ao_words", ao_words))
        av_words = [item for item in av_words if "[" not in item]
        av_words = [item for item in av_words if len(item) > 0]
        ao_words = [item for item in ao_words if "[" not in item]
        ao_words = [item for item in ao_words if len(item) > 0]
        ao_list.append(ao_words)
        av_list.append(av_words)
        dyad_ids.append(dyadid)
    return av_list, ao_list, dyad_ids


def bc_counter(words: list)->int:
    bcs = [bc for bc in words if "*" in bc]
    bc_count = len(bcs)
    return bc_count


def word_counter(av_list: list, ao_list: list):
    av_wc = [len(word_list) for word_list in av_list] 
    ao_wc = [len(word_list) for word_list in ao_list]
    return av_wc, ao_wc
 

def count_framer(ao_bcs: list, av_bcs: list, av_wc: list, ao_wc: list):
    counts_dict = {"av_bc":av_bcs, "ao_bc":ao_bcs, "av_wc":av_wc, "ao_wc":ao_wc}
    counts_df = pd.DataFrame.from_dict(counts_dict)
    return counts_df


# turn the .txt files in to list of lists of words
# each list in the list is from one dyad, len(list) = number of dyads
# with no [ ] or :
av_list, ao_list, dyad_ids = transcript_parse()

# log.debug(("av_list:", av_list, len(av_list)))
# log.debug(("ao_list:", ao_list, len(ao_list))) 

# for each list of words, go through it and check all the *
# return a list of backchannel counts for each dyad, for each condition
ao_bcs = [bc_counter(item) for item in ao_list]
av_bcs = [bc_counter(item) for item in av_list]

log.debug(("ao:", ao_bcs, "av", av_bcs))

# count all the words in each condition by feeding in the list of lists of words
# returns a list of counts
av_wc, ao_wc = word_counter(av_list, ao_list) 
print(f"av word counts are {av_wc}, and ao_wc counts are {ao_wc}")

# turn these counts into a pandas df so we can graph nicely
counts_df = count_framer(av_bcs=av_bcs, ao_bcs=ao_bcs, av_wc=av_wc, ao_wc=ao_wc)
counts_df["dyad_id"] = dyad_ids
counts_df = counts_df[["dyad_id", "av_bc", "ao_bc", "av_wc", "ao_wc"]]
counts_df["prop_ao_bc"] = counts 
graph_df = counts_df[["av_bc", "ao_bc", "av_wc", "ao_wc"]]

print(counts_df)

# counts_df = counts_df.reset_index()
# print(counts_df)
figure1 = sns.boxplot(data=graph_df[["av_bc", "ao_bc"]])
figure1.set(xlabel="Condition", ylabel="Backchannel Count", title="Verbal Backchannels per Condition")
plt.show()
figure1 = figure1.get_figure()
figure1.savefig("backchannel_figure.png")
figure2 = sns.boxplot(data=graph_df[["av_wc", "ao_wc"]])
figure2.set(xlabel="Condition", ylabel="Word Count", title="Word Count per Condition")
plt.show()
figure2 = figure2.get_figure()
figure2.savefig("wordcount_figure.png")

