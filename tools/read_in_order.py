# read_in_order.py
# ryan pili 20191103
# reads in win order text file and assigns it to a variable (in this case, hitbox)

import pathlib
import collections
import textwrap
import re
import random 

def read_in_order():
    infile = pathlib.Path("flow","win_orders.txt")
    order = infile.read_text()
    orders = order.split(sep=",\n\n")
    return orders

hitboxes = read_in_order()
print(hitboxes[1])
print(all(hitboxes[2]))
print(all("yes"))