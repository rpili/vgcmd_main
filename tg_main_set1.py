#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on November 06, 2019, at 17:29
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

import pathlib
stim_folder = pathlib.Path("stimuli")



from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'tg_main_set1'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Ryan Pili\\OneDrive\\GS\\CECLAB\\vgcmd_main\\tg_main_set2.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Ask about the Window
def ask_about_window():
    experimenter_input = input("Where are you? booth_b, booth_c, or elsewhere? ")
    if experimenter_input  == "booth_b":
        window_size = [1050, 600]
        monitor_name = "vgcmd_booth_b"
    elif experimenter_input == "booth_c":
        window_size = [1050, 600]
        monitor_name = "vgcmd_booth_c"
    elif experimenter_input == "elsewhere" or "else":
        window_size = [1920, 1080]
        monitor_name = "ryan's windows acer"
    else:
        print("invalid response.")
        quit
    return window_size, monitor_name 

[window_size, monitor_name] = ask_about_window()

# Setup the window
win = visual.Window(
    size=window_size, fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor=monitor_name, color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instr1"
instr1Clock = core.Clock()
instruction_text = visual.TextStim(win=win, name='instruction_text',
    text="Instructions\n\nOn each trial you will see 12 shapes called tangrams. You will complete 6 trials.\n\nYour tangrams are in the incorrect order. \n\nYour partner's screen presents the Tangrams in the correct order. \n\nYou must work together to match your partner's correct tangram order.",
    font='Arial',
    pos=(0, 0.03), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Click here to continue.',
    font='Arial',
    pos=(0, -0.45), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "instr2"
instr2Clock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Here is a video example.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
mouse_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_2.mouseClock = core.Clock()

# Initialize components for Routine "trial"
trialClock = core.Clock()
one = visual.ImageStim(
    win=win,
    name='one', 
    image=str(stim_folder) + '\one.png', mask=None,
    ori=0, pos=(-.70, .30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
mouse_3 = event.Mouse(win=win)
x, y = [None, None]
mouse_3.mouseClock = core.Clock()
two = visual.ImageStim(
    win=win,
    name='two', 
    image=str(stim_folder)  + '/two.png', mask=None,
    ori=0, pos=(-.45, .30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
three = visual.ImageStim(
    win=win,
    name='three', 
    image=str(stim_folder) + '/three.png', mask=None,
    ori=0, pos=(-0.20, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
seven = visual.ImageStim(
    win=win,
    name='seven', 
    image=str(stim_folder) + '/seven.png', mask=None,
    ori=0, pos=(-0.70, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
eight = visual.ImageStim(
    win=win,
    name='eight', 
    image=str(stim_folder) + '/eight.png', mask=None,
    ori=0, pos=(-0.45, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
nine = visual.ImageStim(
    win=win,
    name='nine', 
    image=str(stim_folder) + '/nine.png', mask=None,
    ori=0, pos=(-0.20, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
four = visual.ImageStim(
    win=win,
    name='four', 
    image=str(stim_folder) + '/four.png', mask=None,
    ori=0, pos=(0.20, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
five = visual.ImageStim(
    win=win,
    name='five', 
    image=str(stim_folder) + '/five.png', mask=None,
    ori=0, pos=(0.45, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
six = visual.ImageStim(
    win=win,
    name='six', 
    image=str(stim_folder) + '/six.png', mask=None,
    ori=0, pos=(0.70, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)
ten = visual.ImageStim(
    win=win,
    name='ten', 
    image=str(stim_folder) + '/ten.png', mask=None,
    ori=0, pos=(0.20, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)
eleven = visual.ImageStim(
    win=win,
    name='eleven', 
    image=str(stim_folder) + '/eleven.png', mask=None,
    ori=0, pos=(0.45, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)
twelve = visual.ImageStim(
    win=win,
    name='twelve', 
    image=str(stim_folder) + '/twelve.png', mask=None,
    ori=0, pos=(0.70, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-12.0)


def movePicked(picked, mouse, grabbed):
    if grabbed is not None and mouse.isPressedIn(grabbed):
        grabbed.pos = mouse.getPos()
        return grabbed
    else:
        for piece in picked:
            if mouse.isPressedIn(piece) and grabbed is None:
                print(f"the piece is {piece.name} and position is {piece.pos}")
                return piece

def win_continue():
    continue_text = visual.TextStim(win=win, name='continue_text',
    text="Continue",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0)
    return continue_text
    
def trial_timer():
    trial_time = visual.TextStim(win=win, name='trial_time',
    text=f"Completed in {int(t)} seconds!",
    font='Arial',
    pos=(0.4, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0)
    return trial_time

# failing because continue_text wasn't defined, but is listed as valid click
# offscreen_continue() creates an unclickable, offscreen object named continue_text
# continue_text is then updated and drawn when win_state = True 
def offscreen_continue():
    continue_text = visual.TextStim(win=win, name='continue_text',
    text="Continue",
    font='Arial',
    pos=(1.5, 1.5), height=0.001, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=0,
    languageStyle='LTR',
    depth=0.0)
    return continue_text

continue_text = offscreen_continue()

# create function to call on each frame, that will out the 
# x and y position of an image as tuple
# call this over each tangram



# then create a function that will test each tangra
# and once they're all in the right place, at the same time
# will return True

def hitbox_checker(box: str, tangram)->bool: 
    xpos = tangram.pos[0] 
    ypos = tangram.pos[1]
    x_upbound = hitbox_dict[box][0][0]
    x_downbound = hitbox_dict[box][0][1]
    y_upbound = hitbox_dict[box][1][0]
    y_downbound = hitbox_dict[box][1][1]
    if x_upbound > xpos > x_downbound and y_upbound >  ypos > y_downbound:
        return True

hitbox_dict = {('one'): ((-0.62, -0.7799999999999999), (0.38, 0.21999999999999997)),
 ('two'): ((-0.37, -0.53), (0.38, 0.21999999999999997)),
 ('three'): ((-0.12000000000000001, -0.28), (0.38, 0.21999999999999997)),
 ('four'): ((0.28, 0.12000000000000001), (0.38, 0.21999999999999997)),
 ('five'): ((0.53, 0.37), (0.38, 0.21999999999999997)),
 ('six'): ((0.7799999999999999, 0.62), (0.38, 0.21999999999999997)),
 ('seven'): ((-0.62, -0.7799999999999999), (-0.21999999999999997, -0.38)),
 ('eight'): ((-0.37, -0.53), (-0.21999999999999997, -0.38)),
 ('nine'): ((-0.12000000000000001, -0.28), (-0.21999999999999997, -0.38)),
 ('ten'): ((0.28, 0.12000000000000001), (-0.21999999999999997, -0.38)),
 ('eleven'): ((0.53, 0.37), (-0.21999999999999997, -0.38)),
 ('twelve'): ((0.7799999999999999, 0.62), (-0.21999999999999997, -0.38))}
gram01 = visual.ImageStim(
    win=win,
    name='gram01', 
    image=str(stim_folder) + '/tangrams/gram01.png', mask=None,
    ori=0, pos=(-.70, -.3), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-14.0)
gram02 = visual.ImageStim(
    win=win,
    name='gram02', 
    image=str(stim_folder) + '/tangrams/gram02.png', mask=None,
    ori=0, pos=(-.70, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-15.0)
gram03 = visual.ImageStim(
    win=win,
    name='gram03', 
    image=str(stim_folder) + '/tangrams/gram03.png', mask=None,
    ori=0, pos=(-0.45, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-16.0)
gram04 = visual.ImageStim(
    win=win,
    name='gram04', 
    image=str(stim_folder) + '/tangrams/gram04.png', mask=None,
    ori=0, pos=(-0.45, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-17.0)
gram05 = visual.ImageStim(
    win=win,
    name='gram05', 
    image=str(stim_folder) + '/tangrams/gram05.png', mask=None,
    ori=0, pos=(0.20, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-18.0)
gram06 = visual.ImageStim(
    win=win,
    name='gram06', 
    image=str(stim_folder) + '/tangrams/gram06.png', mask=None,
    ori=0, pos=(0.70, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-19.0)
gram07 = visual.ImageStim(
    win=win,
    name='gram07', 
    image=str(stim_folder) + '/tangrams/gram07.png', mask=None,
    ori=0, pos=(0.45, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-20.0)
gram08 = visual.ImageStim(
    win=win,
    name='gram08', 
    image=str(stim_folder) + '/tangrams/gram08.png', mask=None,
    ori=0, pos=(0.45, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-21.0)
gram09 = visual.ImageStim(
    win=win,
    name='gram09', 
    image=str(stim_folder) + '/tangrams/gram09.png', mask=None,
    ori=0, pos=(-0.20, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-22.0)
gram10 = visual.ImageStim(
    win=win,
    name='gram10', 
    image=str(stim_folder) + '/tangrams/gram10.png', mask=None,
    ori=0, pos=(-0.20, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-23.0)
gram11 = visual.ImageStim(
    win=win,
    name='gram11', 
    image=str(stim_folder) + '/tangrams/gram11.png', mask=None,
    ori=0, pos=(0.70, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-24.0)
gram12 = visual.ImageStim(
    win=win,
    name='gram12', 
    image=str(stim_folder) + '/tangrams/gram12.png', mask=None,
    ori=0, pos=(0.20, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-25.0)
easy_succ = visual.TextStim(win=win, name='easy_succ',
    text='Move On',
    font='Arial',
    pos=(-.30, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-26.0);

# Initialize components for Routine "trial_2"
trial_2Clock = core.Clock()
one_2 = visual.ImageStim(
    win=win,
    name='one_2', 
    image=str(stim_folder) + '/one.png', mask=None,
    ori=0, pos=(-.70, .30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
mouse_4 = event.Mouse(win=win)
x, y = [None, None]
mouse_4.mouseClock = core.Clock()
two_2 = visual.ImageStim(
    win=win,
    name='two_2', 
    image=str(stim_folder) + '/two.png', mask=None,
    ori=0, pos=(-.45, .30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
three_2 = visual.ImageStim(
    win=win,
    name='three_2', 
    image=str(stim_folder) + '/three.png', mask=None,
    ori=0, pos=(-0.20, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
seven_2 = visual.ImageStim(
    win=win,
    name='seven_2', 
    image=str(stim_folder) + '/seven.png', mask=None,
    ori=0, pos=(-0.70, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
eight_2 = visual.ImageStim(
    win=win,
    name='eight_2', 
    image=str(stim_folder) + '/eight.png', mask=None,
    ori=0, pos=(-0.45, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
nine_2 = visual.ImageStim(
    win=win,
    name='nine_2', 
    image=str(stim_folder) + '/nine.png', mask=None,
    ori=0, pos=(-0.20, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
four_2 = visual.ImageStim(
    win=win,
    name='four_2', 
    image=str(stim_folder) + '/four.png', mask=None,
    ori=0, pos=(0.20, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
five_2 = visual.ImageStim(
    win=win,
    name='five_2', 
    image=str(stim_folder) + '/five.png', mask=None,
    ori=0, pos=(0.45, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
six_2 = visual.ImageStim(
    win=win,
    name='six_2', 
    image=str(stim_folder) + '/six.png', mask=None,
    ori=0, pos=(0.70, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)
ten_2 = visual.ImageStim(
    win=win,
    name='ten_2', 
    image=str(stim_folder) + '/ten.png', mask=None,
    ori=0, pos=(0.20, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)
eleven_2 = visual.ImageStim(
    win=win,
    name='eleven_2', 
    image=str(stim_folder) + '/eleven.png', mask=None,
    ori=0, pos=(0.45, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)
twelve_2 = visual.ImageStim(
    win=win,
    name='twelve_2', 
    image=str(stim_folder) + '/twelve.png', mask=None,
    ori=0, pos=(0.70, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-12.0)


def movePicked(picked, mouse, grabbed):
    if grabbed is not None and mouse.isPressedIn(grabbed):
        grabbed.pos = mouse.getPos()
        return grabbed
    else:
        for piece in picked:
            if mouse.isPressedIn(piece) and grabbed is None:
                print(f"the piece is {piece.name} and position is {piece.pos}")
                return piece

def win_continue():
    continue_text = visual.TextStim(win=win, name='continue_text',
    text="Continue",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0)
    return continue_text

# failing because continue_text wasn't defined, but is listed as valid click
# offscreen_continue() creates an unclickable, offscreen object named continue_text
# continue_text is then updated and drawn when win_state = True 
def offscreen_continue():
    continue_text = visual.TextStim(win=win, name='continue_text',
    text="Continue",
    font='Arial',
    pos=(1.5, 1.5), height=0.001, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=0,
    languageStyle='LTR',
    depth=0.0)
    return continue_text

continue_text = offscreen_continue()

# create function to call on each frame, that will out the 
# x and y position of an image as tuple
# call this over each tangram



# then create a function that will test each tangra
# and once they're all in the right place, at the same time
# will return True

def hitbox_checker(box: str, tangram)->bool: 
    xpos = tangram.pos[0] 
    ypos = tangram.pos[1]
    x_upbound = hitbox_dict[box][0][0]
    x_downbound = hitbox_dict[box][0][1]
    y_upbound = hitbox_dict[box][1][0]
    y_downbound = hitbox_dict[box][1][1]
    if x_upbound > xpos > x_downbound and y_upbound >  ypos > y_downbound:
        return True

hitbox_dict = {('one'): ((-0.62, -0.7799999999999999), (0.38, 0.21999999999999997)),
 ('two'): ((-0.37, -0.53), (0.38, 0.21999999999999997)),
 ('three'): ((-0.12000000000000001, -0.28), (0.38, 0.21999999999999997)),
 ('four'): ((0.28, 0.12000000000000001), (0.38, 0.21999999999999997)),
 ('five'): ((0.53, 0.37), (0.38, 0.21999999999999997)),
 ('six'): ((0.7799999999999999, 0.62), (0.38, 0.21999999999999997)),
 ('seven'): ((-0.62, -0.7799999999999999), (-0.21999999999999997, -0.38)),
 ('eight'): ((-0.37, -0.53), (-0.21999999999999997, -0.38)),
 ('nine'): ((-0.12000000000000001, -0.28), (-0.21999999999999997, -0.38)),
 ('ten'): ((0.28, 0.12000000000000001), (-0.21999999999999997, -0.38)),
 ('eleven'): ((0.53, 0.37), (-0.21999999999999997, -0.38)),
 ('twelve'): ((0.7799999999999999, 0.62), (-0.21999999999999997, -0.38))}
gram01_2 = visual.ImageStim(
    win=win,
    name='gram01_2', 
    image=str(stim_folder) + '/tangrams/gram01.png', mask=None,
    ori=0, pos=(0.20, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-14.0)
gram02_2 = visual.ImageStim(
    win=win,
    name='gram02_2', 
    image=str(stim_folder) + '/tangrams/gram02.png', mask=None,
    ori=0, pos=(-0.70, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-15.0)
gram03_2 = visual.ImageStim(
    win=win,
    name='gram03_2', 
    image=str(stim_folder) + '/tangrams/gram03.png', mask=None,
    ori=0, pos=(-0.20, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-16.0)
gram04_2 = visual.ImageStim(
    win=win,
    name='gram04_2', 
    image=str(stim_folder) + '/tangrams/gram04.png', mask=None,
    ori=0, pos=(0.20, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-17.0)
gram05_2 = visual.ImageStim(
    win=win,
    name='gram05_2', 
    image=str(stim_folder) + '/tangrams/gram05.png', mask=None,
    ori=0, pos=(-0.70, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-18.0)
gram06_2 = visual.ImageStim(
    win=win,
    name='gram06_2', 
    image=str(stim_folder) + '/tangrams/gram06.png', mask=None,
    ori=0, pos=(0.45, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-19.0)
gram07_2 = visual.ImageStim(
    win=win,
    name='gram07_2', 
    image=str(stim_folder) + '/tangrams/gram07.png', mask=None,
    ori=0, pos=(0.70, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-20.0)
gram08_2 = visual.ImageStim(
    win=win,
    name='gram08_2', 
    image=str(stim_folder) + '/tangrams/gram08.png', mask=None,
    ori=0, pos=(-0.20, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-21.0)
gram09_2 = visual.ImageStim(
    win=win,
    name='gram09_2', 
    image=str(stim_folder) + '/tangrams/gram09.png', mask=None,
    ori=0, pos=(0.70, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-22.0)
gram10_2 = visual.ImageStim(
    win=win,
    name='gram10_2', 
    image=str(stim_folder) + '/tangrams/gram10.png', mask=None,
    ori=0, pos=(0.45, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-23.0)
gram11_2 = visual.ImageStim(
    win=win,
    name='gram11_2', 
    image=str(stim_folder) + '/tangrams/gram11.png', mask=None,
    ori=0, pos=(-0.45, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-24.0)
gram12_2 = visual.ImageStim(
    win=win,
    name='gram12_2', 
    image=str(stim_folder) + '/tangrams/gram12.png', mask=None,
    ori=0, pos=(-0.45, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-25.0)
easy_succ_2 = visual.TextStim(win=win, name='easy_succ_2',
    text='Move On',
    font='Arial',
    pos=(-.30, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-26.0);

# Initialize components for Routine "trial_3"
trial_3Clock = core.Clock()
one_3 = visual.ImageStim(
    win=win,
    name='one_3', 
    image=str(stim_folder) + '/one.png', mask=None,
    ori=0, pos=(-.70, .30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
mouse_5 = event.Mouse(win=win)
x, y = [None, None]
mouse_5.mouseClock = core.Clock()
two_3 = visual.ImageStim(
    win=win,
    name='two_3', 
    image=str(stim_folder) + '/two.png', mask=None,
    ori=0, pos=(-.45, .30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
three_3 = visual.ImageStim(
    win=win,
    name='three_3', 
    image=str(stim_folder) + '/three.png', mask=None,
    ori=0, pos=(-0.20, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
seven_3 = visual.ImageStim(
    win=win,
    name='seven_3', 
    image=str(stim_folder) + '/seven.png', mask=None,
    ori=0, pos=(-0.70, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
eight_3 = visual.ImageStim(
    win=win,
    name='eight_3', 
    image=str(stim_folder) + '/eight.png', mask=None,
    ori=0, pos=(-0.45, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
nine_3 = visual.ImageStim(
    win=win,
    name='nine_3', 
    image=str(stim_folder) + '/nine.png', mask=None,
    ori=0, pos=(-0.20, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
four_3 = visual.ImageStim(
    win=win,
    name='four_3', 
    image=str(stim_folder) + '/four.png', mask=None,
    ori=0, pos=(0.20, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
five_3 = visual.ImageStim(
    win=win,
    name='five_3', 
    image=str(stim_folder) + '/five.png', mask=None,
    ori=0, pos=(0.45, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
six_3 = visual.ImageStim(
    win=win,
    name='six_3', 
    image=str(stim_folder) + '/six.png', mask=None,
    ori=0, pos=(0.70, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)
ten_3 = visual.ImageStim(
    win=win,
    name='ten_3', 
    image=str(stim_folder) + '/ten.png', mask=None,
    ori=0, pos=(0.20, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)
eleven_3 = visual.ImageStim(
    win=win,
    name='eleven_3', 
    image=str(stim_folder) + '/eleven.png', mask=None,
    ori=0, pos=(0.45, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)
twelve_3 = visual.ImageStim(
    win=win,
    name='twelve_3', 
    image=str(stim_folder) + '/twelve.png', mask=None,
    ori=0, pos=(0.70, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-12.0)


def movePicked(picked, mouse, grabbed):
    if grabbed is not None and mouse.isPressedIn(grabbed):
        grabbed.pos = mouse.getPos()
        return grabbed
    else:
        for piece in picked:
            if mouse.isPressedIn(piece) and grabbed is None:
                print(f"the piece is {piece.name} and position is {piece.pos}")
                return piece

# create continue text to be presented when tangrams correctly arranged
def win_continue():
    continue_text = visual.TextStim(win=win, name='continue_text',
    text="Continue",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0)
    return continue_text

# failing because continue_text wasn't defined, but is listed as valid click
# offscreen_continue() creates an unclickable, offscreen object named continue_text
# continue_text is then updated and drawn when win_state = True 
def offscreen_continue():
    continue_text = visual.TextStim(win=win, name='continue_text',
    text="Continue",
    font='Arial',
    pos=(1.5, 1.5), height=0.001, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=0,
    languageStyle='LTR',
    depth=0.0)
    return continue_text

continue_text = offscreen_continue()

# create function to call on each frame, that will out the 
# x and y position of an image as tuple
# call this over each tangram



# then create a function that will test each tangra
# and once they're all in the right place, at the same time
# will return True

def hitbox_checker(box: str, tangram)->bool: 
    xpos = tangram.pos[0] 
    ypos = tangram.pos[1]
    x_upbound = hitbox_dict[box][0][0]
    x_downbound = hitbox_dict[box][0][1]
    y_upbound = hitbox_dict[box][1][0]
    y_downbound = hitbox_dict[box][1][1]
    if x_upbound > xpos > x_downbound and y_upbound >  ypos > y_downbound:
        return True

hitbox_dict = {('one'): ((-0.62, -0.7799999999999999), (0.38, 0.21999999999999997)),
 ('two'): ((-0.37, -0.53), (0.38, 0.21999999999999997)),
 ('three'): ((-0.12000000000000001, -0.28), (0.38, 0.21999999999999997)),
 ('four'): ((0.28, 0.12000000000000001), (0.38, 0.21999999999999997)),
 ('five'): ((0.53, 0.37), (0.38, 0.21999999999999997)),
 ('six'): ((0.7799999999999999, 0.62), (0.38, 0.21999999999999997)),
 ('seven'): ((-0.62, -0.7799999999999999), (-0.21999999999999997, -0.38)),
 ('eight'): ((-0.37, -0.53), (-0.21999999999999997, -0.38)),
 ('nine'): ((-0.12000000000000001, -0.28), (-0.21999999999999997, -0.38)),
 ('ten'): ((0.28, 0.12000000000000001), (-0.21999999999999997, -0.38)),
 ('eleven'): ((0.53, 0.37), (-0.21999999999999997, -0.38)),
 ('twelve'): ((0.7799999999999999, 0.62), (-0.21999999999999997, -0.38))}
gram01_3 = visual.ImageStim(
    win=win,
    name='gram01_3', 
    image=str(stim_folder) + '/tangrams/gram01.png', mask=None,
    ori=0, pos=(0.20, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-14.0)
gram02_3 = visual.ImageStim(
    win=win,
    name='gram02_3', 
    image=str(stim_folder) + '/tangrams/gram02.png', mask=None,
    ori=0, pos=(-0.20, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-15.0)
gram03_3 = visual.ImageStim(
    win=win,
    name='gram03_3', 
    image=str(stim_folder) + '/tangrams/gram03.png', mask=None,
    ori=0, pos=(-0.70, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-16.0)
gram04_3 = visual.ImageStim(
    win=win,
    name='gram04_3', 
    image=str(stim_folder) + '/tangrams/gram04.png', mask=None,
    ori=0, pos=(-0.45, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-17.0)
gram05_3 = visual.ImageStim(
    win=win,
    name='gram05_3', 
    image=str(stim_folder) + '/tangrams/gram05.png', mask=None,
    ori=0, pos=(0.45, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-18.0)
gram06_3 = visual.ImageStim(
    win=win,
    name='gram06_3', 
    image=str(stim_folder) + '/tangrams/gram06.png', mask=None,
    ori=0, pos=(0.20, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-19.0)
gram07_3 = visual.ImageStim(
    win=win,
    name='gram07_3', 
    image=str(stim_folder) + '/tangrams/gram07.png', mask=None,
    ori=0, pos=(0.70, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-20.0)
gram08_3 = visual.ImageStim(
    win=win,
    name='gram08_3', 
    image=str(stim_folder) + '/tangrams/gram08.png', mask=None,
    ori=0, pos=(0.45, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-21.0)
gram09_3 = visual.ImageStim(
    win=win,
    name='gram09_3', 
    image=str(stim_folder) + '/tangrams/gram09.png', mask=None,
    ori=0, pos=(-0.20, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-22.0)
gram10_3 = visual.ImageStim(
    win=win,
    name='gram10_3', 
    image=str(stim_folder) + '/tangrams/gram10.png', mask=None,
    ori=0, pos=(0.70, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-23.0)
gram11_3 = visual.ImageStim(
    win=win,
    name='gram11_3', 
    image=str(stim_folder) + '/tangrams/gram11.png', mask=None,
    ori=0, pos=(-0.70, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-24.0)
gram12_3 = visual.ImageStim(
    win=win,
    name='gram12_3', 
    image=str(stim_folder) + '/tangrams/gram12.png', mask=None,
    ori=0, pos=(-0.45, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-25.0)
easy_succ_3 = visual.TextStim(win=win, name='easy_succ_3',
    text='Move On',
    font='Arial',
    pos=(-.30, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-26.0);

# Initialize components for Routine "call_exp1"
call_exp1Clock = core.Clock()
call_exp_text = visual.TextStim(win=win, name='call_exp_text',
    text='Call experimenter to continue!\n\nPlease yell "We\'re done!" ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "TIPI_instr"
TIPI_instrClock = core.Clock()
TIPI_txt = visual.TextStim(win=win, name='TIPI_txt',
    text='On the following page you will describe your partner\'s personality.\n\n-You will see a number of statements about personality traits which may or may not apply to them. \n-Please click the number next to the statement to indicate the extent to which you agree or disagree with that statement. \n-You should rate the extent to which the wording applies to your partner, even if one characteristic applies more strongly than the other.\n\n1 is a rating of "Disagree Strongly"\n7 is a rating of "Agree Strongly"',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "TIPI"
TIPIClock = core.Clock()
win.allowStencil = True
tipi_form = visual.Form(win=win, name='tipi_form',
    items=str(stim_folder) + '/tipi_format.csv',
    textHeight=0.03,
    randomize=False,
    size=(1, 0.7),
    pos=(0, 0),
    itemPadding=0.05)
tipi_scale = visual.ImageStim(
    win=win,
    name='tipi_scale', 
    image=str(stim_folder) + '/tipi_scale.png', mask=None,
    ori=0, pos=(0, 0.43), size=(0.7, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "trial_4"
trial_4Clock = core.Clock()
one_4 = visual.ImageStim(
    win=win,
    name='one_4', 
    image=str(stim_folder) + '/one.png', mask=None,
    ori=0, pos=(-.70, .30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
mouse_6 = event.Mouse(win=win)
x, y = [None, None]
mouse_6.mouseClock = core.Clock()
two_4 = visual.ImageStim(
    win=win,
    name='two_4', 
    image=str(stim_folder) + '/two.png', mask=None,
    ori=0, pos=(-.45, .30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
three_4 = visual.ImageStim(
    win=win,
    name='three_4', 
    image=str(stim_folder) + '/three.png', mask=None,
    ori=0, pos=(-0.20, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
seven_4 = visual.ImageStim(
    win=win,
    name='seven_4', 
    image=str(stim_folder) + '/seven.png', mask=None,
    ori=0, pos=(-0.70, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
eight_4 = visual.ImageStim(
    win=win,
    name='eight_4', 
    image=str(stim_folder) + '/eight.png', mask=None,
    ori=0, pos=(-0.45, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
nine_4 = visual.ImageStim(
    win=win,
    name='nine_4', 
    image=str(stim_folder) + '/nine.png', mask=None,
    ori=0, pos=(-0.20, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
four_4 = visual.ImageStim(
    win=win,
    name='four_4', 
    image=str(stim_folder) + '/four.png', mask=None,
    ori=0, pos=(0.20, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
five_4 = visual.ImageStim(
    win=win,
    name='five_4', 
    image=str(stim_folder) + '/five.png', mask=None,
    ori=0, pos=(0.45, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
six_4 = visual.ImageStim(
    win=win,
    name='six_4', 
    image=str(stim_folder) + '/six.png', mask=None,
    ori=0, pos=(0.70, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)
ten_4 = visual.ImageStim(
    win=win,
    name='ten_4', 
    image=str(stim_folder) + '/ten.png', mask=None,
    ori=0, pos=(0.20, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)
eleven_4 = visual.ImageStim(
    win=win,
    name='eleven_4', 
    image=str(stim_folder) + '/eleven.png', mask=None,
    ori=0, pos=(0.45, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)
twelve_4 = visual.ImageStim(
    win=win,
    name='twelve_4', 
    image=str(stim_folder) + '/twelve.png', mask=None,
    ori=0, pos=(0.70, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-12.0)


def movePicked(picked, mouse, grabbed):
    if grabbed is not None and mouse.isPressedIn(grabbed):
        grabbed.pos = mouse.getPos()
        return grabbed
    else:
        for piece in picked:
            if mouse.isPressedIn(piece) and grabbed is None:
                print(f"the piece is {piece.name} and position is {piece.pos}")
                return piece

def win_continue():
    continue_text = visual.TextStim(win=win, name='continue_text',
    text="Continue",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0)
    return continue_text
    
def trial_timer():
    trial_time = visual.TextStim(win=win, name='trial_time',
    text=f"Completed in {int(t)} seconds!",
    font='Arial',
    pos=(0.4, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0)
    return trial_time

# failing because continue_text wasn't defined, but is listed as valid click
# offscreen_continue() creates an unclickable, offscreen object named continue_text
# continue_text is then updated and drawn when win_state = True 
def offscreen_continue():
    continue_text = visual.TextStim(win=win, name='continue_text',
    text="Continue",
    font='Arial',
    pos=(1.5, 1.5), height=0.001, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=0,
    languageStyle='LTR',
    depth=0.0)
    return continue_text

continue_text = offscreen_continue()

# create function to call on each frame, that will out the 
# x and y position of an image as tuple
# call this over each tangram



# then create a function that will test each tangra
# and once they're all in the right place, at the same time
# will return True

def hitbox_checker(box: str, tangram)->bool: 
    xpos = tangram.pos[0] 
    ypos = tangram.pos[1]
    x_upbound = hitbox_dict[box][0][0]
    x_downbound = hitbox_dict[box][0][1]
    y_upbound = hitbox_dict[box][1][0]
    y_downbound = hitbox_dict[box][1][1]
    if x_upbound > xpos > x_downbound and y_upbound >  ypos > y_downbound:
        return True

hitbox_dict = {('one'): ((-0.62, -0.7799999999999999), (0.38, 0.21999999999999997)),
 ('two'): ((-0.37, -0.53), (0.38, 0.21999999999999997)),
 ('three'): ((-0.12000000000000001, -0.28), (0.38, 0.21999999999999997)),
 ('four'): ((0.28, 0.12000000000000001), (0.38, 0.21999999999999997)),
 ('five'): ((0.53, 0.37), (0.38, 0.21999999999999997)),
 ('six'): ((0.7799999999999999, 0.62), (0.38, 0.21999999999999997)),
 ('seven'): ((-0.62, -0.7799999999999999), (-0.21999999999999997, -0.38)),
 ('eight'): ((-0.37, -0.53), (-0.21999999999999997, -0.38)),
 ('nine'): ((-0.12000000000000001, -0.28), (-0.21999999999999997, -0.38)),
 ('ten'): ((0.28, 0.12000000000000001), (-0.21999999999999997, -0.38)),
 ('eleven'): ((0.53, 0.37), (-0.21999999999999997, -0.38)),
 ('twelve'): ((0.7799999999999999, 0.62), (-0.21999999999999997, -0.38))}
gram13_4 = visual.ImageStim(
    win=win,
    name='gram13_4', 
    image=str(stim_folder) + '/tangrams/gram13.png', mask=None,
    ori=0, pos=(0.70, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-14.0)
gram14_4 = visual.ImageStim(
    win=win,
    name='gram14_4', 
    image=str(stim_folder) + '/tangrams/gram14.png', mask=None,
    ori=0, pos=(-0.20, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-15.0)
gram15_4 = visual.ImageStim(
    win=win,
    name='gram15_4', 
    image=str(stim_folder) + '/tangrams/gram15.png', mask=None,
    ori=0, pos=(0.45, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-16.0)
gram16_4 = visual.ImageStim(
    win=win,
    name='gram16_4', 
    image=str(stim_folder) + '/tangrams/gram16.png', mask=None,
    ori=0, pos=(-0.20, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-17.0)
gram17_4 = visual.ImageStim(
    win=win,
    name='gram17_4', 
    image=str(stim_folder) + '/tangrams/gram17.png', mask=None,
    ori=0, pos=(-0.45, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-18.0)
gram18_4 = visual.ImageStim(
    win=win,
    name='gram18_4', 
    image=str(stim_folder) + '/tangrams/gram18.png', mask=None,
    ori=0, pos=(0.45, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-19.0)
gram19_4 = visual.ImageStim(
    win=win,
    name='gram19_4', 
    image=str(stim_folder) + '/tangrams/gram19.png', mask=None,
    ori=0, pos=(-0.70, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-20.0)
gram20_4 = visual.ImageStim(
    win=win,
    name='gram20_4', 
    image=str(stim_folder) + '/tangrams/gram20.png', mask=None,
    ori=0, pos=(0.70, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-21.0)
gram21_4 = visual.ImageStim(
    win=win,
    name='gram21_4', 
    image=str(stim_folder) + '/tangrams/gram21.png', mask=None,
    ori=0, pos=(0.20, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-22.0)
gram22_4 = visual.ImageStim(
    win=win,
    name='gram22_4', 
    image=str(stim_folder) + '/tangrams/gram22.png', mask=None,
    ori=0, pos=(0.20, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-23.0)
gram23_4 = visual.ImageStim(
    win=win,
    name='gram23_4', 
    image=str(stim_folder) + '/tangrams/gram23.png', mask=None,
    ori=0, pos=(-0.70, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-24.0)
gram24_4 = visual.ImageStim(
    win=win,
    name='gram24_4', 
    image=str(stim_folder) + '/tangrams/gram24.png', mask=None,
    ori=0, pos=(-0.45, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-25.0)
easy_succ_4 = visual.TextStim(win=win, name='easy_succ_4',
    text='Move On',
    font='Arial',
    pos=(-.30, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-26.0);

# Initialize components for Routine "trial_5"
trial_5Clock = core.Clock()
one_5 = visual.ImageStim(
    win=win,
    name='one_5', 
    image=str(stim_folder) + '/one.png', mask=None,
    ori=0, pos=(-.70, .30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
mouse_7 = event.Mouse(win=win)
x, y = [None, None]
mouse_7.mouseClock = core.Clock()
two_5 = visual.ImageStim(
    win=win,
    name='two_5', 
    image=str(stim_folder) + '/two.png', mask=None,
    ori=0, pos=(-.45, .30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
three_5 = visual.ImageStim(
    win=win,
    name='three_5', 
    image=str(stim_folder) + '/three.png', mask=None,
    ori=0, pos=(-0.20, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
seven_5 = visual.ImageStim(
    win=win,
    name='seven_5', 
    image=str(stim_folder) + '/seven.png', mask=None,
    ori=0, pos=(-0.70, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
eight_5 = visual.ImageStim(
    win=win,
    name='eight_5', 
    image=str(stim_folder) + '/eight.png', mask=None,
    ori=0, pos=(-0.45, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
nine_5 = visual.ImageStim(
    win=win,
    name='nine_5', 
    image=str(stim_folder) + '/nine.png', mask=None,
    ori=0, pos=(-0.20, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
four_5 = visual.ImageStim(
    win=win,
    name='four_5', 
    image=str(stim_folder) + '/four.png', mask=None,
    ori=0, pos=(0.20, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
five_5 = visual.ImageStim(
    win=win,
    name='five_5', 
    image=str(stim_folder) + '/five.png', mask=None,
    ori=0, pos=(0.45, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
six_5 = visual.ImageStim(
    win=win,
    name='six_5', 
    image=str(stim_folder) + '/six.png', mask=None,
    ori=0, pos=(0.70, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)
ten_5 = visual.ImageStim(
    win=win,
    name='ten_5', 
    image=str(stim_folder) + '/ten.png', mask=None,
    ori=0, pos=(0.20, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)
eleven_5 = visual.ImageStim(
    win=win,
    name='eleven_5', 
    image=str(stim_folder) + '/eleven.png', mask=None,
    ori=0, pos=(0.45, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)
twelve_5 = visual.ImageStim(
    win=win,
    name='twelve_5', 
    image=str(stim_folder) + '/twelve.png', mask=None,
    ori=0, pos=(0.70, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-12.0)


def movePicked(picked, mouse, grabbed):
    if grabbed is not None and mouse.isPressedIn(grabbed):
        grabbed.pos = mouse.getPos()
        return grabbed
    else:
        for piece in picked:
            if mouse.isPressedIn(piece) and grabbed is None:
                print(f"the piece is {piece.name} and position is {piece.pos}")
                return piece

def win_continue():
    continue_text = visual.TextStim(win=win, name='continue_text',
    text="Continue",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0)
    return continue_text
    
def trial_timer():
    trial_time = visual.TextStim(win=win, name='trial_time',
    text=f"Completed in {int(t)} seconds!",
    font='Arial',
    pos=(0.4, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0)
    return trial_time

# failing because continue_text wasn't defined, but is listed as valid click
# offscreen_continue() creates an unclickable, offscreen object named continue_text
# continue_text is then updated and drawn when win_state = True 
def offscreen_continue():
    continue_text = visual.TextStim(win=win, name='continue_text',
    text="Continue",
    font='Arial',
    pos=(1.5, 1.5), height=0.001, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=0,
    languageStyle='LTR',
    depth=0.0)
    return continue_text

continue_text = offscreen_continue()

# create function to call on each frame, that will out the 
# x and y position of an image as tuple
# call this over each tangram



# then create a function that will test each tangra
# and once they're all in the right place, at the same time
# will return True

def hitbox_checker(box: str, tangram)->bool: 
    xpos = tangram.pos[0] 
    ypos = tangram.pos[1]
    x_upbound = hitbox_dict[box][0][0]
    x_downbound = hitbox_dict[box][0][1]
    y_upbound = hitbox_dict[box][1][0]
    y_downbound = hitbox_dict[box][1][1]
    if x_upbound > xpos > x_downbound and y_upbound >  ypos > y_downbound:
        return True

hitbox_dict = {('one'): ((-0.62, -0.7799999999999999), (0.38, 0.21999999999999997)),
 ('two'): ((-0.37, -0.53), (0.38, 0.21999999999999997)),
 ('three'): ((-0.12000000000000001, -0.28), (0.38, 0.21999999999999997)),
 ('four'): ((0.28, 0.12000000000000001), (0.38, 0.21999999999999997)),
 ('five'): ((0.53, 0.37), (0.38, 0.21999999999999997)),
 ('six'): ((0.7799999999999999, 0.62), (0.38, 0.21999999999999997)),
 ('seven'): ((-0.62, -0.7799999999999999), (-0.21999999999999997, -0.38)),
 ('eight'): ((-0.37, -0.53), (-0.21999999999999997, -0.38)),
 ('nine'): ((-0.12000000000000001, -0.28), (-0.21999999999999997, -0.38)),
 ('ten'): ((0.28, 0.12000000000000001), (-0.21999999999999997, -0.38)),
 ('eleven'): ((0.53, 0.37), (-0.21999999999999997, -0.38)),
 ('twelve'): ((0.7799999999999999, 0.62), (-0.21999999999999997, -0.38))}
gram13_5 = visual.ImageStim(
    win=win,
    name='gram13_5', 
    image=str(stim_folder) + '/tangrams/gram13.png', mask=None,
    ori=0, pos=(-0.70, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-14.0)
gram14_5 = visual.ImageStim(
    win=win,
    name='gram14_5', 
    image=str(stim_folder) + '/tangrams/gram14.png', mask=None,
    ori=0, pos=(-0.20, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-15.0)
gram15_5 = visual.ImageStim(
    win=win,
    name='gram15_5', 
    image=str(stim_folder) + '/tangrams/gram15.png', mask=None,
    ori=0, pos=(-0.45, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-16.0)
gram16_5 = visual.ImageStim(
    win=win,
    name='gram16_5', 
    image=str(stim_folder) + '/tangrams/gram16.png', mask=None,
    ori=0, pos=(0.45, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-17.0)
gram17_5 = visual.ImageStim(
    win=win,
    name='gram17_5', 
    image=str(stim_folder) + '/tangrams/gram17.png', mask=None,
    ori=0, pos=(-0.70, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-18.0)
gram18_5 = visual.ImageStim(
    win=win,
    name='gram18_5', 
    image=str(stim_folder) + '/tangrams/gram18.png', mask=None,
    ori=0, pos=(0.20, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-19.0)
gram19_5 = visual.ImageStim(
    win=win,
    name='gram19_5', 
    image=str(stim_folder) + '/tangrams/gram19.png', mask=None,
    ori=0, pos=(0.70, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-20.0)
gram20_5 = visual.ImageStim(
    win=win,
    name='gram20_5', 
    image=str(stim_folder) + '/tangrams/gram20.png', mask=None,
    ori=0, pos=(0.45, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-21.0)
gram21_5 = visual.ImageStim(
    win=win,
    name='gram21_5', 
    image=str(stim_folder) + '/tangrams/gram21.png', mask=None,
    ori=0, pos=(0.70, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-22.0)
gram22_5 = visual.ImageStim(
    win=win,
    name='gram22_5', 
    image=str(stim_folder) + '/tangrams/gram22.png', mask=None,
    ori=0, pos=(-0.45, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-23.0)
gram23_5 = visual.ImageStim(
    win=win,
    name='gram23_5', 
    image=str(stim_folder) + '/tangrams/gram23.png', mask=None,
    ori=0, pos=(0.20, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-24.0)
gram24_5 = visual.ImageStim(
    win=win,
    name='gram24_5', 
    image=str(stim_folder) + '/tangrams/gram24.png', mask=None,
    ori=0, pos=(-0.20, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-25.0)
easy_succ_5 = visual.TextStim(win=win, name='easy_succ_5',
    text='Move On',
    font='Arial',
    pos=(-.30, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-26.0);

# Initialize components for Routine "trial_6"
trial_6Clock = core.Clock()
one_6 = visual.ImageStim(
    win=win,
    name='one_6', 
    image=str(stim_folder) + '/one.png', mask=None,
    ori=0, pos=(-.70, .30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
mouse_8 = event.Mouse(win=win)
x, y = [None, None]
mouse_8.mouseClock = core.Clock()
two_6 = visual.ImageStim(
    win=win,
    name='two_6', 
    image=str(stim_folder) + '/two.png', mask=None,
    ori=0, pos=(-.45, .30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
three_6 = visual.ImageStim(
    win=win,
    name='three_6', 
    image=str(stim_folder) + '/three.png', mask=None,
    ori=0, pos=(-0.20, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
seven_6 = visual.ImageStim(
    win=win,
    name='seven_6', 
    image=str(stim_folder) + '/seven.png', mask=None,
    ori=0, pos=(-0.70, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
eight_6 = visual.ImageStim(
    win=win,
    name='eight_6', 
    image=str(stim_folder) + '/eight.png', mask=None,
    ori=0, pos=(-0.45, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
nine_6 = visual.ImageStim(
    win=win,
    name='nine_6', 
    image=str(stim_folder) + '/nine.png', mask=None,
    ori=0, pos=(-0.20, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
four_6 = visual.ImageStim(
    win=win,
    name='four_6', 
    image=str(stim_folder) + '/four.png', mask=None,
    ori=0, pos=(0.20, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
five_6 = visual.ImageStim(
    win=win,
    name='five_6', 
    image=str(stim_folder) + '/five.png', mask=None,
    ori=0, pos=(0.45, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
six_6 = visual.ImageStim(
    win=win,
    name='six_6', 
    image=str(stim_folder) + '/six.png', mask=None,
    ori=0, pos=(0.70, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)
ten_6 = visual.ImageStim(
    win=win,
    name='ten_6', 
    image=str(stim_folder) + '/ten.png', mask=None,
    ori=0, pos=(0.20, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)
eleven_6 = visual.ImageStim(
    win=win,
    name='eleven_6', 
    image=str(stim_folder) + '/eleven.png', mask=None,
    ori=0, pos=(0.45, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)
twelve_6 = visual.ImageStim(
    win=win,
    name='twelve_6', 
    image=str(stim_folder) + '/twelve.png', mask=None,
    ori=0, pos=(0.70, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-12.0)


def movePicked(picked, mouse, grabbed):
    if grabbed is not None and mouse.isPressedIn(grabbed):
        grabbed.pos = mouse.getPos()
        return grabbed
    else:
        for piece in picked:
            if mouse.isPressedIn(piece) and grabbed is None:
                print(f"the piece is {piece.name} and position is {piece.pos}")
                return piece

def win_continue():
    continue_text = visual.TextStim(win=win, name='continue_text',
    text="Continue",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0)
    return continue_text
    
def trial_timer():
    trial_time = visual.TextStim(win=win, name='trial_time',
    text=f"Completed in {int(t)} seconds!",
    font='Arial',
    pos=(0.4, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0)
    return trial_time

# failing because continue_text wasn't defined, but is listed as valid click
# offscreen_continue() creates an unclickable, offscreen object named continue_text
# continue_text is then updated and drawn when win_state = True 
def offscreen_continue():
    continue_text = visual.TextStim(win=win, name='continue_text',
    text="Continue",
    font='Arial',
    pos=(1.5, 1.5), height=0.001, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=0,
    languageStyle='LTR',
    depth=0.0)
    return continue_text

continue_text = offscreen_continue()

# create function to call on each frame, that will out the 
# x and y position of an image as tuple
# call this over each tangram



# then create a function that will test each tangra
# and once they're all in the right place, at the same time
# will return True

def hitbox_checker(box: str, tangram)->bool: 
    xpos = tangram.pos[0] 
    ypos = tangram.pos[1]
    x_upbound = hitbox_dict[box][0][0]
    x_downbound = hitbox_dict[box][0][1]
    y_upbound = hitbox_dict[box][1][0]
    y_downbound = hitbox_dict[box][1][1]
    if x_upbound > xpos > x_downbound and y_upbound >  ypos > y_downbound:
        return True

hitbox_dict = {('one'): ((-0.62, -0.7799999999999999), (0.38, 0.21999999999999997)),
 ('two'): ((-0.37, -0.53), (0.38, 0.21999999999999997)),
 ('three'): ((-0.12000000000000001, -0.28), (0.38, 0.21999999999999997)),
 ('four'): ((0.28, 0.12000000000000001), (0.38, 0.21999999999999997)),
 ('five'): ((0.53, 0.37), (0.38, 0.21999999999999997)),
 ('six'): ((0.7799999999999999, 0.62), (0.38, 0.21999999999999997)),
 ('seven'): ((-0.62, -0.7799999999999999), (-0.21999999999999997, -0.38)),
 ('eight'): ((-0.37, -0.53), (-0.21999999999999997, -0.38)),
 ('nine'): ((-0.12000000000000001, -0.28), (-0.21999999999999997, -0.38)),
 ('ten'): ((0.28, 0.12000000000000001), (-0.21999999999999997, -0.38)),
 ('eleven'): ((0.53, 0.37), (-0.21999999999999997, -0.38)),
 ('twelve'): ((0.7799999999999999, 0.62), (-0.21999999999999997, -0.38))}
gram13_6 = visual.ImageStim(
    win=win,
    name='gram13_6', 
    image=str(stim_folder) + '/tangrams/gram13.png', mask=None,
    ori=0, pos=(-.70, .3), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-14.0)
gram14_6 = visual.ImageStim(
    win=win,
    name='gram14_6', 
    image=str(stim_folder) + '/tangrams/gram14.png', mask=None,
    ori=0, pos=(-.45, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-15.0)
gram15_6 = visual.ImageStim(
    win=win,
    name='gram15_6', 
    image=str(stim_folder) + '/tangrams/gram15.png', mask=None,
    ori=0, pos=(-0.20, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-16.0)
gram16_6 = visual.ImageStim(
    win=win,
    name='gram16_6', 
    image=str(stim_folder) + '/tangrams/gram16.png', mask=None,
    ori=0, pos=(0.20, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-17.0)
gram17_6 = visual.ImageStim(
    win=win,
    name='gram17_6', 
    image=str(stim_folder) + '/tangrams/gram17.png', mask=None,
    ori=0, pos=(0.45, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-18.0)
gram18_6 = visual.ImageStim(
    win=win,
    name='gram18_6', 
    image=str(stim_folder) + '/tangrams/gram18.png', mask=None,
    ori=0, pos=(0.70, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-19.0)
gram19_6 = visual.ImageStim(
    win=win,
    name='gram19_6', 
    image=str(stim_folder) + '/tangrams/gram19.png', mask=None,
    ori=0, pos=(-0.70, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-20.0)
gram20_6 = visual.ImageStim(
    win=win,
    name='gram20_6', 
    image=str(stim_folder) + '/tangrams/gram20.png', mask=None,
    ori=0, pos=(-0.45, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-21.0)
gram21_6 = visual.ImageStim(
    win=win,
    name='gram21_6', 
    image=str(stim_folder) + '/tangrams/gram21.png', mask=None,
    ori=0, pos=(-0.20, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-22.0)
gram22_6 = visual.ImageStim(
    win=win,
    name='gram22_6', 
    image=str(stim_folder) + '/tangrams/gram22.png', mask=None,
    ori=0, pos=(0.20, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-23.0)
gram23_6 = visual.ImageStim(
    win=win,
    name='gram23_6', 
    image=str(stim_folder) + '/tangrams/gram23.png', mask=None,
    ori=0, pos=(0.45, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-24.0)
gram24_6 = visual.ImageStim(
    win=win,
    name='gram24_6', 
    image=str(stim_folder) + '/tangrams/gram24.png', mask=None,
    ori=0, pos=(0.70, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-25.0)
easy_succ_6 = visual.TextStim(win=win, name='easy_succ_6',
    text='Move On',
    font='Arial',
    pos=(-.30, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-26.0);

# Initialize components for Routine "call_exp2"
call_exp2Clock = core.Clock()
call_exp_text2 = visual.TextStim(win=win, name='call_exp_text2',
    text='Call experimenter to continue! \n\nPlease yell "We\'re done!"',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instr1"-------
# update component parameters for each repeat
# setup some python lists for storing info about the mouse
mouse.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
instr1Components = [instruction_text, mouse, text_2]
for thisComponent in instr1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "instr1"-------
while continueRoutine:
    # get current time
    t = instr1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruction_text* updates
    if instruction_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruction_text.frameNStart = frameN  # exact frame index
        instruction_text.tStart = t  # local t and not account for scr refresh
        instruction_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction_text, 'tStartRefresh')  # time at next scr refresh
        instruction_text.setAutoDraw(True)
    # *mouse* updates
    if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse.frameNStart = frameN  # exact frame index
        mouse.tStart = t  # local t and not account for scr refresh
        mouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
        mouse.status = STARTED
        mouse.mouseClock.reset()
        prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
    if mouse.status == STARTED:  # only update if started and not finished!
        buttons = mouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [text_2]:
                    if obj.contains(mouse):
                        gotValidClick = True
                        mouse.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr1"-------
for thisComponent in instr1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instruction_text.started', instruction_text.tStartRefresh)
thisExp.addData('instruction_text.stopped', instruction_text.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = mouse.getPos()
buttons = mouse.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    for obj in [text_2]:
        if obj.contains(mouse):
            gotValidClick = True
            mouse.clicked_name.append(obj.name)
thisExp.addData('mouse.x', x)
thisExp.addData('mouse.y', y)
thisExp.addData('mouse.leftButton', buttons[0])
thisExp.addData('mouse.midButton', buttons[1])
thisExp.addData('mouse.rightButton', buttons[2])
if len(mouse.clicked_name):
    thisExp.addData('mouse.clicked_name', mouse.clicked_name[0])
thisExp.addData('mouse.started', mouse.tStart)
thisExp.addData('mouse.stopped', mouse.tStop)
thisExp.nextEntry()
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# the Routine "instr1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr2"-------
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_2
gotValidClick = False  # until a click is received
# keep track of which components have finished
instr2Components = [text, mouse_2]
for thisComponent in instr2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "instr2"-------
while continueRoutine:
    # get current time
    t = instr2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    # *mouse_2* updates
    if mouse_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_2.frameNStart = frameN  # exact frame index
        mouse_2.tStart = t  # local t and not account for scr refresh
        mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
        mouse_2.status = STARTED
        mouse_2.mouseClock.reset()
        prevButtonState = mouse_2.getPressed()  # if button is down already this ISN'T a new click
    if mouse_2.status == STARTED:  # only update if started and not finished!
        buttons = mouse_2.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # abort routine on response
                continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr2"-------
for thisComponent in instr2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = mouse_2.getPos()
buttons = mouse_2.getPressed()
thisExp.addData('mouse_2.x', x)
thisExp.addData('mouse_2.y', y)
thisExp.addData('mouse_2.leftButton', buttons[0])
thisExp.addData('mouse_2.midButton', buttons[1])
thisExp.addData('mouse_2.rightButton', buttons[2])
thisExp.addData('mouse_2.started', mouse_2.tStart)
thisExp.addData('mouse_2.stopped', mouse_2.tStop)
thisExp.nextEntry()
# the Routine "instr2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trial"-------
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_3
mouse_3.clicked_name = []
gotValidClick = False  # until a click is received
pieces = [gram01,gram02,gram03,gram04,gram05,gram06,gram07,gram08,gram09,gram10,gram11,gram12]
picked = []
movingPiece = None

    # this works, it keeps track of what trial it is
    # so in win_checker() add an if statement
        # if this_trial is specific trial
        # change what hitboxes takes in as its 2nd argument
        # depending on the winstate order


def win_checker()->bool:
    order = [hitbox_checker("one", gram08), 
                    hitbox_checker("two", gram04),
                    hitbox_checker("three", gram07),
                    hitbox_checker("four", gram02),
                    hitbox_checker("five", gram01),
                    hitbox_checker("six", gram05),
                    hitbox_checker("seven", gram10),
                    hitbox_checker("eight", gram09),
                    hitbox_checker("nine", gram03),
                    hitbox_checker("ten", gram12),
                    hitbox_checker("eleven", gram06),
                    hitbox_checker("twelve", gram11)]
    if all(order):
        return True

trial_time = []
# keep track of which components have finished
trialComponents = [one, mouse_3, two, three, seven, eight, nine, four, five, six, ten, eleven, twelve, gram01, gram02, gram03, gram04, gram05, gram06, gram07, gram08, gram09, gram10, gram11, gram12, easy_succ]
for thisComponent in trialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "trial"-------
while continueRoutine:
    # get current time
    t = trialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *one* updates
    if one.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        one.frameNStart = frameN  # exact frame index
        one.tStart = t  # local t and not account for scr refresh
        one.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(one, 'tStartRefresh')  # time at next scr refresh
        one.setAutoDraw(True)
    # *mouse_3* updates
    if mouse_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_3.frameNStart = frameN  # exact frame index
        mouse_3.tStart = t  # local t and not account for scr refresh
        mouse_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_3, 'tStartRefresh')  # time at next scr refresh
        mouse_3.status = STARTED
        mouse_3.mouseClock.reset()
        prevButtonState = mouse_3.getPressed()  # if button is down already this ISN'T a new click
    if mouse_3.status == STARTED:  # only update if started and not finished!
        buttons = mouse_3.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [continue_text, easy_succ]:
                    if obj.contains(mouse_3):
                        gotValidClick = True
                        mouse_3.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # *two* updates
    if two.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        two.frameNStart = frameN  # exact frame index
        two.tStart = t  # local t and not account for scr refresh
        two.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(two, 'tStartRefresh')  # time at next scr refresh
        two.setAutoDraw(True)
    
    # *three* updates
    if three.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        three.frameNStart = frameN  # exact frame index
        three.tStart = t  # local t and not account for scr refresh
        three.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(three, 'tStartRefresh')  # time at next scr refresh
        three.setAutoDraw(True)
    
    # *seven* updates
    if seven.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        seven.frameNStart = frameN  # exact frame index
        seven.tStart = t  # local t and not account for scr refresh
        seven.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(seven, 'tStartRefresh')  # time at next scr refresh
        seven.setAutoDraw(True)
    
    # *eight* updates
    if eight.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        eight.frameNStart = frameN  # exact frame index
        eight.tStart = t  # local t and not account for scr refresh
        eight.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(eight, 'tStartRefresh')  # time at next scr refresh
        eight.setAutoDraw(True)
    
    # *nine* updates
    if nine.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        nine.frameNStart = frameN  # exact frame index
        nine.tStart = t  # local t and not account for scr refresh
        nine.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(nine, 'tStartRefresh')  # time at next scr refresh
        nine.setAutoDraw(True)
    
    # *four* updates
    if four.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        four.frameNStart = frameN  # exact frame index
        four.tStart = t  # local t and not account for scr refresh
        four.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(four, 'tStartRefresh')  # time at next scr refresh
        four.setAutoDraw(True)
    
    # *five* updates
    if five.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        five.frameNStart = frameN  # exact frame index
        five.tStart = t  # local t and not account for scr refresh
        five.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(five, 'tStartRefresh')  # time at next scr refresh
        five.setAutoDraw(True)
    
    # *six* updates
    if six.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        six.frameNStart = frameN  # exact frame index
        six.tStart = t  # local t and not account for scr refresh
        six.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(six, 'tStartRefresh')  # time at next scr refresh
        six.setAutoDraw(True)
    
    # *ten* updates
    if ten.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ten.frameNStart = frameN  # exact frame index
        ten.tStart = t  # local t and not account for scr refresh
        ten.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ten, 'tStartRefresh')  # time at next scr refresh
        ten.setAutoDraw(True)
    
    # *eleven* updates
    if eleven.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        eleven.frameNStart = frameN  # exact frame index
        eleven.tStart = t  # local t and not account for scr refresh
        eleven.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(eleven, 'tStartRefresh')  # time at next scr refresh
        eleven.setAutoDraw(True)
    
    # *twelve* updates
    if twelve.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        twelve.frameNStart = frameN  # exact frame index
        twelve.tStart = t  # local t and not account for scr refresh
        twelve.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(twelve, 'tStartRefresh')  # time at next scr refresh
        twelve.setAutoDraw(True)
    for piece in pieces:
        if mouse.isPressedIn(piece) and movingPiece is None:
            picked.append(piece)
    
    movingPiece = movePicked(picked, mouse, movingPiece)
    
    gram01_xpos = gram01.pos[0]
    gram01_ypos = gram01.pos[1]
    
    win_state = False
    
    win_state = win_checker()

    # in begin routine, create a function that will check if
    # all the tangrams are in the correct spot
    # if they are, then have it return true and draw continue_text
    
    if win_state:
        continue_text = win_continue()
        continue_text.draw()
        trial_time.append(trial_timer())
        trial_time[0].draw()
    else: 
        win.flip()
    
    
    #if mouse.isPressedIn(polygon):
    #    crosses.append(makeCross(mouse.getPos()))
    
    # *gram01* updates
    if gram01.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram01.frameNStart = frameN  # exact frame index
        gram01.tStart = t  # local t and not account for scr refresh
        gram01.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram01, 'tStartRefresh')  # time at next scr refresh
        gram01.setAutoDraw(True)
    
    # *gram02* updates
    if gram02.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram02.frameNStart = frameN  # exact frame index
        gram02.tStart = t  # local t and not account for scr refresh
        gram02.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram02, 'tStartRefresh')  # time at next scr refresh
        gram02.setAutoDraw(True)
    
    # *gram03* updates
    if gram03.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram03.frameNStart = frameN  # exact frame index
        gram03.tStart = t  # local t and not account for scr refresh
        gram03.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram03, 'tStartRefresh')  # time at next scr refresh
        gram03.setAutoDraw(True)
    
    # *gram04* updates
    if gram04.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram04.frameNStart = frameN  # exact frame index
        gram04.tStart = t  # local t and not account for scr refresh
        gram04.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram04, 'tStartRefresh')  # time at next scr refresh
        gram04.setAutoDraw(True)
    
    # *gram05* updates
    if gram05.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram05.frameNStart = frameN  # exact frame index
        gram05.tStart = t  # local t and not account for scr refresh
        gram05.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram05, 'tStartRefresh')  # time at next scr refresh
        gram05.setAutoDraw(True)
    
    # *gram06* updates
    if gram06.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram06.frameNStart = frameN  # exact frame index
        gram06.tStart = t  # local t and not account for scr refresh
        gram06.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram06, 'tStartRefresh')  # time at next scr refresh
        gram06.setAutoDraw(True)
    
    # *gram07* updates
    if gram07.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram07.frameNStart = frameN  # exact frame index
        gram07.tStart = t  # local t and not account for scr refresh
        gram07.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram07, 'tStartRefresh')  # time at next scr refresh
        gram07.setAutoDraw(True)
    
    # *gram08* updates
    if gram08.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram08.frameNStart = frameN  # exact frame index
        gram08.tStart = t  # local t and not account for scr refresh
        gram08.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram08, 'tStartRefresh')  # time at next scr refresh
        gram08.setAutoDraw(True)
    
    # *gram09* updates
    if gram09.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram09.frameNStart = frameN  # exact frame index
        gram09.tStart = t  # local t and not account for scr refresh
        gram09.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram09, 'tStartRefresh')  # time at next scr refresh
        gram09.setAutoDraw(True)
    
    # *gram10* updates
    if gram10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram10.frameNStart = frameN  # exact frame index
        gram10.tStart = t  # local t and not account for scr refresh
        gram10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram10, 'tStartRefresh')  # time at next scr refresh
        gram10.setAutoDraw(True)
    
    # *gram11* updates
    if gram11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram11.frameNStart = frameN  # exact frame index
        gram11.tStart = t  # local t and not account for scr refresh
        gram11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram11, 'tStartRefresh')  # time at next scr refresh
        gram11.setAutoDraw(True)
    
    # *gram12* updates
    if gram12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram12.frameNStart = frameN  # exact frame index
        gram12.tStart = t  # local t and not account for scr refresh
        gram12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram12, 'tStartRefresh')  # time at next scr refresh
        gram12.setAutoDraw(True)
    
    # *easy_succ* updates
    if easy_succ.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        easy_succ.frameNStart = frameN  # exact frame index
        easy_succ.tStart = t  # local t and not account for scr refresh
        easy_succ.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(easy_succ, 'tStartRefresh')  # time at next scr refresh
        easy_succ.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial"-------
for thisComponent in trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('one.started', one.tStartRefresh)
thisExp.addData('one.stopped', one.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = mouse_3.getPos()
buttons = mouse_3.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    for obj in [continue_text, easy_succ]:
        if obj.contains(mouse_3):
            gotValidClick = True
            mouse_3.clicked_name.append(obj.name)
thisExp.addData('mouse_3.x', x)
thisExp.addData('mouse_3.y', y)
thisExp.addData('mouse_3.leftButton', buttons[0])
thisExp.addData('mouse_3.midButton', buttons[1])
thisExp.addData('mouse_3.rightButton', buttons[2])
if len(mouse_3.clicked_name):
    thisExp.addData('mouse_3.clicked_name', mouse_3.clicked_name[0])
thisExp.addData('mouse_3.started', mouse_3.tStart)
thisExp.addData('mouse_3.stopped', mouse_3.tStop)
thisExp.nextEntry()
thisExp.addData('two.started', two.tStartRefresh)
thisExp.addData('two.stopped', two.tStopRefresh)
thisExp.addData('three.started', three.tStartRefresh)
thisExp.addData('three.stopped', three.tStopRefresh)
thisExp.addData('seven.started', seven.tStartRefresh)
thisExp.addData('seven.stopped', seven.tStopRefresh)
thisExp.addData('eight.started', eight.tStartRefresh)
thisExp.addData('eight.stopped', eight.tStopRefresh)
thisExp.addData('nine.started', nine.tStartRefresh)
thisExp.addData('nine.stopped', nine.tStopRefresh)
thisExp.addData('four.started', four.tStartRefresh)
thisExp.addData('four.stopped', four.tStopRefresh)
thisExp.addData('five.started', five.tStartRefresh)
thisExp.addData('five.stopped', five.tStopRefresh)
thisExp.addData('six.started', six.tStartRefresh)
thisExp.addData('six.stopped', six.tStopRefresh)
thisExp.addData('ten.started', ten.tStartRefresh)
thisExp.addData('ten.stopped', ten.tStopRefresh)
thisExp.addData('eleven.started', eleven.tStartRefresh)
thisExp.addData('eleven.stopped', eleven.tStopRefresh)
thisExp.addData('twelve.started', twelve.tStartRefresh)
thisExp.addData('twelve.stopped', twelve.tStopRefresh)
thisExp.addData('gram01.started', gram01.tStartRefresh)
thisExp.addData('gram01.stopped', gram01.tStopRefresh)
thisExp.addData('gram02.started', gram02.tStartRefresh)
thisExp.addData('gram02.stopped', gram02.tStopRefresh)
thisExp.addData('gram03.started', gram03.tStartRefresh)
thisExp.addData('gram03.stopped', gram03.tStopRefresh)
thisExp.addData('gram04.started', gram04.tStartRefresh)
thisExp.addData('gram04.stopped', gram04.tStopRefresh)
thisExp.addData('gram05.started', gram05.tStartRefresh)
thisExp.addData('gram05.stopped', gram05.tStopRefresh)
thisExp.addData('gram06.started', gram06.tStartRefresh)
thisExp.addData('gram06.stopped', gram06.tStopRefresh)
thisExp.addData('gram07.started', gram07.tStartRefresh)
thisExp.addData('gram07.stopped', gram07.tStopRefresh)
thisExp.addData('gram08.started', gram08.tStartRefresh)
thisExp.addData('gram08.stopped', gram08.tStopRefresh)
thisExp.addData('gram09.started', gram09.tStartRefresh)
thisExp.addData('gram09.stopped', gram09.tStopRefresh)
thisExp.addData('gram10.started', gram10.tStartRefresh)
thisExp.addData('gram10.stopped', gram10.tStopRefresh)
thisExp.addData('gram11.started', gram11.tStartRefresh)
thisExp.addData('gram11.stopped', gram11.tStopRefresh)
thisExp.addData('gram12.started', gram12.tStartRefresh)
thisExp.addData('gram12.stopped', gram12.tStopRefresh)
thisExp.addData('easy_succ.started', easy_succ.tStartRefresh)
thisExp.addData('easy_succ.stopped', easy_succ.tStopRefresh)
# the Routine "trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trial_2"-------
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_4
mouse_4.clicked_name = []
gotValidClick = False  # until a click is received
pieces = [gram01_2,gram02_2,gram03_2,gram04_2,gram05_2,gram06_2,gram07_2,gram08_2,gram09_2,gram10_2,gram11_2,gram12_2]
picked = []
movingPiece = None

    # this works, it keeps track of what trial it is
    # so in win_checker() add an if statement
        # if this_trial is specific trial
        # change what hitboxes takes in as its 2nd argument
        # depending on the winstate order


def win_checker()->bool:
    order = [hitbox_checker("one", gram10_2), 
                    hitbox_checker("two", gram09_2),
                    hitbox_checker("three", gram07_2),
                    hitbox_checker("four", gram03_2),
                    hitbox_checker("five", gram12_2),
                    hitbox_checker("six", gram02_2),
                    hitbox_checker("seven", gram08_2),
                    hitbox_checker("eight", gram11_2),
                    hitbox_checker("nine", gram04_2),
                    hitbox_checker("ten", gram05_2),
                    hitbox_checker("eleven", gram06_2),
                    hitbox_checker("twelve", gram01_2)]
    if all(order):
        return True

trial_time = []
# keep track of which components have finished
trial_2Components = [one_2, mouse_4, two_2, three_2, seven_2, eight_2, nine_2, four_2, five_2, six_2, ten_2, eleven_2, twelve_2, gram01_2, gram02_2, gram03_2, gram04_2, gram05_2, gram06_2, gram07_2, gram08_2, gram09_2, gram10_2, gram11_2, gram12_2, easy_succ_2]
for thisComponent in trial_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "trial_2"-------
while continueRoutine:
    # get current time
    t = trial_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *one_2* updates
    if one_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        one_2.frameNStart = frameN  # exact frame index
        one_2.tStart = t  # local t and not account for scr refresh
        one_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(one_2, 'tStartRefresh')  # time at next scr refresh
        one_2.setAutoDraw(True)
    # *mouse_4* updates
    if mouse_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_4.frameNStart = frameN  # exact frame index
        mouse_4.tStart = t  # local t and not account for scr refresh
        mouse_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_4, 'tStartRefresh')  # time at next scr refresh
        mouse_4.status = STARTED
        mouse_4.mouseClock.reset()
        prevButtonState = mouse_4.getPressed()  # if button is down already this ISN'T a new click
    if mouse_4.status == STARTED:  # only update if started and not finished!
        buttons = mouse_4.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [continue_text, easy_succ_2]:
                    if obj.contains(mouse_4):
                        gotValidClick = True
                        mouse_4.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # *two_2* updates
    if two_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        two_2.frameNStart = frameN  # exact frame index
        two_2.tStart = t  # local t and not account for scr refresh
        two_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(two_2, 'tStartRefresh')  # time at next scr refresh
        two_2.setAutoDraw(True)
    
    # *three_2* updates
    if three_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        three_2.frameNStart = frameN  # exact frame index
        three_2.tStart = t  # local t and not account for scr refresh
        three_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(three_2, 'tStartRefresh')  # time at next scr refresh
        three_2.setAutoDraw(True)
    
    # *seven_2* updates
    if seven_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        seven_2.frameNStart = frameN  # exact frame index
        seven_2.tStart = t  # local t and not account for scr refresh
        seven_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(seven_2, 'tStartRefresh')  # time at next scr refresh
        seven_2.setAutoDraw(True)
    
    # *eight_2* updates
    if eight_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        eight_2.frameNStart = frameN  # exact frame index
        eight_2.tStart = t  # local t and not account for scr refresh
        eight_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(eight_2, 'tStartRefresh')  # time at next scr refresh
        eight_2.setAutoDraw(True)
    
    # *nine_2* updates
    if nine_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        nine_2.frameNStart = frameN  # exact frame index
        nine_2.tStart = t  # local t and not account for scr refresh
        nine_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(nine_2, 'tStartRefresh')  # time at next scr refresh
        nine_2.setAutoDraw(True)
    
    # *four_2* updates
    if four_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        four_2.frameNStart = frameN  # exact frame index
        four_2.tStart = t  # local t and not account for scr refresh
        four_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(four_2, 'tStartRefresh')  # time at next scr refresh
        four_2.setAutoDraw(True)
    
    # *five_2* updates
    if five_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        five_2.frameNStart = frameN  # exact frame index
        five_2.tStart = t  # local t and not account for scr refresh
        five_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(five_2, 'tStartRefresh')  # time at next scr refresh
        five_2.setAutoDraw(True)
    
    # *six_2* updates
    if six_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        six_2.frameNStart = frameN  # exact frame index
        six_2.tStart = t  # local t and not account for scr refresh
        six_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(six_2, 'tStartRefresh')  # time at next scr refresh
        six_2.setAutoDraw(True)
    
    # *ten_2* updates
    if ten_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ten_2.frameNStart = frameN  # exact frame index
        ten_2.tStart = t  # local t and not account for scr refresh
        ten_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ten_2, 'tStartRefresh')  # time at next scr refresh
        ten_2.setAutoDraw(True)
    
    # *eleven_2* updates
    if eleven_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        eleven_2.frameNStart = frameN  # exact frame index
        eleven_2.tStart = t  # local t and not account for scr refresh
        eleven_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(eleven_2, 'tStartRefresh')  # time at next scr refresh
        eleven_2.setAutoDraw(True)
    
    # *twelve_2* updates
    if twelve_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        twelve_2.frameNStart = frameN  # exact frame index
        twelve_2.tStart = t  # local t and not account for scr refresh
        twelve_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(twelve_2, 'tStartRefresh')  # time at next scr refresh
        twelve_2.setAutoDraw(True)
    for piece in pieces:
        if mouse.isPressedIn(piece) and movingPiece is None:
            picked.append(piece)
    
    movingPiece = movePicked(picked, mouse, movingPiece)
    
    gram01_xpos = gram01.pos[0]
    gram01_ypos = gram01.pos[1]
    
    win_state = False
    
    
    win_state = win_checker()
    
    continue_text = offscreen_continue()
    continue_text.draw()
    
    
    # in begin routine, create a function that will check if
    # all the tangrams are in the correct spot
    # if they are, then have it return true and draw continue_text
    
    if win_state:
        continue_text = win_continue()
        continue_text.draw()
        trial_time.append(trial_timer())
        trial_time[0].draw()
    else: 
        win.flip()
    
    
    #if mouse.isPressedIn(polygon):
    #    crosses.append(makeCross(mouse.getPos()))
    
    # *gram01_2* updates
    if gram01_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram01_2.frameNStart = frameN  # exact frame index
        gram01_2.tStart = t  # local t and not account for scr refresh
        gram01_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram01_2, 'tStartRefresh')  # time at next scr refresh
        gram01_2.setAutoDraw(True)
    
    # *gram02_2* updates
    if gram02_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram02_2.frameNStart = frameN  # exact frame index
        gram02_2.tStart = t  # local t and not account for scr refresh
        gram02_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram02_2, 'tStartRefresh')  # time at next scr refresh
        gram02_2.setAutoDraw(True)
    
    # *gram03_2* updates
    if gram03_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram03_2.frameNStart = frameN  # exact frame index
        gram03_2.tStart = t  # local t and not account for scr refresh
        gram03_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram03_2, 'tStartRefresh')  # time at next scr refresh
        gram03_2.setAutoDraw(True)
    
    # *gram04_2* updates
    if gram04_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram04_2.frameNStart = frameN  # exact frame index
        gram04_2.tStart = t  # local t and not account for scr refresh
        gram04_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram04_2, 'tStartRefresh')  # time at next scr refresh
        gram04_2.setAutoDraw(True)
    
    # *gram05_2* updates
    if gram05_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram05_2.frameNStart = frameN  # exact frame index
        gram05_2.tStart = t  # local t and not account for scr refresh
        gram05_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram05_2, 'tStartRefresh')  # time at next scr refresh
        gram05_2.setAutoDraw(True)
    
    # *gram06_2* updates
    if gram06_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram06_2.frameNStart = frameN  # exact frame index
        gram06_2.tStart = t  # local t and not account for scr refresh
        gram06_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram06_2, 'tStartRefresh')  # time at next scr refresh
        gram06_2.setAutoDraw(True)
    
    # *gram07_2* updates
    if gram07_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram07_2.frameNStart = frameN  # exact frame index
        gram07_2.tStart = t  # local t and not account for scr refresh
        gram07_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram07_2, 'tStartRefresh')  # time at next scr refresh
        gram07_2.setAutoDraw(True)
    
    # *gram08_2* updates
    if gram08_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram08_2.frameNStart = frameN  # exact frame index
        gram08_2.tStart = t  # local t and not account for scr refresh
        gram08_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram08_2, 'tStartRefresh')  # time at next scr refresh
        gram08_2.setAutoDraw(True)
    
    # *gram09_2* updates
    if gram09_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram09_2.frameNStart = frameN  # exact frame index
        gram09_2.tStart = t  # local t and not account for scr refresh
        gram09_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram09_2, 'tStartRefresh')  # time at next scr refresh
        gram09_2.setAutoDraw(True)
    
    # *gram10_2* updates
    if gram10_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram10_2.frameNStart = frameN  # exact frame index
        gram10_2.tStart = t  # local t and not account for scr refresh
        gram10_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram10_2, 'tStartRefresh')  # time at next scr refresh
        gram10_2.setAutoDraw(True)
    
    # *gram11_2* updates
    if gram11_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram11_2.frameNStart = frameN  # exact frame index
        gram11_2.tStart = t  # local t and not account for scr refresh
        gram11_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram11_2, 'tStartRefresh')  # time at next scr refresh
        gram11_2.setAutoDraw(True)
    
    # *gram12_2* updates
    if gram12_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram12_2.frameNStart = frameN  # exact frame index
        gram12_2.tStart = t  # local t and not account for scr refresh
        gram12_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram12_2, 'tStartRefresh')  # time at next scr refresh
        gram12_2.setAutoDraw(True)
    
    # *easy_succ_2* updates
    if easy_succ_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        easy_succ_2.frameNStart = frameN  # exact frame index
        easy_succ_2.tStart = t  # local t and not account for scr refresh
        easy_succ_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(easy_succ_2, 'tStartRefresh')  # time at next scr refresh
        easy_succ_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial_2"-------
for thisComponent in trial_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('one_2.started', one_2.tStartRefresh)
thisExp.addData('one_2.stopped', one_2.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = mouse_4.getPos()
buttons = mouse_4.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    for obj in [continue_text, easy_succ_2]:
        if obj.contains(mouse_4):
            gotValidClick = True
            mouse_4.clicked_name.append(obj.name)
thisExp.addData('mouse_4.x', x)
thisExp.addData('mouse_4.y', y)
thisExp.addData('mouse_4.leftButton', buttons[0])
thisExp.addData('mouse_4.midButton', buttons[1])
thisExp.addData('mouse_4.rightButton', buttons[2])
if len(mouse_4.clicked_name):
    thisExp.addData('mouse_4.clicked_name', mouse_4.clicked_name[0])
thisExp.addData('mouse_4.started', mouse_4.tStart)
thisExp.addData('mouse_4.stopped', mouse_4.tStop)
thisExp.nextEntry()
thisExp.addData('two_2.started', two_2.tStartRefresh)
thisExp.addData('two_2.stopped', two_2.tStopRefresh)
thisExp.addData('three_2.started', three_2.tStartRefresh)
thisExp.addData('three_2.stopped', three_2.tStopRefresh)
thisExp.addData('seven_2.started', seven_2.tStartRefresh)
thisExp.addData('seven_2.stopped', seven_2.tStopRefresh)
thisExp.addData('eight_2.started', eight_2.tStartRefresh)
thisExp.addData('eight_2.stopped', eight_2.tStopRefresh)
thisExp.addData('nine_2.started', nine_2.tStartRefresh)
thisExp.addData('nine_2.stopped', nine_2.tStopRefresh)
thisExp.addData('four_2.started', four_2.tStartRefresh)
thisExp.addData('four_2.stopped', four_2.tStopRefresh)
thisExp.addData('five_2.started', five_2.tStartRefresh)
thisExp.addData('five_2.stopped', five_2.tStopRefresh)
thisExp.addData('six_2.started', six_2.tStartRefresh)
thisExp.addData('six_2.stopped', six_2.tStopRefresh)
thisExp.addData('ten_2.started', ten_2.tStartRefresh)
thisExp.addData('ten_2.stopped', ten_2.tStopRefresh)
thisExp.addData('eleven_2.started', eleven_2.tStartRefresh)
thisExp.addData('eleven_2.stopped', eleven_2.tStopRefresh)
thisExp.addData('twelve_2.started', twelve_2.tStartRefresh)
thisExp.addData('twelve_2.stopped', twelve_2.tStopRefresh)
thisExp.addData('gram01_2.started', gram01_2.tStartRefresh)
thisExp.addData('gram01_2.stopped', gram01_2.tStopRefresh)
thisExp.addData('gram02_2.started', gram02_2.tStartRefresh)
thisExp.addData('gram02_2.stopped', gram02_2.tStopRefresh)
thisExp.addData('gram03_2.started', gram03_2.tStartRefresh)
thisExp.addData('gram03_2.stopped', gram03_2.tStopRefresh)
thisExp.addData('gram04_2.started', gram04_2.tStartRefresh)
thisExp.addData('gram04_2.stopped', gram04_2.tStopRefresh)
thisExp.addData('gram05_2.started', gram05_2.tStartRefresh)
thisExp.addData('gram05_2.stopped', gram05_2.tStopRefresh)
thisExp.addData('gram06_2.started', gram06_2.tStartRefresh)
thisExp.addData('gram06_2.stopped', gram06_2.tStopRefresh)
thisExp.addData('gram07_2.started', gram07_2.tStartRefresh)
thisExp.addData('gram07_2.stopped', gram07_2.tStopRefresh)
thisExp.addData('gram08_2.started', gram08_2.tStartRefresh)
thisExp.addData('gram08_2.stopped', gram08_2.tStopRefresh)
thisExp.addData('gram09_2.started', gram09_2.tStartRefresh)
thisExp.addData('gram09_2.stopped', gram09_2.tStopRefresh)
thisExp.addData('gram10_2.started', gram10_2.tStartRefresh)
thisExp.addData('gram10_2.stopped', gram10_2.tStopRefresh)
thisExp.addData('gram11_2.started', gram11_2.tStartRefresh)
thisExp.addData('gram11_2.stopped', gram11_2.tStopRefresh)
thisExp.addData('gram12_2.started', gram12_2.tStartRefresh)
thisExp.addData('gram12_2.stopped', gram12_2.tStopRefresh)
thisExp.addData('easy_succ_2.started', easy_succ_2.tStartRefresh)
thisExp.addData('easy_succ_2.stopped', easy_succ_2.tStopRefresh)
# the Routine "trial_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trial_3"-------
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_5
mouse_5.clicked_name = []
gotValidClick = False  # until a click is received
pieces = [gram01_3,gram02_3,gram03_3,gram04_3,gram05_3,gram06_3,gram07_3,gram08_3,gram09_3,gram10_3,gram11_3,gram12_3]
picked = []
movingPiece = None

    # this works, it keeps track of what trial it is
    # so in win_checker() add an if statement
        # if this_trial is specific trial
        # change what hitboxes takes in as its 2nd argument
        # depending on the winstate order


def win_checker()->bool:
    order = [hitbox_checker("one", gram02_3), 
                    hitbox_checker("two", gram11_3),
                    hitbox_checker("three", gram01_3),
                    hitbox_checker("four", gram04_3),
                    hitbox_checker("five", gram08_3),
                    hitbox_checker("six", gram03_3),
                    hitbox_checker("seven", gram10_3),
                    hitbox_checker("eight", gram09_3),
                    hitbox_checker("nine", gram12_3),
                    hitbox_checker("ten", gram05_3),
                    hitbox_checker("eleven", gram07_3),
                    hitbox_checker("twelve", gram06_3)]
    if all(order):
        return True
# keep track of which components have finished
trial_3Components = [one_3, mouse_5, two_3, three_3, seven_3, eight_3, nine_3, four_3, five_3, six_3, ten_3, eleven_3, twelve_3, gram01_3, gram02_3, gram03_3, gram04_3, gram05_3, gram06_3, gram07_3, gram08_3, gram09_3, gram10_3, gram11_3, gram12_3, easy_succ_3]
for thisComponent in trial_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "trial_3"-------
while continueRoutine:
    # get current time
    t = trial_3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial_3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *one_3* updates
    if one_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        one_3.frameNStart = frameN  # exact frame index
        one_3.tStart = t  # local t and not account for scr refresh
        one_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(one_3, 'tStartRefresh')  # time at next scr refresh
        one_3.setAutoDraw(True)
    # *mouse_5* updates
    if mouse_5.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_5.frameNStart = frameN  # exact frame index
        mouse_5.tStart = t  # local t and not account for scr refresh
        mouse_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_5, 'tStartRefresh')  # time at next scr refresh
        mouse_5.status = STARTED
        mouse_5.mouseClock.reset()
        prevButtonState = mouse_5.getPressed()  # if button is down already this ISN'T a new click
    if mouse_5.status == STARTED:  # only update if started and not finished!
        buttons = mouse_5.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [continue_text, easy_succ_3]:
                    if obj.contains(mouse_5):
                        gotValidClick = True
                        mouse_5.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # *two_3* updates
    if two_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        two_3.frameNStart = frameN  # exact frame index
        two_3.tStart = t  # local t and not account for scr refresh
        two_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(two_3, 'tStartRefresh')  # time at next scr refresh
        two_3.setAutoDraw(True)
    
    # *three_3* updates
    if three_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        three_3.frameNStart = frameN  # exact frame index
        three_3.tStart = t  # local t and not account for scr refresh
        three_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(three_3, 'tStartRefresh')  # time at next scr refresh
        three_3.setAutoDraw(True)
    
    # *seven_3* updates
    if seven_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        seven_3.frameNStart = frameN  # exact frame index
        seven_3.tStart = t  # local t and not account for scr refresh
        seven_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(seven_3, 'tStartRefresh')  # time at next scr refresh
        seven_3.setAutoDraw(True)
    
    # *eight_3* updates
    if eight_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        eight_3.frameNStart = frameN  # exact frame index
        eight_3.tStart = t  # local t and not account for scr refresh
        eight_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(eight_3, 'tStartRefresh')  # time at next scr refresh
        eight_3.setAutoDraw(True)
    
    # *nine_3* updates
    if nine_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        nine_3.frameNStart = frameN  # exact frame index
        nine_3.tStart = t  # local t and not account for scr refresh
        nine_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(nine_3, 'tStartRefresh')  # time at next scr refresh
        nine_3.setAutoDraw(True)
    
    # *four_3* updates
    if four_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        four_3.frameNStart = frameN  # exact frame index
        four_3.tStart = t  # local t and not account for scr refresh
        four_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(four_3, 'tStartRefresh')  # time at next scr refresh
        four_3.setAutoDraw(True)
    
    # *five_3* updates
    if five_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        five_3.frameNStart = frameN  # exact frame index
        five_3.tStart = t  # local t and not account for scr refresh
        five_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(five_3, 'tStartRefresh')  # time at next scr refresh
        five_3.setAutoDraw(True)
    
    # *six_3* updates
    if six_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        six_3.frameNStart = frameN  # exact frame index
        six_3.tStart = t  # local t and not account for scr refresh
        six_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(six_3, 'tStartRefresh')  # time at next scr refresh
        six_3.setAutoDraw(True)
    
    # *ten_3* updates
    if ten_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ten_3.frameNStart = frameN  # exact frame index
        ten_3.tStart = t  # local t and not account for scr refresh
        ten_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ten_3, 'tStartRefresh')  # time at next scr refresh
        ten_3.setAutoDraw(True)
    
    # *eleven_3* updates
    if eleven_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        eleven_3.frameNStart = frameN  # exact frame index
        eleven_3.tStart = t  # local t and not account for scr refresh
        eleven_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(eleven_3, 'tStartRefresh')  # time at next scr refresh
        eleven_3.setAutoDraw(True)
    
    # *twelve_3* updates
    if twelve_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        twelve_3.frameNStart = frameN  # exact frame index
        twelve_3.tStart = t  # local t and not account for scr refresh
        twelve_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(twelve_3, 'tStartRefresh')  # time at next scr refresh
        twelve_3.setAutoDraw(True)
    for piece in pieces:
        if mouse.isPressedIn(piece) and movingPiece is None:
            picked.append(piece)
    
    movingPiece = movePicked(picked, mouse, movingPiece)
    
    gram01_xpos = gram01.pos[0]
    gram01_ypos = gram01.pos[1]
    
    win_state = False
    
    '''
    if 0.778 > gram01_xpos > 0.62 and -0.219 > gram01_ypos > -0.38:
        win_state = True
    else:
        win_state = False
    '''
    
    win_state = win_checker()
    
    continue_text = offscreen_continue() # move the continue off_screen, so you cant click it 
    continue_text.draw()
    
    # in begin routine, create a function that will check if
    # all the tangrams are in the correct spot
    # if they are, then have it return true and draw continue_text
    
    if win_state:
        continue_text = win_continue()
        continue_text.draw()
        trial_time.append(trial_timer())
        trial_time[0].draw()
    else: 
        win.flip()
    
    
    #if mouse.isPressedIn(polygon):
    #    crosses.append(makeCross(mouse.getPos()))
    
    # *gram01_3* updates
    if gram01_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram01_3.frameNStart = frameN  # exact frame index
        gram01_3.tStart = t  # local t and not account for scr refresh
        gram01_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram01_3, 'tStartRefresh')  # time at next scr refresh
        gram01_3.setAutoDraw(True)
    
    # *gram02_3* updates
    if gram02_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram02_3.frameNStart = frameN  # exact frame index
        gram02_3.tStart = t  # local t and not account for scr refresh
        gram02_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram02_3, 'tStartRefresh')  # time at next scr refresh
        gram02_3.setAutoDraw(True)
    
    # *gram03_3* updates
    if gram03_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram03_3.frameNStart = frameN  # exact frame index
        gram03_3.tStart = t  # local t and not account for scr refresh
        gram03_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram03_3, 'tStartRefresh')  # time at next scr refresh
        gram03_3.setAutoDraw(True)
    
    # *gram04_3* updates
    if gram04_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram04_3.frameNStart = frameN  # exact frame index
        gram04_3.tStart = t  # local t and not account for scr refresh
        gram04_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram04_3, 'tStartRefresh')  # time at next scr refresh
        gram04_3.setAutoDraw(True)
    
    # *gram05_3* updates
    if gram05_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram05_3.frameNStart = frameN  # exact frame index
        gram05_3.tStart = t  # local t and not account for scr refresh
        gram05_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram05_3, 'tStartRefresh')  # time at next scr refresh
        gram05_3.setAutoDraw(True)
    
    # *gram06_3* updates
    if gram06_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram06_3.frameNStart = frameN  # exact frame index
        gram06_3.tStart = t  # local t and not account for scr refresh
        gram06_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram06_3, 'tStartRefresh')  # time at next scr refresh
        gram06_3.setAutoDraw(True)
    
    # *gram07_3* updates
    if gram07_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram07_3.frameNStart = frameN  # exact frame index
        gram07_3.tStart = t  # local t and not account for scr refresh
        gram07_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram07_3, 'tStartRefresh')  # time at next scr refresh
        gram07_3.setAutoDraw(True)
    
    # *gram08_3* updates
    if gram08_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram08_3.frameNStart = frameN  # exact frame index
        gram08_3.tStart = t  # local t and not account for scr refresh
        gram08_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram08_3, 'tStartRefresh')  # time at next scr refresh
        gram08_3.setAutoDraw(True)
    
    # *gram09_3* updates
    if gram09_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram09_3.frameNStart = frameN  # exact frame index
        gram09_3.tStart = t  # local t and not account for scr refresh
        gram09_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram09_3, 'tStartRefresh')  # time at next scr refresh
        gram09_3.setAutoDraw(True)
    
    # *gram10_3* updates
    if gram10_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram10_3.frameNStart = frameN  # exact frame index
        gram10_3.tStart = t  # local t and not account for scr refresh
        gram10_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram10_3, 'tStartRefresh')  # time at next scr refresh
        gram10_3.setAutoDraw(True)
    
    # *gram11_3* updates
    if gram11_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram11_3.frameNStart = frameN  # exact frame index
        gram11_3.tStart = t  # local t and not account for scr refresh
        gram11_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram11_3, 'tStartRefresh')  # time at next scr refresh
        gram11_3.setAutoDraw(True)
    
    # *gram12_3* updates
    if gram12_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram12_3.frameNStart = frameN  # exact frame index
        gram12_3.tStart = t  # local t and not account for scr refresh
        gram12_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram12_3, 'tStartRefresh')  # time at next scr refresh
        gram12_3.setAutoDraw(True)
    
    # *easy_succ_3* updates
    if easy_succ_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        easy_succ_3.frameNStart = frameN  # exact frame index
        easy_succ_3.tStart = t  # local t and not account for scr refresh
        easy_succ_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(easy_succ_3, 'tStartRefresh')  # time at next scr refresh
        easy_succ_3.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial_3"-------
for thisComponent in trial_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('one_3.started', one_3.tStartRefresh)
thisExp.addData('one_3.stopped', one_3.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = mouse_5.getPos()
buttons = mouse_5.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    for obj in [continue_text, easy_succ_3]:
        if obj.contains(mouse_5):
            gotValidClick = True
            mouse_5.clicked_name.append(obj.name)
thisExp.addData('mouse_5.x', x)
thisExp.addData('mouse_5.y', y)
thisExp.addData('mouse_5.leftButton', buttons[0])
thisExp.addData('mouse_5.midButton', buttons[1])
thisExp.addData('mouse_5.rightButton', buttons[2])
if len(mouse_5.clicked_name):
    thisExp.addData('mouse_5.clicked_name', mouse_5.clicked_name[0])
thisExp.addData('mouse_5.started', mouse_5.tStart)
thisExp.addData('mouse_5.stopped', mouse_5.tStop)
thisExp.nextEntry()
thisExp.addData('two_3.started', two_3.tStartRefresh)
thisExp.addData('two_3.stopped', two_3.tStopRefresh)
thisExp.addData('three_3.started', three_3.tStartRefresh)
thisExp.addData('three_3.stopped', three_3.tStopRefresh)
thisExp.addData('seven_3.started', seven_3.tStartRefresh)
thisExp.addData('seven_3.stopped', seven_3.tStopRefresh)
thisExp.addData('eight_3.started', eight_3.tStartRefresh)
thisExp.addData('eight_3.stopped', eight_3.tStopRefresh)
thisExp.addData('nine_3.started', nine_3.tStartRefresh)
thisExp.addData('nine_3.stopped', nine_3.tStopRefresh)
thisExp.addData('four_3.started', four_3.tStartRefresh)
thisExp.addData('four_3.stopped', four_3.tStopRefresh)
thisExp.addData('five_3.started', five_3.tStartRefresh)
thisExp.addData('five_3.stopped', five_3.tStopRefresh)
thisExp.addData('six_3.started', six_3.tStartRefresh)
thisExp.addData('six_3.stopped', six_3.tStopRefresh)
thisExp.addData('ten_3.started', ten_3.tStartRefresh)
thisExp.addData('ten_3.stopped', ten_3.tStopRefresh)
thisExp.addData('eleven_3.started', eleven_3.tStartRefresh)
thisExp.addData('eleven_3.stopped', eleven_3.tStopRefresh)
thisExp.addData('twelve_3.started', twelve_3.tStartRefresh)
thisExp.addData('twelve_3.stopped', twelve_3.tStopRefresh)
thisExp.addData('gram01_3.started', gram01_3.tStartRefresh)
thisExp.addData('gram01_3.stopped', gram01_3.tStopRefresh)
thisExp.addData('gram02_3.started', gram02_3.tStartRefresh)
thisExp.addData('gram02_3.stopped', gram02_3.tStopRefresh)
thisExp.addData('gram03_3.started', gram03_3.tStartRefresh)
thisExp.addData('gram03_3.stopped', gram03_3.tStopRefresh)
thisExp.addData('gram04_3.started', gram04_3.tStartRefresh)
thisExp.addData('gram04_3.stopped', gram04_3.tStopRefresh)
thisExp.addData('gram05_3.started', gram05_3.tStartRefresh)
thisExp.addData('gram05_3.stopped', gram05_3.tStopRefresh)
thisExp.addData('gram06_3.started', gram06_3.tStartRefresh)
thisExp.addData('gram06_3.stopped', gram06_3.tStopRefresh)
thisExp.addData('gram07_3.started', gram07_3.tStartRefresh)
thisExp.addData('gram07_3.stopped', gram07_3.tStopRefresh)
thisExp.addData('gram08_3.started', gram08_3.tStartRefresh)
thisExp.addData('gram08_3.stopped', gram08_3.tStopRefresh)
thisExp.addData('gram09_3.started', gram09_3.tStartRefresh)
thisExp.addData('gram09_3.stopped', gram09_3.tStopRefresh)
thisExp.addData('gram10_3.started', gram10_3.tStartRefresh)
thisExp.addData('gram10_3.stopped', gram10_3.tStopRefresh)
thisExp.addData('gram11_3.started', gram11_3.tStartRefresh)
thisExp.addData('gram11_3.stopped', gram11_3.tStopRefresh)
thisExp.addData('gram12_3.started', gram12_3.tStartRefresh)
thisExp.addData('gram12_3.stopped', gram12_3.tStopRefresh)
thisExp.addData('easy_succ_3.started', easy_succ_3.tStartRefresh)
thisExp.addData('easy_succ_3.stopped', easy_succ_3.tStopRefresh)
# the Routine "trial_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "call_exp1"-------
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
# keep track of which components have finished
call_exp1Components = [call_exp_text, key_resp]
for thisComponent in call_exp1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
call_exp1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "call_exp1"-------
while continueRoutine:
    # get current time
    t = call_exp1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=call_exp1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *call_exp_text* updates
    if call_exp_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        call_exp_text.frameNStart = frameN  # exact frame index
        call_exp_text.tStart = t  # local t and not account for scr refresh
        call_exp_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(call_exp_text, 'tStartRefresh')  # time at next scr refresh
        call_exp_text.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['y'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp.keys = theseKeys.name  # just the last key pressed
            key_resp.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in call_exp1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "call_exp1"-------
for thisComponent in call_exp1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('call_exp_text.started', call_exp_text.tStartRefresh)
thisExp.addData('call_exp_text.stopped', call_exp_text.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "call_exp1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "TIPI_instr"-------
# update component parameters for each repeat
continueButton = visual.ButtonStim(win, labelText= "Continue", pos=(.6, -.42))
# keep track of which components have finished
TIPI_instrComponents = [TIPI_txt]
for thisComponent in TIPI_instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
TIPI_instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "TIPI_instr"-------
while continueRoutine:
    # get current time
    t = TIPI_instrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=TIPI_instrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *TIPI_txt* updates
    if TIPI_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        TIPI_txt.frameNStart = frameN  # exact frame index
        TIPI_txt.tStart = t  # local t and not account for scr refresh
        TIPI_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(TIPI_txt, 'tStartRefresh')  # time at next scr refresh
        TIPI_txt.setAutoDraw(True)
    continueButton.draw()
    continueButton.buttonEnabled = True
    
    if continueButton.buttonSelected:
        continueRoutine = False
    
    
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in TIPI_instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "TIPI_instr"-------
for thisComponent in TIPI_instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('TIPI_txt.started', TIPI_txt.tStartRefresh)
thisExp.addData('TIPI_txt.stopped', TIPI_txt.tStopRefresh)
# the Routine "TIPI_instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "TIPI"-------
# update component parameters for each repeat
continueButton = visual.ButtonStim(win, labelText= "Continue", pos=(.35, -.4))
# keep track of which components have finished
TIPIComponents = [tipi_form, tipi_scale]
for thisComponent in TIPIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
TIPIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "TIPI"-------
while continueRoutine:
    # get current time
    t = TIPIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=TIPIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    tipi_form.draw()
    continueButton.draw()
    
    if tipi_form.formComplete():
        continueButton.buttonEnabled = True
        
    if continueButton.buttonSelected:
        continueRoutine = False
    
    # *tipi_scale* updates
    if tipi_scale.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        tipi_scale.frameNStart = frameN  # exact frame index
        tipi_scale.tStart = t  # local t and not account for scr refresh
        tipi_scale.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(tipi_scale, 'tStartRefresh')  # time at next scr refresh
        tipi_scale.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in TIPIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "TIPI"-------
for thisComponent in TIPIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
tipi_formData = tipi_form.getData()
while tipi_formData['questions']:
    for dataTypes in tipi_formData.keys():
        thisExp.addData(dataTypes, tipi_formData[dataTypes].popleft())
    thisExp.nextEntry()
thisExp.addData('tipi_scale.started', tipi_scale.tStartRefresh)
thisExp.addData('tipi_scale.stopped', tipi_scale.tStopRefresh)
# the Routine "TIPI" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trial_4"-------
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_6
mouse_6.clicked_name = []
gotValidClick = False  # until a click is received
pieces = [gram13_4,gram14_4,gram15_4,gram16_4,gram17_4,gram18_4,gram19_4,gram20_4,gram21_4,gram22_4,gram23_4,gram24_4]
picked = []
movingPiece = None

    # this works, it keeps track of what trial it is
    # so in win_checker() add an if statement
        # if this_trial is specific trial
        # change what hitboxes takes in as its 2nd argument
        # depending on the winstate order


def win_checker()->bool:
    order = [hitbox_checker("one", gram20_4), 
                    hitbox_checker("two", gram16_4),
                    hitbox_checker("three", gram23_4),
                    hitbox_checker("four", gram14_4),
                    hitbox_checker("five", gram18_4),
                    hitbox_checker("six", gram24_4),
                    hitbox_checker("seven", gram19_4),
                    hitbox_checker("eight", gram22_4),
                    hitbox_checker("nine", gram13_4),
                    hitbox_checker("ten", gram17_4),
                    hitbox_checker("eleven", gram15_4),
                    hitbox_checker("twelve", gram21_4)]
    if all(order):
        return True

trial_time = []
# keep track of which components have finished
trial_4Components = [one_4, mouse_6, two_4, three_4, seven_4, eight_4, nine_4, four_4, five_4, six_4, ten_4, eleven_4, twelve_4, gram13_4, gram14_4, gram15_4, gram16_4, gram17_4, gram18_4, gram19_4, gram20_4, gram21_4, gram22_4, gram23_4, gram24_4, easy_succ_4]
for thisComponent in trial_4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial_4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "trial_4"-------
while continueRoutine:
    # get current time
    t = trial_4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial_4Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *one_4* updates
    if one_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        one_4.frameNStart = frameN  # exact frame index
        one_4.tStart = t  # local t and not account for scr refresh
        one_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(one_4, 'tStartRefresh')  # time at next scr refresh
        one_4.setAutoDraw(True)
    # *mouse_6* updates
    if mouse_6.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_6.frameNStart = frameN  # exact frame index
        mouse_6.tStart = t  # local t and not account for scr refresh
        mouse_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_6, 'tStartRefresh')  # time at next scr refresh
        mouse_6.status = STARTED
        mouse_6.mouseClock.reset()
        prevButtonState = mouse_6.getPressed()  # if button is down already this ISN'T a new click
    if mouse_6.status == STARTED:  # only update if started and not finished!
        buttons = mouse_6.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [continue_text, easy_succ]:
                    if obj.contains(mouse_6):
                        gotValidClick = True
                        mouse_6.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # *two_4* updates
    if two_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        two_4.frameNStart = frameN  # exact frame index
        two_4.tStart = t  # local t and not account for scr refresh
        two_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(two_4, 'tStartRefresh')  # time at next scr refresh
        two_4.setAutoDraw(True)
    
    # *three_4* updates
    if three_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        three_4.frameNStart = frameN  # exact frame index
        three_4.tStart = t  # local t and not account for scr refresh
        three_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(three_4, 'tStartRefresh')  # time at next scr refresh
        three_4.setAutoDraw(True)
    
    # *seven_4* updates
    if seven_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        seven_4.frameNStart = frameN  # exact frame index
        seven_4.tStart = t  # local t and not account for scr refresh
        seven_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(seven_4, 'tStartRefresh')  # time at next scr refresh
        seven_4.setAutoDraw(True)
    
    # *eight_4* updates
    if eight_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        eight_4.frameNStart = frameN  # exact frame index
        eight_4.tStart = t  # local t and not account for scr refresh
        eight_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(eight_4, 'tStartRefresh')  # time at next scr refresh
        eight_4.setAutoDraw(True)
    
    # *nine_4* updates
    if nine_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        nine_4.frameNStart = frameN  # exact frame index
        nine_4.tStart = t  # local t and not account for scr refresh
        nine_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(nine_4, 'tStartRefresh')  # time at next scr refresh
        nine_4.setAutoDraw(True)
    
    # *four_4* updates
    if four_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        four_4.frameNStart = frameN  # exact frame index
        four_4.tStart = t  # local t and not account for scr refresh
        four_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(four_4, 'tStartRefresh')  # time at next scr refresh
        four_4.setAutoDraw(True)
    
    # *five_4* updates
    if five_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        five_4.frameNStart = frameN  # exact frame index
        five_4.tStart = t  # local t and not account for scr refresh
        five_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(five_4, 'tStartRefresh')  # time at next scr refresh
        five_4.setAutoDraw(True)
    
    # *six_4* updates
    if six_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        six_4.frameNStart = frameN  # exact frame index
        six_4.tStart = t  # local t and not account for scr refresh
        six_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(six_4, 'tStartRefresh')  # time at next scr refresh
        six_4.setAutoDraw(True)
    
    # *ten_4* updates
    if ten_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ten_4.frameNStart = frameN  # exact frame index
        ten_4.tStart = t  # local t and not account for scr refresh
        ten_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ten_4, 'tStartRefresh')  # time at next scr refresh
        ten_4.setAutoDraw(True)
    
    # *eleven_4* updates
    if eleven_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        eleven_4.frameNStart = frameN  # exact frame index
        eleven_4.tStart = t  # local t and not account for scr refresh
        eleven_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(eleven_4, 'tStartRefresh')  # time at next scr refresh
        eleven_4.setAutoDraw(True)
    
    # *twelve_4* updates
    if twelve_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        twelve_4.frameNStart = frameN  # exact frame index
        twelve_4.tStart = t  # local t and not account for scr refresh
        twelve_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(twelve_4, 'tStartRefresh')  # time at next scr refresh
        twelve_4.setAutoDraw(True)
    for piece in pieces:
        if mouse.isPressedIn(piece) and movingPiece is None:
            picked.append(piece)
    
    movingPiece = movePicked(picked, mouse, movingPiece)
    
    gram01_xpos = gram01.pos[0]
    gram01_ypos = gram01.pos[1]
    
    win_state = False
    
    win_state = win_checker()
    
    continue_text = offscreen_continue() # move the continue off-screen so it can't be clicked.
    continue_text.draw()
    
    # in begin routine, create a function that will check if
    # all the tangrams are in the correct spot
    # if they are, then have it return true and draw continue_text
    
    if win_state:
        continue_text = win_continue()
        continue_text.draw()
        trial_time.append(trial_timer())
        trial_time[0].draw()
    else: 
        win.flip()
    
    
    #if mouse.isPressedIn(polygon):
    #    crosses.append(makeCross(mouse.getPos()))
    
    # *gram13_4* updates
    if gram13_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram13_4.frameNStart = frameN  # exact frame index
        gram13_4.tStart = t  # local t and not account for scr refresh
        gram13_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram13_4, 'tStartRefresh')  # time at next scr refresh
        gram13_4.setAutoDraw(True)
    
    # *gram14_4* updates
    if gram14_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram14_4.frameNStart = frameN  # exact frame index
        gram14_4.tStart = t  # local t and not account for scr refresh
        gram14_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram14_4, 'tStartRefresh')  # time at next scr refresh
        gram14_4.setAutoDraw(True)
    
    # *gram15_4* updates
    if gram15_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram15_4.frameNStart = frameN  # exact frame index
        gram15_4.tStart = t  # local t and not account for scr refresh
        gram15_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram15_4, 'tStartRefresh')  # time at next scr refresh
        gram15_4.setAutoDraw(True)
    
    # *gram16_4* updates
    if gram16_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram16_4.frameNStart = frameN  # exact frame index
        gram16_4.tStart = t  # local t and not account for scr refresh
        gram16_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram16_4, 'tStartRefresh')  # time at next scr refresh
        gram16_4.setAutoDraw(True)
    
    # *gram17_4* updates
    if gram17_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram17_4.frameNStart = frameN  # exact frame index
        gram17_4.tStart = t  # local t and not account for scr refresh
        gram17_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram17_4, 'tStartRefresh')  # time at next scr refresh
        gram17_4.setAutoDraw(True)
    
    # *gram18_4* updates
    if gram18_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram18_4.frameNStart = frameN  # exact frame index
        gram18_4.tStart = t  # local t and not account for scr refresh
        gram18_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram18_4, 'tStartRefresh')  # time at next scr refresh
        gram18_4.setAutoDraw(True)
    
    # *gram19_4* updates
    if gram19_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram19_4.frameNStart = frameN  # exact frame index
        gram19_4.tStart = t  # local t and not account for scr refresh
        gram19_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram19_4, 'tStartRefresh')  # time at next scr refresh
        gram19_4.setAutoDraw(True)
    
    # *gram20_4* updates
    if gram20_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram20_4.frameNStart = frameN  # exact frame index
        gram20_4.tStart = t  # local t and not account for scr refresh
        gram20_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram20_4, 'tStartRefresh')  # time at next scr refresh
        gram20_4.setAutoDraw(True)
    
    # *gram21_4* updates
    if gram21_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram21_4.frameNStart = frameN  # exact frame index
        gram21_4.tStart = t  # local t and not account for scr refresh
        gram21_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram21_4, 'tStartRefresh')  # time at next scr refresh
        gram21_4.setAutoDraw(True)
    
    # *gram22_4* updates
    if gram22_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram22_4.frameNStart = frameN  # exact frame index
        gram22_4.tStart = t  # local t and not account for scr refresh
        gram22_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram22_4, 'tStartRefresh')  # time at next scr refresh
        gram22_4.setAutoDraw(True)
    
    # *gram23_4* updates
    if gram23_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram23_4.frameNStart = frameN  # exact frame index
        gram23_4.tStart = t  # local t and not account for scr refresh
        gram23_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram23_4, 'tStartRefresh')  # time at next scr refresh
        gram23_4.setAutoDraw(True)
    
    # *gram24_4* updates
    if gram24_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram24_4.frameNStart = frameN  # exact frame index
        gram24_4.tStart = t  # local t and not account for scr refresh
        gram24_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram24_4, 'tStartRefresh')  # time at next scr refresh
        gram24_4.setAutoDraw(True)
    
    # *easy_succ_4* updates
    if easy_succ_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        easy_succ_4.frameNStart = frameN  # exact frame index
        easy_succ_4.tStart = t  # local t and not account for scr refresh
        easy_succ_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(easy_succ_4, 'tStartRefresh')  # time at next scr refresh
        easy_succ_4.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial_4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial_4"-------
for thisComponent in trial_4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('one_4.started', one_4.tStartRefresh)
thisExp.addData('one_4.stopped', one_4.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = mouse_6.getPos()
buttons = mouse_6.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    for obj in [continue_text, easy_succ]:
        if obj.contains(mouse_6):
            gotValidClick = True
            mouse_6.clicked_name.append(obj.name)
thisExp.addData('mouse_6.x', x)
thisExp.addData('mouse_6.y', y)
thisExp.addData('mouse_6.leftButton', buttons[0])
thisExp.addData('mouse_6.midButton', buttons[1])
thisExp.addData('mouse_6.rightButton', buttons[2])
if len(mouse_6.clicked_name):
    thisExp.addData('mouse_6.clicked_name', mouse_6.clicked_name[0])
thisExp.addData('mouse_6.started', mouse_6.tStart)
thisExp.addData('mouse_6.stopped', mouse_6.tStop)
thisExp.nextEntry()
thisExp.addData('two_4.started', two_4.tStartRefresh)
thisExp.addData('two_4.stopped', two_4.tStopRefresh)
thisExp.addData('three_4.started', three_4.tStartRefresh)
thisExp.addData('three_4.stopped', three_4.tStopRefresh)
thisExp.addData('seven_4.started', seven_4.tStartRefresh)
thisExp.addData('seven_4.stopped', seven_4.tStopRefresh)
thisExp.addData('eight_4.started', eight_4.tStartRefresh)
thisExp.addData('eight_4.stopped', eight_4.tStopRefresh)
thisExp.addData('nine_4.started', nine_4.tStartRefresh)
thisExp.addData('nine_4.stopped', nine_4.tStopRefresh)
thisExp.addData('four_4.started', four_4.tStartRefresh)
thisExp.addData('four_4.stopped', four_4.tStopRefresh)
thisExp.addData('five_4.started', five_4.tStartRefresh)
thisExp.addData('five_4.stopped', five_4.tStopRefresh)
thisExp.addData('six_4.started', six_4.tStartRefresh)
thisExp.addData('six_4.stopped', six_4.tStopRefresh)
thisExp.addData('ten_4.started', ten_4.tStartRefresh)
thisExp.addData('ten_4.stopped', ten_4.tStopRefresh)
thisExp.addData('eleven_4.started', eleven_4.tStartRefresh)
thisExp.addData('eleven_4.stopped', eleven_4.tStopRefresh)
thisExp.addData('twelve_4.started', twelve_4.tStartRefresh)
thisExp.addData('twelve_4.stopped', twelve_4.tStopRefresh)
thisExp.addData('gram13_4.started', gram13_4.tStartRefresh)
thisExp.addData('gram13_4.stopped', gram13_4.tStopRefresh)
thisExp.addData('gram14_4.started', gram14_4.tStartRefresh)
thisExp.addData('gram14_4.stopped', gram14_4.tStopRefresh)
thisExp.addData('gram15_4.started', gram15_4.tStartRefresh)
thisExp.addData('gram15_4.stopped', gram15_4.tStopRefresh)
thisExp.addData('gram16_4.started', gram16_4.tStartRefresh)
thisExp.addData('gram16_4.stopped', gram16_4.tStopRefresh)
thisExp.addData('gram17_4.started', gram17_4.tStartRefresh)
thisExp.addData('gram17_4.stopped', gram17_4.tStopRefresh)
thisExp.addData('gram18_4.started', gram18_4.tStartRefresh)
thisExp.addData('gram18_4.stopped', gram18_4.tStopRefresh)
thisExp.addData('gram19_4.started', gram19_4.tStartRefresh)
thisExp.addData('gram19_4.stopped', gram19_4.tStopRefresh)
thisExp.addData('gram20_4.started', gram20_4.tStartRefresh)
thisExp.addData('gram20_4.stopped', gram20_4.tStopRefresh)
thisExp.addData('gram21_4.started', gram21_4.tStartRefresh)
thisExp.addData('gram21_4.stopped', gram21_4.tStopRefresh)
thisExp.addData('gram22_4.started', gram22_4.tStartRefresh)
thisExp.addData('gram22_4.stopped', gram22_4.tStopRefresh)
thisExp.addData('gram23_4.started', gram23_4.tStartRefresh)
thisExp.addData('gram23_4.stopped', gram23_4.tStopRefresh)
thisExp.addData('gram24_4.started', gram24_4.tStartRefresh)
thisExp.addData('gram24_4.stopped', gram24_4.tStopRefresh)
thisExp.addData('easy_succ_4.started', easy_succ_4.tStartRefresh)
thisExp.addData('easy_succ_4.stopped', easy_succ_4.tStopRefresh)
# the Routine "trial_4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trial_5"-------
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_7
mouse_7.clicked_name = []
gotValidClick = False  # until a click is received
pieces = [gram13_5,gram14_5,gram15_5,gram16_5,gram17_5,gram18_5,gram19_5,gram20_5,gram21_5,gram22_5,gram23_5,gram24_5]
picked = []
movingPiece = None

    # this works, it keeps track of what trial it is
    # so in win_checker() add an if statement
        # if this_trial is specific trial
        # change what hitboxes takes in as its 2nd argument
        # depending on the winstate order


def win_checker()->bool:
    order = [hitbox_checker("one", gram21_5), 
                    hitbox_checker("two", gram23_5),
                    hitbox_checker("three", gram17_5),
                    hitbox_checker("four", gram22_5),
                    hitbox_checker("five", gram19_5),
                    hitbox_checker("six", gram18_5),
                    hitbox_checker("seven", gram20_5),
                    hitbox_checker("eight", gram15_5),
                    hitbox_checker("nine", gram14_5),
                    hitbox_checker("ten", gram16_5),
                    hitbox_checker("eleven", gram13_5),
                    hitbox_checker("twelve", gram24_5)]
    if all(order):
        return True

trial_time = []
# keep track of which components have finished
trial_5Components = [one_5, mouse_7, two_5, three_5, seven_5, eight_5, nine_5, four_5, five_5, six_5, ten_5, eleven_5, twelve_5, gram13_5, gram14_5, gram15_5, gram16_5, gram17_5, gram18_5, gram19_5, gram20_5, gram21_5, gram22_5, gram23_5, gram24_5, easy_succ_5]
for thisComponent in trial_5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial_5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "trial_5"-------
while continueRoutine:
    # get current time
    t = trial_5Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial_5Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *one_5* updates
    if one_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        one_5.frameNStart = frameN  # exact frame index
        one_5.tStart = t  # local t and not account for scr refresh
        one_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(one_5, 'tStartRefresh')  # time at next scr refresh
        one_5.setAutoDraw(True)
    # *mouse_7* updates
    if mouse_7.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_7.frameNStart = frameN  # exact frame index
        mouse_7.tStart = t  # local t and not account for scr refresh
        mouse_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_7, 'tStartRefresh')  # time at next scr refresh
        mouse_7.status = STARTED
        mouse_7.mouseClock.reset()
        prevButtonState = mouse_7.getPressed()  # if button is down already this ISN'T a new click
    if mouse_7.status == STARTED:  # only update if started and not finished!
        buttons = mouse_7.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [continue_text, easy_succ]:
                    if obj.contains(mouse_7):
                        gotValidClick = True
                        mouse_7.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # *two_5* updates
    if two_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        two_5.frameNStart = frameN  # exact frame index
        two_5.tStart = t  # local t and not account for scr refresh
        two_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(two_5, 'tStartRefresh')  # time at next scr refresh
        two_5.setAutoDraw(True)
    
    # *three_5* updates
    if three_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        three_5.frameNStart = frameN  # exact frame index
        three_5.tStart = t  # local t and not account for scr refresh
        three_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(three_5, 'tStartRefresh')  # time at next scr refresh
        three_5.setAutoDraw(True)
    
    # *seven_5* updates
    if seven_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        seven_5.frameNStart = frameN  # exact frame index
        seven_5.tStart = t  # local t and not account for scr refresh
        seven_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(seven_5, 'tStartRefresh')  # time at next scr refresh
        seven_5.setAutoDraw(True)
    
    # *eight_5* updates
    if eight_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        eight_5.frameNStart = frameN  # exact frame index
        eight_5.tStart = t  # local t and not account for scr refresh
        eight_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(eight_5, 'tStartRefresh')  # time at next scr refresh
        eight_5.setAutoDraw(True)
    
    # *nine_5* updates
    if nine_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        nine_5.frameNStart = frameN  # exact frame index
        nine_5.tStart = t  # local t and not account for scr refresh
        nine_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(nine_5, 'tStartRefresh')  # time at next scr refresh
        nine_5.setAutoDraw(True)
    
    # *four_5* updates
    if four_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        four_5.frameNStart = frameN  # exact frame index
        four_5.tStart = t  # local t and not account for scr refresh
        four_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(four_5, 'tStartRefresh')  # time at next scr refresh
        four_5.setAutoDraw(True)
    
    # *five_5* updates
    if five_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        five_5.frameNStart = frameN  # exact frame index
        five_5.tStart = t  # local t and not account for scr refresh
        five_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(five_5, 'tStartRefresh')  # time at next scr refresh
        five_5.setAutoDraw(True)
    
    # *six_5* updates
    if six_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        six_5.frameNStart = frameN  # exact frame index
        six_5.tStart = t  # local t and not account for scr refresh
        six_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(six_5, 'tStartRefresh')  # time at next scr refresh
        six_5.setAutoDraw(True)
    
    # *ten_5* updates
    if ten_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ten_5.frameNStart = frameN  # exact frame index
        ten_5.tStart = t  # local t and not account for scr refresh
        ten_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ten_5, 'tStartRefresh')  # time at next scr refresh
        ten_5.setAutoDraw(True)
    
    # *eleven_5* updates
    if eleven_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        eleven_5.frameNStart = frameN  # exact frame index
        eleven_5.tStart = t  # local t and not account for scr refresh
        eleven_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(eleven_5, 'tStartRefresh')  # time at next scr refresh
        eleven_5.setAutoDraw(True)
    
    # *twelve_5* updates
    if twelve_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        twelve_5.frameNStart = frameN  # exact frame index
        twelve_5.tStart = t  # local t and not account for scr refresh
        twelve_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(twelve_5, 'tStartRefresh')  # time at next scr refresh
        twelve_5.setAutoDraw(True)
    for piece in pieces:
        if mouse.isPressedIn(piece) and movingPiece is None:
            picked.append(piece)
    
    movingPiece = movePicked(picked, mouse, movingPiece)
    
    gram01_xpos = gram01.pos[0]
    gram01_ypos = gram01.pos[1]
    
    win_state = False
    
    win_state = win_checker()
    
    continue_text = offscreen_continue() # move the continue off-screen so it can't be clicked.
    continue_text.draw()
    
    # in begin routine, create a function that will check if
    # all the tangrams are in the correct spot
    # if they are, then have it return true and draw continue_text
    
    if win_state:
        continue_text = win_continue()
        continue_text.draw()
        trial_time.append(trial_timer())
        trial_time[0].draw()
    else: 
        win.flip()
    
    
    #if mouse.isPressedIn(polygon):
    #    crosses.append(makeCross(mouse.getPos()))
    
    # *gram13_5* updates
    if gram13_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram13_5.frameNStart = frameN  # exact frame index
        gram13_5.tStart = t  # local t and not account for scr refresh
        gram13_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram13_5, 'tStartRefresh')  # time at next scr refresh
        gram13_5.setAutoDraw(True)
    
    # *gram14_5* updates
    if gram14_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram14_5.frameNStart = frameN  # exact frame index
        gram14_5.tStart = t  # local t and not account for scr refresh
        gram14_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram14_5, 'tStartRefresh')  # time at next scr refresh
        gram14_5.setAutoDraw(True)
    
    # *gram15_5* updates
    if gram15_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram15_5.frameNStart = frameN  # exact frame index
        gram15_5.tStart = t  # local t and not account for scr refresh
        gram15_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram15_5, 'tStartRefresh')  # time at next scr refresh
        gram15_5.setAutoDraw(True)
    
    # *gram16_5* updates
    if gram16_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram16_5.frameNStart = frameN  # exact frame index
        gram16_5.tStart = t  # local t and not account for scr refresh
        gram16_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram16_5, 'tStartRefresh')  # time at next scr refresh
        gram16_5.setAutoDraw(True)
    
    # *gram17_5* updates
    if gram17_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram17_5.frameNStart = frameN  # exact frame index
        gram17_5.tStart = t  # local t and not account for scr refresh
        gram17_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram17_5, 'tStartRefresh')  # time at next scr refresh
        gram17_5.setAutoDraw(True)
    
    # *gram18_5* updates
    if gram18_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram18_5.frameNStart = frameN  # exact frame index
        gram18_5.tStart = t  # local t and not account for scr refresh
        gram18_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram18_5, 'tStartRefresh')  # time at next scr refresh
        gram18_5.setAutoDraw(True)
    
    # *gram19_5* updates
    if gram19_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram19_5.frameNStart = frameN  # exact frame index
        gram19_5.tStart = t  # local t and not account for scr refresh
        gram19_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram19_5, 'tStartRefresh')  # time at next scr refresh
        gram19_5.setAutoDraw(True)
    
    # *gram20_5* updates
    if gram20_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram20_5.frameNStart = frameN  # exact frame index
        gram20_5.tStart = t  # local t and not account for scr refresh
        gram20_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram20_5, 'tStartRefresh')  # time at next scr refresh
        gram20_5.setAutoDraw(True)
    
    # *gram21_5* updates
    if gram21_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram21_5.frameNStart = frameN  # exact frame index
        gram21_5.tStart = t  # local t and not account for scr refresh
        gram21_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram21_5, 'tStartRefresh')  # time at next scr refresh
        gram21_5.setAutoDraw(True)
    
    # *gram22_5* updates
    if gram22_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram22_5.frameNStart = frameN  # exact frame index
        gram22_5.tStart = t  # local t and not account for scr refresh
        gram22_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram22_5, 'tStartRefresh')  # time at next scr refresh
        gram22_5.setAutoDraw(True)
    
    # *gram23_5* updates
    if gram23_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram23_5.frameNStart = frameN  # exact frame index
        gram23_5.tStart = t  # local t and not account for scr refresh
        gram23_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram23_5, 'tStartRefresh')  # time at next scr refresh
        gram23_5.setAutoDraw(True)
    
    # *gram24_5* updates
    if gram24_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram24_5.frameNStart = frameN  # exact frame index
        gram24_5.tStart = t  # local t and not account for scr refresh
        gram24_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram24_5, 'tStartRefresh')  # time at next scr refresh
        gram24_5.setAutoDraw(True)
    
    # *easy_succ_5* updates
    if easy_succ_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        easy_succ_5.frameNStart = frameN  # exact frame index
        easy_succ_5.tStart = t  # local t and not account for scr refresh
        easy_succ_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(easy_succ_5, 'tStartRefresh')  # time at next scr refresh
        easy_succ_5.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial_5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial_5"-------
for thisComponent in trial_5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('one_5.started', one_5.tStartRefresh)
thisExp.addData('one_5.stopped', one_5.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = mouse_7.getPos()
buttons = mouse_7.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    for obj in [continue_text, easy_succ]:
        if obj.contains(mouse_7):
            gotValidClick = True
            mouse_7.clicked_name.append(obj.name)
thisExp.addData('mouse_7.x', x)
thisExp.addData('mouse_7.y', y)
thisExp.addData('mouse_7.leftButton', buttons[0])
thisExp.addData('mouse_7.midButton', buttons[1])
thisExp.addData('mouse_7.rightButton', buttons[2])
if len(mouse_7.clicked_name):
    thisExp.addData('mouse_7.clicked_name', mouse_7.clicked_name[0])
thisExp.addData('mouse_7.started', mouse_7.tStart)
thisExp.addData('mouse_7.stopped', mouse_7.tStop)
thisExp.nextEntry()
thisExp.addData('two_5.started', two_5.tStartRefresh)
thisExp.addData('two_5.stopped', two_5.tStopRefresh)
thisExp.addData('three_5.started', three_5.tStartRefresh)
thisExp.addData('three_5.stopped', three_5.tStopRefresh)
thisExp.addData('seven_5.started', seven_5.tStartRefresh)
thisExp.addData('seven_5.stopped', seven_5.tStopRefresh)
thisExp.addData('eight_5.started', eight_5.tStartRefresh)
thisExp.addData('eight_5.stopped', eight_5.tStopRefresh)
thisExp.addData('nine_5.started', nine_5.tStartRefresh)
thisExp.addData('nine_5.stopped', nine_5.tStopRefresh)
thisExp.addData('four_5.started', four_5.tStartRefresh)
thisExp.addData('four_5.stopped', four_5.tStopRefresh)
thisExp.addData('five_5.started', five_5.tStartRefresh)
thisExp.addData('five_5.stopped', five_5.tStopRefresh)
thisExp.addData('six_5.started', six_5.tStartRefresh)
thisExp.addData('six_5.stopped', six_5.tStopRefresh)
thisExp.addData('ten_5.started', ten_5.tStartRefresh)
thisExp.addData('ten_5.stopped', ten_5.tStopRefresh)
thisExp.addData('eleven_5.started', eleven_5.tStartRefresh)
thisExp.addData('eleven_5.stopped', eleven_5.tStopRefresh)
thisExp.addData('twelve_5.started', twelve_5.tStartRefresh)
thisExp.addData('twelve_5.stopped', twelve_5.tStopRefresh)
thisExp.addData('gram13_5.started', gram13_5.tStartRefresh)
thisExp.addData('gram13_5.stopped', gram13_5.tStopRefresh)
thisExp.addData('gram14_5.started', gram14_5.tStartRefresh)
thisExp.addData('gram14_5.stopped', gram14_5.tStopRefresh)
thisExp.addData('gram15_5.started', gram15_5.tStartRefresh)
thisExp.addData('gram15_5.stopped', gram15_5.tStopRefresh)
thisExp.addData('gram16_5.started', gram16_5.tStartRefresh)
thisExp.addData('gram16_5.stopped', gram16_5.tStopRefresh)
thisExp.addData('gram17_5.started', gram17_5.tStartRefresh)
thisExp.addData('gram17_5.stopped', gram17_5.tStopRefresh)
thisExp.addData('gram18_5.started', gram18_5.tStartRefresh)
thisExp.addData('gram18_5.stopped', gram18_5.tStopRefresh)
thisExp.addData('gram19_5.started', gram19_5.tStartRefresh)
thisExp.addData('gram19_5.stopped', gram19_5.tStopRefresh)
thisExp.addData('gram20_5.started', gram20_5.tStartRefresh)
thisExp.addData('gram20_5.stopped', gram20_5.tStopRefresh)
thisExp.addData('gram21_5.started', gram21_5.tStartRefresh)
thisExp.addData('gram21_5.stopped', gram21_5.tStopRefresh)
thisExp.addData('gram22_5.started', gram22_5.tStartRefresh)
thisExp.addData('gram22_5.stopped', gram22_5.tStopRefresh)
thisExp.addData('gram23_5.started', gram23_5.tStartRefresh)
thisExp.addData('gram23_5.stopped', gram23_5.tStopRefresh)
thisExp.addData('gram24_5.started', gram24_5.tStartRefresh)
thisExp.addData('gram24_5.stopped', gram24_5.tStopRefresh)
thisExp.addData('easy_succ_5.started', easy_succ_5.tStartRefresh)
thisExp.addData('easy_succ_5.stopped', easy_succ_5.tStopRefresh)
# the Routine "trial_5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trial_6"-------
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_8
mouse_8.clicked_name = []
gotValidClick = False  # until a click is received
pieces = [gram13_6,gram14_6,gram15_6,gram16_6,gram17_6,gram18_6,gram19_6,gram20_6,gram21_6,gram22_6,gram23_6,gram24_6]
picked = []
movingPiece = None

    # this works, it keeps track of what trial it is
    # so in win_checker() add an if statement
        # if this_trial is specific trial
        # change what hitboxes takes in as its 2nd argument
        # depending on the winstate order


def win_checker()->bool:
    order = [hitbox_checker("one", gram17_6), 
                    hitbox_checker("two", gram14_6),
                    hitbox_checker("three", gram20_6),
                    hitbox_checker("four", gram22_6),
                    hitbox_checker("five", gram24_6),
                    hitbox_checker("six", gram21_6),
                    hitbox_checker("seven", gram19_6),
                    hitbox_checker("eight", gram16_6),
                    hitbox_checker("nine", gram13_6),
                    hitbox_checker("ten", gram15_6),
                    hitbox_checker("eleven", gram23_6),
                    hitbox_checker("twelve", gram18_6)]
    if all(order):
        return True

trial_time = []
# keep track of which components have finished
trial_6Components = [one_6, mouse_8, two_6, three_6, seven_6, eight_6, nine_6, four_6, five_6, six_6, ten_6, eleven_6, twelve_6, gram13_6, gram14_6, gram15_6, gram16_6, gram17_6, gram18_6, gram19_6, gram20_6, gram21_6, gram22_6, gram23_6, gram24_6, easy_succ_6]
for thisComponent in trial_6Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial_6Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "trial_6"-------
while continueRoutine:
    # get current time
    t = trial_6Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial_6Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *one_6* updates
    if one_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        one_6.frameNStart = frameN  # exact frame index
        one_6.tStart = t  # local t and not account for scr refresh
        one_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(one_6, 'tStartRefresh')  # time at next scr refresh
        one_6.setAutoDraw(True)
    # *mouse_8* updates
    if mouse_8.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_8.frameNStart = frameN  # exact frame index
        mouse_8.tStart = t  # local t and not account for scr refresh
        mouse_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_8, 'tStartRefresh')  # time at next scr refresh
        mouse_8.status = STARTED
        mouse_8.mouseClock.reset()
        prevButtonState = mouse_8.getPressed()  # if button is down already this ISN'T a new click
    if mouse_8.status == STARTED:  # only update if started and not finished!
        buttons = mouse_8.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [continue_text, easy_succ]:
                    if obj.contains(mouse_8):
                        gotValidClick = True
                        mouse_8.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # *two_6* updates
    if two_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        two_6.frameNStart = frameN  # exact frame index
        two_6.tStart = t  # local t and not account for scr refresh
        two_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(two_6, 'tStartRefresh')  # time at next scr refresh
        two_6.setAutoDraw(True)
    
    # *three_6* updates
    if three_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        three_6.frameNStart = frameN  # exact frame index
        three_6.tStart = t  # local t and not account for scr refresh
        three_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(three_6, 'tStartRefresh')  # time at next scr refresh
        three_6.setAutoDraw(True)
    
    # *seven_6* updates
    if seven_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        seven_6.frameNStart = frameN  # exact frame index
        seven_6.tStart = t  # local t and not account for scr refresh
        seven_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(seven_6, 'tStartRefresh')  # time at next scr refresh
        seven_6.setAutoDraw(True)
    
    # *eight_6* updates
    if eight_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        eight_6.frameNStart = frameN  # exact frame index
        eight_6.tStart = t  # local t and not account for scr refresh
        eight_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(eight_6, 'tStartRefresh')  # time at next scr refresh
        eight_6.setAutoDraw(True)
    
    # *nine_6* updates
    if nine_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        nine_6.frameNStart = frameN  # exact frame index
        nine_6.tStart = t  # local t and not account for scr refresh
        nine_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(nine_6, 'tStartRefresh')  # time at next scr refresh
        nine_6.setAutoDraw(True)
    
    # *four_6* updates
    if four_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        four_6.frameNStart = frameN  # exact frame index
        four_6.tStart = t  # local t and not account for scr refresh
        four_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(four_6, 'tStartRefresh')  # time at next scr refresh
        four_6.setAutoDraw(True)
    
    # *five_6* updates
    if five_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        five_6.frameNStart = frameN  # exact frame index
        five_6.tStart = t  # local t and not account for scr refresh
        five_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(five_6, 'tStartRefresh')  # time at next scr refresh
        five_6.setAutoDraw(True)
    
    # *six_6* updates
    if six_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        six_6.frameNStart = frameN  # exact frame index
        six_6.tStart = t  # local t and not account for scr refresh
        six_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(six_6, 'tStartRefresh')  # time at next scr refresh
        six_6.setAutoDraw(True)
    
    # *ten_6* updates
    if ten_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ten_6.frameNStart = frameN  # exact frame index
        ten_6.tStart = t  # local t and not account for scr refresh
        ten_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ten_6, 'tStartRefresh')  # time at next scr refresh
        ten_6.setAutoDraw(True)
    
    # *eleven_6* updates
    if eleven_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        eleven_6.frameNStart = frameN  # exact frame index
        eleven_6.tStart = t  # local t and not account for scr refresh
        eleven_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(eleven_6, 'tStartRefresh')  # time at next scr refresh
        eleven_6.setAutoDraw(True)
    
    # *twelve_6* updates
    if twelve_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        twelve_6.frameNStart = frameN  # exact frame index
        twelve_6.tStart = t  # local t and not account for scr refresh
        twelve_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(twelve_6, 'tStartRefresh')  # time at next scr refresh
        twelve_6.setAutoDraw(True)
    for piece in pieces:
        if mouse.isPressedIn(piece) and movingPiece is None:
            picked.append(piece)
    
    movingPiece = movePicked(picked, mouse, movingPiece)
    
    gram01_xpos = gram01.pos[0]
    gram01_ypos = gram01.pos[1]
    
    win_state = False
    
    win_state = win_checker()
    
    continue_text = offscreen_continue() # move the continue off-screen so it can't be clicked.
    continue_text.draw()

    # in begin routine, create a function that will check if
    # all the tangrams are in the correct spot
    # if they are, then have it return true and draw continue_text
    
    if win_state:
        continue_text = win_continue()
        continue_text.draw()
        trial_time.append(trial_timer())
        trial_time[0].draw()
    else: 
        win.flip()
    
    
    #if mouse.isPressedIn(polygon):
    #    crosses.append(makeCross(mouse.getPos()))
    
    # *gram13_6* updates
    if gram13_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram13_6.frameNStart = frameN  # exact frame index
        gram13_6.tStart = t  # local t and not account for scr refresh
        gram13_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram13_6, 'tStartRefresh')  # time at next scr refresh
        gram13_6.setAutoDraw(True)
    
    # *gram14_6* updates
    if gram14_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram14_6.frameNStart = frameN  # exact frame index
        gram14_6.tStart = t  # local t and not account for scr refresh
        gram14_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram14_6, 'tStartRefresh')  # time at next scr refresh
        gram14_6.setAutoDraw(True)
    
    # *gram15_6* updates
    if gram15_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram15_6.frameNStart = frameN  # exact frame index
        gram15_6.tStart = t  # local t and not account for scr refresh
        gram15_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram15_6, 'tStartRefresh')  # time at next scr refresh
        gram15_6.setAutoDraw(True)
    
    # *gram16_6* updates
    if gram16_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram16_6.frameNStart = frameN  # exact frame index
        gram16_6.tStart = t  # local t and not account for scr refresh
        gram16_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram16_6, 'tStartRefresh')  # time at next scr refresh
        gram16_6.setAutoDraw(True)
    
    # *gram17_6* updates
    if gram17_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram17_6.frameNStart = frameN  # exact frame index
        gram17_6.tStart = t  # local t and not account for scr refresh
        gram17_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram17_6, 'tStartRefresh')  # time at next scr refresh
        gram17_6.setAutoDraw(True)
    
    # *gram18_6* updates
    if gram18_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram18_6.frameNStart = frameN  # exact frame index
        gram18_6.tStart = t  # local t and not account for scr refresh
        gram18_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram18_6, 'tStartRefresh')  # time at next scr refresh
        gram18_6.setAutoDraw(True)
    
    # *gram19_6* updates
    if gram19_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram19_6.frameNStart = frameN  # exact frame index
        gram19_6.tStart = t  # local t and not account for scr refresh
        gram19_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram19_6, 'tStartRefresh')  # time at next scr refresh
        gram19_6.setAutoDraw(True)
    
    # *gram20_6* updates
    if gram20_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram20_6.frameNStart = frameN  # exact frame index
        gram20_6.tStart = t  # local t and not account for scr refresh
        gram20_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram20_6, 'tStartRefresh')  # time at next scr refresh
        gram20_6.setAutoDraw(True)
    
    # *gram21_6* updates
    if gram21_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram21_6.frameNStart = frameN  # exact frame index
        gram21_6.tStart = t  # local t and not account for scr refresh
        gram21_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram21_6, 'tStartRefresh')  # time at next scr refresh
        gram21_6.setAutoDraw(True)
    
    # *gram22_6* updates
    if gram22_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram22_6.frameNStart = frameN  # exact frame index
        gram22_6.tStart = t  # local t and not account for scr refresh
        gram22_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram22_6, 'tStartRefresh')  # time at next scr refresh
        gram22_6.setAutoDraw(True)
    
    # *gram23_6* updates
    if gram23_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram23_6.frameNStart = frameN  # exact frame index
        gram23_6.tStart = t  # local t and not account for scr refresh
        gram23_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram23_6, 'tStartRefresh')  # time at next scr refresh
        gram23_6.setAutoDraw(True)
    
    # *gram24_6* updates
    if gram24_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram24_6.frameNStart = frameN  # exact frame index
        gram24_6.tStart = t  # local t and not account for scr refresh
        gram24_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram24_6, 'tStartRefresh')  # time at next scr refresh
        gram24_6.setAutoDraw(True)
    
    # *easy_succ_6* updates
    if easy_succ_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        easy_succ_6.frameNStart = frameN  # exact frame index
        easy_succ_6.tStart = t  # local t and not account for scr refresh
        easy_succ_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(easy_succ_6, 'tStartRefresh')  # time at next scr refresh
        easy_succ_6.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial_6Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial_6"-------
for thisComponent in trial_6Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('one_6.started', one_6.tStartRefresh)
thisExp.addData('one_6.stopped', one_6.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = mouse_8.getPos()
buttons = mouse_8.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    for obj in [continue_text, easy_succ]:
        if obj.contains(mouse_8):
            gotValidClick = True
            mouse_8.clicked_name.append(obj.name)
thisExp.addData('mouse_8.x', x)
thisExp.addData('mouse_8.y', y)
thisExp.addData('mouse_8.leftButton', buttons[0])
thisExp.addData('mouse_8.midButton', buttons[1])
thisExp.addData('mouse_8.rightButton', buttons[2])
if len(mouse_8.clicked_name):
    thisExp.addData('mouse_8.clicked_name', mouse_8.clicked_name[0])
thisExp.addData('mouse_8.started', mouse_8.tStart)
thisExp.addData('mouse_8.stopped', mouse_8.tStop)
thisExp.nextEntry()
thisExp.addData('two_6.started', two_6.tStartRefresh)
thisExp.addData('two_6.stopped', two_6.tStopRefresh)
thisExp.addData('three_6.started', three_6.tStartRefresh)
thisExp.addData('three_6.stopped', three_6.tStopRefresh)
thisExp.addData('seven_6.started', seven_6.tStartRefresh)
thisExp.addData('seven_6.stopped', seven_6.tStopRefresh)
thisExp.addData('eight_6.started', eight_6.tStartRefresh)
thisExp.addData('eight_6.stopped', eight_6.tStopRefresh)
thisExp.addData('nine_6.started', nine_6.tStartRefresh)
thisExp.addData('nine_6.stopped', nine_6.tStopRefresh)
thisExp.addData('four_6.started', four_6.tStartRefresh)
thisExp.addData('four_6.stopped', four_6.tStopRefresh)
thisExp.addData('five_6.started', five_6.tStartRefresh)
thisExp.addData('five_6.stopped', five_6.tStopRefresh)
thisExp.addData('six_6.started', six_6.tStartRefresh)
thisExp.addData('six_6.stopped', six_6.tStopRefresh)
thisExp.addData('ten_6.started', ten_6.tStartRefresh)
thisExp.addData('ten_6.stopped', ten_6.tStopRefresh)
thisExp.addData('eleven_6.started', eleven_6.tStartRefresh)
thisExp.addData('eleven_6.stopped', eleven_6.tStopRefresh)
thisExp.addData('twelve_6.started', twelve_6.tStartRefresh)
thisExp.addData('twelve_6.stopped', twelve_6.tStopRefresh)
thisExp.addData('gram13_6.started', gram13_6.tStartRefresh)
thisExp.addData('gram13_6.stopped', gram13_6.tStopRefresh)
thisExp.addData('gram14_6.started', gram14_6.tStartRefresh)
thisExp.addData('gram14_6.stopped', gram14_6.tStopRefresh)
thisExp.addData('gram15_6.started', gram15_6.tStartRefresh)
thisExp.addData('gram15_6.stopped', gram15_6.tStopRefresh)
thisExp.addData('gram16_6.started', gram16_6.tStartRefresh)
thisExp.addData('gram16_6.stopped', gram16_6.tStopRefresh)
thisExp.addData('gram17_6.started', gram17_6.tStartRefresh)
thisExp.addData('gram17_6.stopped', gram17_6.tStopRefresh)
thisExp.addData('gram18_6.started', gram18_6.tStartRefresh)
thisExp.addData('gram18_6.stopped', gram18_6.tStopRefresh)
thisExp.addData('gram19_6.started', gram19_6.tStartRefresh)
thisExp.addData('gram19_6.stopped', gram19_6.tStopRefresh)
thisExp.addData('gram20_6.started', gram20_6.tStartRefresh)
thisExp.addData('gram20_6.stopped', gram20_6.tStopRefresh)
thisExp.addData('gram21_6.started', gram21_6.tStartRefresh)
thisExp.addData('gram21_6.stopped', gram21_6.tStopRefresh)
thisExp.addData('gram22_6.started', gram22_6.tStartRefresh)
thisExp.addData('gram22_6.stopped', gram22_6.tStopRefresh)
thisExp.addData('gram23_6.started', gram23_6.tStartRefresh)
thisExp.addData('gram23_6.stopped', gram23_6.tStopRefresh)
thisExp.addData('gram24_6.started', gram24_6.tStartRefresh)
thisExp.addData('gram24_6.stopped', gram24_6.tStopRefresh)
thisExp.addData('easy_succ_6.started', easy_succ_6.tStartRefresh)
thisExp.addData('easy_succ_6.stopped', easy_succ_6.tStopRefresh)
# the Routine "trial_6" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "call_exp2"-------
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
# keep track of which components have finished
call_exp2Components = [call_exp_text2, key_resp_2]
for thisComponent in call_exp2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
call_exp2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "call_exp2"-------
while continueRoutine:
    # get current time
    t = call_exp2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=call_exp2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *call_exp_text2* updates
    if call_exp_text2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        call_exp_text2.frameNStart = frameN  # exact frame index
        call_exp_text2.tStart = t  # local t and not account for scr refresh
        call_exp_text2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(call_exp_text2, 'tStartRefresh')  # time at next scr refresh
        call_exp_text2.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['y'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_2.keys = theseKeys.name  # just the last key pressed
            key_resp_2.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in call_exp2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "call_exp2"-------
for thisComponent in call_exp2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('call_exp_text2.started', call_exp_text2.tStartRefresh)
thisExp.addData('call_exp_text2.stopped', call_exp_text2.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "call_exp2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
