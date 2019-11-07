# positioning.py
# ryan pili 20191102
# program to read in imagecoords.txt and output the range for the tangram being in that slot.
import pathlib
import collections
import textwrap
import re
import random 

def define_slot():
    infile = pathlib.Path("stimuli", "justcoords.txt")
    imagecoords = infile.read_text()
    found_coords = re.findall(r"(-?\d\.\d\d), (-?\d.\d\d)", imagecoords)
    ranges = []
    x_ranges = []
    y_ranges = [] 
    for coord in found_coords:
        x_pos = float(coord[0]) + .08
        x_neg = float(coord[0]) - .08
        y_pos = float(coord[1]) + .08
        y_neg = float(coord[1]) - .08
        x_range = (x_pos, x_neg) 
        y_range = (y_pos, y_neg)
        x_ranges.append(x_range)
        y_ranges.append(y_range)
    x_strings = [str(coord) for coord in x_ranges]
    y_strings = [str(coord) for coord in y_ranges]
    ranges = tuple(zip(x_strings, y_strings))
    ranges = dict(zip(found_coords, ranges))
    return ranges

'''
def slot_on_lines():
    range_line = [str(possible_range) + "\n" for possible_range in ranges]
    return range_line
'''

def randints(start, end, num): 
    randlist = []  
    num_range = end - start
    randlist = random.sample(range(num_range), num)
    return randlist


def write_slot(text_to_write: str):
    outfile = pathlib.Path("stimuli", "coords_with_ranges.txt")
    outfile.write_text(str(text_to_write))
    print("File Created.")

ranges = str(define_slot())
pattern = re.compile(r"(\))(,)( )")
new_ranges = pattern.sub(r"\1\n\3", ranges)
write_slot(new_ranges)

for number in range(13):
    if len(str(number)) is 1:
        number = "0" + str(number)
    print(f"gram{number}", end=",")

'''
trials = {}
for idx, trial in enumerate(range(3)): 
    trials[idx] = randints(1, 12, 12)
print(trials)
'''

randlist = random.sample(range(12), 12)
print(randlist, "randlist")

  
# Driver Code 
num = 10
start = 20
end = 40
print(randints(start, end, num)) 
