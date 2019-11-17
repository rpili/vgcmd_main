This is a set of psychopy based experiments based on Clark & Gibbs's tangram task.
tg_main_set1.py and tg_main_set2.py are to be presented to the matcher.
tg_dr_set1.py and tg_dr_set2.py are to be presented to the director. 
The experiment presents six tangram matching trials.
There are 2 sets of 12 tangrams. The "set1" and "set2" denote which set is presented first.
Between the two sets, a TIPI test is presented to determine impressions of the conversational partner.

20191105 - ryan pili
tg_main_set1.py, tg_main_set2.py are good to go
    just need to remove the easy_succ
tg_dr_set1.py is close
    need to update trial_6_answer so tangrams are in the win order
    then need to add instructions for the director
tg_dr_set2.py just need to move around the trials and copy/rename

20191105 - ryan pili
please don't commit your data files.

20191117 - ryan pili
for easy_succ, just make some variable called location
    then based on a flag you can 
        make the location off screen
        or have it in it's original spot
    