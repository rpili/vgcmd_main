#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on November 06, 2019, at 15:07
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

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'tg_dr_set2'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\rjpil\\OneDrive\\GS\\CECLAB\\vgcmd_main\\tg_dr_set2.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor="ryan's windows acer", color=[0,0,0], colorSpace='rgb',
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
    text="Instructions\n \nOn each trial you will see 12 shapes called tangrams. You will complete 6 trials. \n\nYour tangrams are in the correct order.\n\nYour partner's screen presents the same tangrams in an incorrect order. \n\nYou must work together to help your partner match your correct tangram order.",
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

# Initialize components for Routine "trial_4_answer"
trial_4_answerClock = core.Clock()
one_10 = visual.ImageStim(
    win=win,
    name='one_10', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/one.png', mask=None,
    ori=0, pos=(-.70, .30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
mouse_12 = event.Mouse(win=win)
x, y = [None, None]
mouse_12.mouseClock = core.Clock()
two_10 = visual.ImageStim(
    win=win,
    name='two_10', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/two.png', mask=None,
    ori=0, pos=(-.45, .30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
three_10 = visual.ImageStim(
    win=win,
    name='three_10', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/three.png', mask=None,
    ori=0, pos=(-0.20, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
seven_10 = visual.ImageStim(
    win=win,
    name='seven_10', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/seven.png', mask=None,
    ori=0, pos=(-0.70, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
eight_10 = visual.ImageStim(
    win=win,
    name='eight_10', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/eight.png', mask=None,
    ori=0, pos=(-0.45, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
nine_10 = visual.ImageStim(
    win=win,
    name='nine_10', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/nine.png', mask=None,
    ori=0, pos=(-0.20, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
four_10 = visual.ImageStim(
    win=win,
    name='four_10', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/four.png', mask=None,
    ori=0, pos=(0.20, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
five_10 = visual.ImageStim(
    win=win,
    name='five_10', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/five.png', mask=None,
    ori=0, pos=(0.45, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
six_10 = visual.ImageStim(
    win=win,
    name='six_10', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/six.png', mask=None,
    ori=0, pos=(0.70, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)
ten_10 = visual.ImageStim(
    win=win,
    name='ten_10', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/ten.png', mask=None,
    ori=0, pos=(0.20, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)
eleven_10 = visual.ImageStim(
    win=win,
    name='eleven_10', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/eleven.png', mask=None,
    ori=0, pos=(0.45, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)
twelve_10 = visual.ImageStim(
    win=win,
    name='twelve_10', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/twelve.png', mask=None,
    ori=0, pos=(0.70, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-12.0)
import pathlib

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


    
def continue_instr():
    continue_instr = visual.TextStim(win=win, name='continue_instr',
    text="Only Press Continue When Your Partner Is Ready",
    font='Arial',
    pos=(0.46, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0)
    return continue_instr



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
gram13 = visual.ImageStim(
    win=win,
    name='gram13', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram13.png', mask=None,
    ori=0, pos=(-0.2, -0.3), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-14.0)
gram14 = visual.ImageStim(
    win=win,
    name='gram14', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram14.png', mask=None,
    ori=0, pos=(0.2, 0.3), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-15.0)
gram15 = visual.ImageStim(
    win=win,
    name='gram15', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram15.png', mask=None,
    ori=0, pos=(0.45, -0.3), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-16.0)
gram16 = visual.ImageStim(
    win=win,
    name='gram16', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram16.png', mask=None,
    ori=0, pos=(-0.45, 0.3), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-17.0)
gram17 = visual.ImageStim(
    win=win,
    name='gram17', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram17.png', mask=None,
    ori=0, pos=(0.2, -0.3), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-18.0)
gram18 = visual.ImageStim(
    win=win,
    name='gram18', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram18.png', mask=None,
    ori=0, pos=(0.45, 0.3), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-19.0)
gram19 = visual.ImageStim(
    win=win,
    name='gram19', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram19.png', mask=None,
    ori=0, pos=(-0.7, -0.3), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-20.0)
gram20 = visual.ImageStim(
    win=win,
    name='gram20', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram20.png', mask=None,
    ori=0, pos=(-0.7, 0.3), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-21.0)
gram21 = visual.ImageStim(
    win=win,
    name='gram21', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram21.png', mask=None,
    ori=0, pos=(0.7, -0.3), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-22.0)
gram22 = visual.ImageStim(
    win=win,
    name='gram22', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram22.png', mask=None,
    ori=0, pos=(-0.45, -0.3), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-23.0)
gram23 = visual.ImageStim(
    win=win,
    name='gram23', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram23.png', mask=None,
    ori=0, pos=(-0.2, 0.3), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-24.0)
gram24 = visual.ImageStim(
    win=win,
    name='gram24', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram24.png', mask=None,
    ori=0, pos=(0.7, 0.3), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-25.0)

# Initialize components for Routine "trial_5_answer"
trial_5_answerClock = core.Clock()
one_11 = visual.ImageStim(
    win=win,
    name='one_11', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/one.png', mask=None,
    ori=0, pos=(-.70, .30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
mouse_13 = event.Mouse(win=win)
x, y = [None, None]
mouse_13.mouseClock = core.Clock()
two_11 = visual.ImageStim(
    win=win,
    name='two_11', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/two.png', mask=None,
    ori=0, pos=(-.45, .30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
three_11 = visual.ImageStim(
    win=win,
    name='three_11', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/three.png', mask=None,
    ori=0, pos=(-0.20, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
seven_11 = visual.ImageStim(
    win=win,
    name='seven_11', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/seven.png', mask=None,
    ori=0, pos=(-0.70, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
eight_11 = visual.ImageStim(
    win=win,
    name='eight_11', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/eight.png', mask=None,
    ori=0, pos=(-0.45, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
nine_11 = visual.ImageStim(
    win=win,
    name='nine_11', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/nine.png', mask=None,
    ori=0, pos=(-0.20, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
four_11 = visual.ImageStim(
    win=win,
    name='four_11', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/four.png', mask=None,
    ori=0, pos=(0.20, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
five_11 = visual.ImageStim(
    win=win,
    name='five_11', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/five.png', mask=None,
    ori=0, pos=(0.45, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
six_11 = visual.ImageStim(
    win=win,
    name='six_11', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/six.png', mask=None,
    ori=0, pos=(0.70, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)
ten_11 = visual.ImageStim(
    win=win,
    name='ten_11', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/ten.png', mask=None,
    ori=0, pos=(0.20, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)
eleven_11 = visual.ImageStim(
    win=win,
    name='eleven_11', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/eleven.png', mask=None,
    ori=0, pos=(0.45, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)
twelve_11 = visual.ImageStim(
    win=win,
    name='twelve_11', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/twelve.png', mask=None,
    ori=0, pos=(0.70, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-12.0)
import pathlib

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
gram13_7 = visual.ImageStim(
    win=win,
    name='gram13_7', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram13.png', mask=None,
    ori=0, pos=(0.45, -0.3), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-14.0)
gram14_7 = visual.ImageStim(
    win=win,
    name='gram14_7', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram14.png', mask=None,
    ori=0, pos=(-0.2, -0.3), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-15.0)
gram15_7 = visual.ImageStim(
    win=win,
    name='gram15_7', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram15.png', mask=None,
    ori=0, pos=(-0.45, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-16.0)
gram16_7 = visual.ImageStim(
    win=win,
    name='gram16_7', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram16.png', mask=None,
    ori=0, pos=(0.2, -0.3), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-17.0)
gram17_7 = visual.ImageStim(
    win=win,
    name='gram17_7', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram17.png', mask=None,
    ori=0, pos=(-0.2, 0.3), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-18.0)
gram18_7 = visual.ImageStim(
    win=win,
    name='gram18_7', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram18.png', mask=None,
    ori=0, pos=(0.7, 0.3), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-19.0)
gram19_7 = visual.ImageStim(
    win=win,
    name='gram19_7', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram19.png', mask=None,
    ori=0, pos=(0.45, 0.3), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-20.0)
gram20_7 = visual.ImageStim(
    win=win,
    name='gram20_7', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram20.png', mask=None,
    ori=0, pos=(-0.7, -0.3), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-21.0)
gram21_7 = visual.ImageStim(
    win=win,
    name='gram21_7', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram21.png', mask=None,
    ori=0, pos=(-0.7, 0.3), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-22.0)
gram22_7 = visual.ImageStim(
    win=win,
    name='gram22_7', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram22.png', mask=None,
    ori=0, pos=(0.2, 0.3), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-23.0)
gram23_7 = visual.ImageStim(
    win=win,
    name='gram23_7', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram23.png', mask=None,
    ori=0, pos=(-0.45, 0.3), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-24.0)
gram24_7 = visual.ImageStim(
    win=win,
    name='gram24_7', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram24.png', mask=None,
    ori=0, pos=(0.7, -0.3), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-25.0)

# Initialize components for Routine "trial_6_answer"
trial_6_answerClock = core.Clock()
one_12 = visual.ImageStim(
    win=win,
    name='one_12', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/one.png', mask=None,
    ori=0, pos=(-.70, .30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
mouse_14 = event.Mouse(win=win)
x, y = [None, None]
mouse_14.mouseClock = core.Clock()
two_12 = visual.ImageStim(
    win=win,
    name='two_12', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/two.png', mask=None,
    ori=0, pos=(-.45, .30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
three_12 = visual.ImageStim(
    win=win,
    name='three_12', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/three.png', mask=None,
    ori=0, pos=(-0.20, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
seven_12 = visual.ImageStim(
    win=win,
    name='seven_12', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/seven.png', mask=None,
    ori=0, pos=(-0.70, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
eight_12 = visual.ImageStim(
    win=win,
    name='eight_12', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/eight.png', mask=None,
    ori=0, pos=(-0.45, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
nine_12 = visual.ImageStim(
    win=win,
    name='nine_12', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/nine.png', mask=None,
    ori=0, pos=(-0.20, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
four_12 = visual.ImageStim(
    win=win,
    name='four_12', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/four.png', mask=None,
    ori=0, pos=(0.20, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
five_12 = visual.ImageStim(
    win=win,
    name='five_12', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/five.png', mask=None,
    ori=0, pos=(0.45, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
six_12 = visual.ImageStim(
    win=win,
    name='six_12', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/six.png', mask=None,
    ori=0, pos=(0.70, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)
ten_12 = visual.ImageStim(
    win=win,
    name='ten_12', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/ten.png', mask=None,
    ori=0, pos=(0.20, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)
eleven_12 = visual.ImageStim(
    win=win,
    name='eleven_12', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/eleven.png', mask=None,
    ori=0, pos=(0.45, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)
twelve_12 = visual.ImageStim(
    win=win,
    name='twelve_12', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/twelve.png', mask=None,
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
gram13_8 = visual.ImageStim(
    win=win,
    name='gram13_8', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram13.png', mask=None,
    ori=0, pos=(-0.2, -0.3), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-14.0)
gram14_8 = visual.ImageStim(
    win=win,
    name='gram14_8', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram14.png', mask=None,
    ori=0, pos=(-0.45, 0.3), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-15.0)
gram15_8 = visual.ImageStim(
    win=win,
    name='gram15_8', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram15.png', mask=None,
    ori=0, pos=(0.2, -0.3), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-16.0)
gram16_8 = visual.ImageStim(
    win=win,
    name='gram16_8', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram16.png', mask=None,
    ori=0, pos=(-0.45, -0.3), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-17.0)
gram17_8 = visual.ImageStim(
    win=win,
    name='gram17_8', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram17.png', mask=None,
    ori=0, pos=(-0.7, 0.3), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-18.0)
gram18_8 = visual.ImageStim(
    win=win,
    name='gram18_8', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram18.png', mask=None,
    ori=0, pos=(0.7, -0.3), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-19.0)
gram19_8 = visual.ImageStim(
    win=win,
    name='gram19_8', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram19.png', mask=None,
    ori=0, pos=(-0.7, -0.3), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-20.0)
gram20_8 = visual.ImageStim(
    win=win,
    name='gram20_8', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram20.png', mask=None,
    ori=0, pos=(-0.2, 0.3), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-21.0)
gram21_8 = visual.ImageStim(
    win=win,
    name='gram21_8', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram21.png', mask=None,
    ori=0, pos=(0.7, 0.3), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-22.0)
gram22_8 = visual.ImageStim(
    win=win,
    name='gram22_8', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram22.png', mask=None,
    ori=0, pos=(0.2, 0.3), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-23.0)
gram23_8 = visual.ImageStim(
    win=win,
    name='gram23_8', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram23.png', mask=None,
    ori=0, pos=(0.45, -0.3), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-24.0)
gram24_8 = visual.ImageStim(
    win=win,
    name='gram24_8', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram24.png', mask=None,
    ori=0, pos=(0.45, 0.3), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-25.0)

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
    items='C:\\Users\\rjpil\\OneDrive\\GS\\CECLAB\\vgcmd_main\\stimuli\\tipi_format.csv',
    textHeight=0.03,
    randomize=False,
    size=(1, 0.7),
    pos=(0, 0),
    itemPadding=0.05)
tipi_scale = visual.ImageStim(
    win=win,
    name='tipi_scale', 
    image='C:\\Users\\rjpil\\OneDrive\\GS\\CECLAB\\vgcmd_main\\stimuli\\tipi_scale.png', mask=None,
    ori=0, pos=(0, 0.43), size=(0.7, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "trial_answer"
trial_answerClock = core.Clock()
one_7 = visual.ImageStim(
    win=win,
    name='one_7', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/one.png', mask=None,
    ori=0, pos=(-.70, .30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
mouse_9 = event.Mouse(win=win)
x, y = [None, None]
mouse_9.mouseClock = core.Clock()
two_7 = visual.ImageStim(
    win=win,
    name='two_7', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/two.png', mask=None,
    ori=0, pos=(-.45, .30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
three_7 = visual.ImageStim(
    win=win,
    name='three_7', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/three.png', mask=None,
    ori=0, pos=(-0.20, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
seven_7 = visual.ImageStim(
    win=win,
    name='seven_7', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/seven.png', mask=None,
    ori=0, pos=(-0.70, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
eight_7 = visual.ImageStim(
    win=win,
    name='eight_7', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/eight.png', mask=None,
    ori=0, pos=(-0.45, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
nine_7 = visual.ImageStim(
    win=win,
    name='nine_7', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/nine.png', mask=None,
    ori=0, pos=(-0.20, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
four_7 = visual.ImageStim(
    win=win,
    name='four_7', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/four.png', mask=None,
    ori=0, pos=(0.20, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
five_7 = visual.ImageStim(
    win=win,
    name='five_7', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/five.png', mask=None,
    ori=0, pos=(0.45, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
six_7 = visual.ImageStim(
    win=win,
    name='six_7', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/six.png', mask=None,
    ori=0, pos=(0.70, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)
ten_7 = visual.ImageStim(
    win=win,
    name='ten_7', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/ten.png', mask=None,
    ori=0, pos=(0.20, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)
eleven_7 = visual.ImageStim(
    win=win,
    name='eleven_7', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/eleven.png', mask=None,
    ori=0, pos=(0.45, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)
twelve_7 = visual.ImageStim(
    win=win,
    name='twelve_7', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/twelve.png', mask=None,
    ori=0, pos=(0.70, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-12.0)
import pathlib

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
gram01_4 = visual.ImageStim(
    win=win,
    name='gram01_4', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram01.png', mask=None,
    ori=0, pos=(0.45, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-14.0)
gram02_4 = visual.ImageStim(
    win=win,
    name='gram02_4', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram02.png', mask=None,
    ori=0, pos=(0.20, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-15.0)
gram03_4 = visual.ImageStim(
    win=win,
    name='gram03_4', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram03.png', mask=None,
    ori=0, pos=(-0.20, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-16.0)
gram04_4 = visual.ImageStim(
    win=win,
    name='gram04_4', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram04.png', mask=None,
    ori=0, pos=(-0.45, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-17.0)
gram05_4 = visual.ImageStim(
    win=win,
    name='gram05_4', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram05.png', mask=None,
    ori=0, pos=(0.70, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-18.0)
gram06_4 = visual.ImageStim(
    win=win,
    name='gram06_4', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram06.png', mask=None,
    ori=0, pos=(0.45, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-19.0)
gram07_4 = visual.ImageStim(
    win=win,
    name='gram07_4', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram07.png', mask=None,
    ori=0, pos=(-0.20, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-20.0)
gram08_4 = visual.ImageStim(
    win=win,
    name='gram08_4', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram08.png', mask=None,
    ori=0, pos=(-0.70, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-21.0)
gram09_4 = visual.ImageStim(
    win=win,
    name='gram09_4', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram09.png', mask=None,
    ori=0, pos=(-0.45, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-22.0)
gram10_4 = visual.ImageStim(
    win=win,
    name='gram10_4', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram10.png', mask=None,
    ori=0, pos=(-0.70, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-23.0)
gram11_4 = visual.ImageStim(
    win=win,
    name='gram11_4', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram11.png', mask=None,
    ori=0, pos=(0.70, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-24.0)
gram12_4 = visual.ImageStim(
    win=win,
    name='gram12_4', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram12.png', mask=None,
    ori=0, pos=(0.20, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-25.0)

# Initialize components for Routine "trial_2_answer"
trial_2_answerClock = core.Clock()
one_8 = visual.ImageStim(
    win=win,
    name='one_8', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/one.png', mask=None,
    ori=0, pos=(-.70, .30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
mouse_10 = event.Mouse(win=win)
x, y = [None, None]
mouse_10.mouseClock = core.Clock()
two_8 = visual.ImageStim(
    win=win,
    name='two_8', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/two.png', mask=None,
    ori=0, pos=(-.45, .30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
three_8 = visual.ImageStim(
    win=win,
    name='three_8', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/three.png', mask=None,
    ori=0, pos=(-0.20, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
seven_8 = visual.ImageStim(
    win=win,
    name='seven_8', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/seven.png', mask=None,
    ori=0, pos=(-0.70, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
eight_8 = visual.ImageStim(
    win=win,
    name='eight_8', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/eight.png', mask=None,
    ori=0, pos=(-0.45, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
nine_8 = visual.ImageStim(
    win=win,
    name='nine_8', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/nine.png', mask=None,
    ori=0, pos=(-0.20, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
four_8 = visual.ImageStim(
    win=win,
    name='four_8', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/four.png', mask=None,
    ori=0, pos=(0.20, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
five_8 = visual.ImageStim(
    win=win,
    name='five_8', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/five.png', mask=None,
    ori=0, pos=(0.45, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
six_8 = visual.ImageStim(
    win=win,
    name='six_8', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/six.png', mask=None,
    ori=0, pos=(0.70, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)
ten_8 = visual.ImageStim(
    win=win,
    name='ten_8', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/ten.png', mask=None,
    ori=0, pos=(0.20, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)
eleven_8 = visual.ImageStim(
    win=win,
    name='eleven_8', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/eleven.png', mask=None,
    ori=0, pos=(0.45, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)
twelve_8 = visual.ImageStim(
    win=win,
    name='twelve_8', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/twelve.png', mask=None,
    ori=0, pos=(0.70, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-12.0)
import pathlib

def movePicked(picked, mouse, grabbed):
    if grabbed is not None and mouse.isPressedIn(grabbed):
        grabbed.pos = mouse.getPos()
        return grabbed
    else:
        for piece in picked:
            if mouse.isPressedIn(piece) and grabbed is None:
                print(f"the piece is {piece.name} and position is {piece.pos}")
                return piece

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
gram01_5 = visual.ImageStim(
    win=win,
    name='gram01_5', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram01.png', mask=None,
    ori=0, pos=(0.70, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-14.0)
gram02_5 = visual.ImageStim(
    win=win,
    name='gram02_5', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram02.png', mask=None,
    ori=0, pos=(0.70, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-15.0)
gram03_5 = visual.ImageStim(
    win=win,
    name='gram03_5', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram03.png', mask=None,
    ori=0, pos=(0.20, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-16.0)
gram04_5 = visual.ImageStim(
    win=win,
    name='gram04_5', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram04.png', mask=None,
    ori=0, pos=(-0.20, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-17.0)
gram05_5 = visual.ImageStim(
    win=win,
    name='gram05_5', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram05.png', mask=None,
    ori=0, pos=(0.20, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-18.0)
gram06_5 = visual.ImageStim(
    win=win,
    name='gram06_5', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram06.png', mask=None,
    ori=0, pos=(0.45, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-19.0)
gram07_5 = visual.ImageStim(
    win=win,
    name='gram07_5', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram07.png', mask=None,
    ori=0, pos=(-0.20, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-20.0)
gram08_5 = visual.ImageStim(
    win=win,
    name='gram08_5', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram08.png', mask=None,
    ori=0, pos=(-0.70, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-21.0)
gram09_5 = visual.ImageStim(
    win=win,
    name='gram09_5', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram09.png', mask=None,
    ori=0, pos=(-0.45, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-22.0)
gram10_5 = visual.ImageStim(
    win=win,
    name='gram10_5', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram10.png', mask=None,
    ori=0, pos=(-0.70, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-23.0)
gram11_5 = visual.ImageStim(
    win=win,
    name='gram11_5', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram11.png', mask=None,
    ori=0, pos=(-0.45, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-24.0)
gram12_5 = visual.ImageStim(
    win=win,
    name='gram12_5', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram12.png', mask=None,
    ori=0, pos=(0.45, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-25.0)

# Initialize components for Routine "trial_3_answer"
trial_3_answerClock = core.Clock()
one_9 = visual.ImageStim(
    win=win,
    name='one_9', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/one.png', mask=None,
    ori=0, pos=(-.70, .30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
mouse_11 = event.Mouse(win=win)
x, y = [None, None]
mouse_11.mouseClock = core.Clock()
two_9 = visual.ImageStim(
    win=win,
    name='two_9', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/two.png', mask=None,
    ori=0, pos=(-.45, .30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
three_9 = visual.ImageStim(
    win=win,
    name='three_9', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/three.png', mask=None,
    ori=0, pos=(-0.20, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
seven_9 = visual.ImageStim(
    win=win,
    name='seven_9', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/seven.png', mask=None,
    ori=0, pos=(-0.70, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
eight_9 = visual.ImageStim(
    win=win,
    name='eight_9', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/eight.png', mask=None,
    ori=0, pos=(-0.45, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
nine_9 = visual.ImageStim(
    win=win,
    name='nine_9', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/nine.png', mask=None,
    ori=0, pos=(-0.20, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
four_9 = visual.ImageStim(
    win=win,
    name='four_9', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/four.png', mask=None,
    ori=0, pos=(0.20, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
five_9 = visual.ImageStim(
    win=win,
    name='five_9', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/five.png', mask=None,
    ori=0, pos=(0.45, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
six_9 = visual.ImageStim(
    win=win,
    name='six_9', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/six.png', mask=None,
    ori=0, pos=(0.70, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)
ten_9 = visual.ImageStim(
    win=win,
    name='ten_9', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/ten.png', mask=None,
    ori=0, pos=(0.20, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)
eleven_9 = visual.ImageStim(
    win=win,
    name='eleven_9', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/eleven.png', mask=None,
    ori=0, pos=(0.45, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)
twelve_9 = visual.ImageStim(
    win=win,
    name='twelve_9', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/twelve.png', mask=None,
    ori=0, pos=(0.70, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-12.0)
import pathlib

def movePicked(picked, mouse, grabbed):
    if grabbed is not None and mouse.isPressedIn(grabbed):
        grabbed.pos = mouse.getPos()
        return grabbed
    else:
        for piece in picked:
            if mouse.isPressedIn(piece) and grabbed is None:
                print(f"the piece is {piece.name} and position is {piece.pos}")
                return piece

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
gram01_6 = visual.ImageStim(
    win=win,
    name='gram01_6', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram01.png', mask=None,
    ori=0, pos=(-0.2, 0.3), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-14.0)
gram02_6 = visual.ImageStim(
    win=win,
    name='gram02_6', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram02.png', mask=None,
    ori=0, pos=(-0.7, 0.3), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-15.0)
gram03_6 = visual.ImageStim(
    win=win,
    name='gram03_6', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram03.png', mask=None,
    ori=0, pos=(0.7, 0.3), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-16.0)
gram04_6 = visual.ImageStim(
    win=win,
    name='gram04_6', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram04.png', mask=None,
    ori=0, pos=(0.2, 0.3), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-17.0)
gram05_6 = visual.ImageStim(
    win=win,
    name='gram05_6', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram05.png', mask=None,
    ori=0, pos=(0.2, -0.3), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-18.0)
gram06_6 = visual.ImageStim(
    win=win,
    name='gram06_6', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram06.png', mask=None,
    ori=0, pos=(0.7, -0.3), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-19.0)
gram07_6 = visual.ImageStim(
    win=win,
    name='gram07_6', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram07.png', mask=None,
    ori=0, pos=(0.45, -0.3), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-20.0)
gram08_6 = visual.ImageStim(
    win=win,
    name='gram08_6', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram08.png', mask=None,
    ori=0, pos=(0.45, 0.3), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-21.0)
gram09_6 = visual.ImageStim(
    win=win,
    name='gram09_6', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram09.png', mask=None,
    ori=0, pos=(-0.45, -0.3), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-22.0)
gram10_6 = visual.ImageStim(
    win=win,
    name='gram10_6', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram10.png', mask=None,
    ori=0, pos=(-0.7, -0.3), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-23.0)
gram11_6 = visual.ImageStim(
    win=win,
    name='gram11_6', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram11.png', mask=None,
    ori=0, pos=(-0.45, 0.3), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-24.0)
gram12_6 = visual.ImageStim(
    win=win,
    name='gram12_6', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/tangrams/gram12.png', mask=None,
    ori=0, pos=(-0.2, -0.3), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-25.0)

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

# ------Prepare to start Routine "trial_4_answer"-------
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_12
mouse_12.clicked_name = []
gotValidClick = False  # until a click is received
pieces = [gram13,gram14,gram15,gram16,gram17,gram18,gram19,gram20,gram21,gram22,gram23,gram24]
picked = []
movingPiece = None

    # this works, it keeps track of what trial it is
    # so in win_checker() add an if statement
        # if this_trial is specific trial
        # change what hitboxes takes in as its 2nd argument
        # depending on the winstate order

continue_instr = continue_instr()
continue_instr.autoDraw = True

def win_checker()->bool:
    order = [hitbox_checker("one", gram20), 
                    hitbox_checker("two", gram16),
                    hitbox_checker("three", gram23),
                    hitbox_checker("four", gram14),
                    hitbox_checker("five", gram18),
                    hitbox_checker("six", gram24),
                    hitbox_checker("seven", gram19),
                    hitbox_checker("eight", gram22),
                    hitbox_checker("nine", gram13),
                    hitbox_checker("ten", gram17),
                    hitbox_checker("eleven", gram15),
                    hitbox_checker("twelve", gram21)]
    if all(order):
        return True

trial_time = []
# keep track of which components have finished
trial_4_answerComponents = [one_10, mouse_12, two_10, three_10, seven_10, eight_10, nine_10, four_10, five_10, six_10, ten_10, eleven_10, twelve_10, gram13, gram14, gram15, gram16, gram17, gram18, gram19, gram20, gram21, gram22, gram23, gram24]
for thisComponent in trial_4_answerComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial_4_answerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "trial_4_answer"-------
while continueRoutine:
    # get current time
    t = trial_4_answerClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial_4_answerClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *one_10* updates
    if one_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        one_10.frameNStart = frameN  # exact frame index
        one_10.tStart = t  # local t and not account for scr refresh
        one_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(one_10, 'tStartRefresh')  # time at next scr refresh
        one_10.setAutoDraw(True)
    # *mouse_12* updates
    if mouse_12.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_12.frameNStart = frameN  # exact frame index
        mouse_12.tStart = t  # local t and not account for scr refresh
        mouse_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_12, 'tStartRefresh')  # time at next scr refresh
        mouse_12.status = STARTED
        mouse_12.mouseClock.reset()
        prevButtonState = mouse_12.getPressed()  # if button is down already this ISN'T a new click
    if mouse_12.status == STARTED:  # only update if started and not finished!
        buttons = mouse_12.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [continue_text,]:
                    if obj.contains(mouse_12):
                        gotValidClick = True
                        mouse_12.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # *two_10* updates
    if two_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        two_10.frameNStart = frameN  # exact frame index
        two_10.tStart = t  # local t and not account for scr refresh
        two_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(two_10, 'tStartRefresh')  # time at next scr refresh
        two_10.setAutoDraw(True)
    
    # *three_10* updates
    if three_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        three_10.frameNStart = frameN  # exact frame index
        three_10.tStart = t  # local t and not account for scr refresh
        three_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(three_10, 'tStartRefresh')  # time at next scr refresh
        three_10.setAutoDraw(True)
    
    # *seven_10* updates
    if seven_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        seven_10.frameNStart = frameN  # exact frame index
        seven_10.tStart = t  # local t and not account for scr refresh
        seven_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(seven_10, 'tStartRefresh')  # time at next scr refresh
        seven_10.setAutoDraw(True)
    
    # *eight_10* updates
    if eight_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        eight_10.frameNStart = frameN  # exact frame index
        eight_10.tStart = t  # local t and not account for scr refresh
        eight_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(eight_10, 'tStartRefresh')  # time at next scr refresh
        eight_10.setAutoDraw(True)
    
    # *nine_10* updates
    if nine_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        nine_10.frameNStart = frameN  # exact frame index
        nine_10.tStart = t  # local t and not account for scr refresh
        nine_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(nine_10, 'tStartRefresh')  # time at next scr refresh
        nine_10.setAutoDraw(True)
    
    # *four_10* updates
    if four_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        four_10.frameNStart = frameN  # exact frame index
        four_10.tStart = t  # local t and not account for scr refresh
        four_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(four_10, 'tStartRefresh')  # time at next scr refresh
        four_10.setAutoDraw(True)
    
    # *five_10* updates
    if five_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        five_10.frameNStart = frameN  # exact frame index
        five_10.tStart = t  # local t and not account for scr refresh
        five_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(five_10, 'tStartRefresh')  # time at next scr refresh
        five_10.setAutoDraw(True)
    
    # *six_10* updates
    if six_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        six_10.frameNStart = frameN  # exact frame index
        six_10.tStart = t  # local t and not account for scr refresh
        six_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(six_10, 'tStartRefresh')  # time at next scr refresh
        six_10.setAutoDraw(True)
    
    # *ten_10* updates
    if ten_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ten_10.frameNStart = frameN  # exact frame index
        ten_10.tStart = t  # local t and not account for scr refresh
        ten_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ten_10, 'tStartRefresh')  # time at next scr refresh
        ten_10.setAutoDraw(True)
    
    # *eleven_10* updates
    if eleven_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        eleven_10.frameNStart = frameN  # exact frame index
        eleven_10.tStart = t  # local t and not account for scr refresh
        eleven_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(eleven_10, 'tStartRefresh')  # time at next scr refresh
        eleven_10.setAutoDraw(True)
    
    # *twelve_10* updates
    if twelve_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        twelve_10.frameNStart = frameN  # exact frame index
        twelve_10.tStart = t  # local t and not account for scr refresh
        twelve_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(twelve_10, 'tStartRefresh')  # time at next scr refresh
        twelve_10.setAutoDraw(True)
    for piece in pieces:
        if mouse.isPressedIn(piece) and movingPiece is None:
            picked.append(piece)
    
    movingPiece = movePicked(picked, mouse, movingPiece)
    
    win_state = False
    
    win_state = win_checker()
    
    
    # in begin routine, create a function that will check if
    # all the tangrams are in the correct spot
    # if they are, then have it return true and draw continue_text
    
    if win_state:
        continue_text = win_continue()
        continue_text.draw()
    else: 
        win.flip()
    
    
    #if mouse.isPressedIn(polygon):
    #    crosses.append(makeCross(mouse.getPos()))
    
    # *gram13* updates
    if gram13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram13.frameNStart = frameN  # exact frame index
        gram13.tStart = t  # local t and not account for scr refresh
        gram13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram13, 'tStartRefresh')  # time at next scr refresh
        gram13.setAutoDraw(True)
    
    # *gram14* updates
    if gram14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram14.frameNStart = frameN  # exact frame index
        gram14.tStart = t  # local t and not account for scr refresh
        gram14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram14, 'tStartRefresh')  # time at next scr refresh
        gram14.setAutoDraw(True)
    
    # *gram15* updates
    if gram15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram15.frameNStart = frameN  # exact frame index
        gram15.tStart = t  # local t and not account for scr refresh
        gram15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram15, 'tStartRefresh')  # time at next scr refresh
        gram15.setAutoDraw(True)
    
    # *gram16* updates
    if gram16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram16.frameNStart = frameN  # exact frame index
        gram16.tStart = t  # local t and not account for scr refresh
        gram16.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram16, 'tStartRefresh')  # time at next scr refresh
        gram16.setAutoDraw(True)
    
    # *gram17* updates
    if gram17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram17.frameNStart = frameN  # exact frame index
        gram17.tStart = t  # local t and not account for scr refresh
        gram17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram17, 'tStartRefresh')  # time at next scr refresh
        gram17.setAutoDraw(True)
    
    # *gram18* updates
    if gram18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram18.frameNStart = frameN  # exact frame index
        gram18.tStart = t  # local t and not account for scr refresh
        gram18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram18, 'tStartRefresh')  # time at next scr refresh
        gram18.setAutoDraw(True)
    
    # *gram19* updates
    if gram19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram19.frameNStart = frameN  # exact frame index
        gram19.tStart = t  # local t and not account for scr refresh
        gram19.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram19, 'tStartRefresh')  # time at next scr refresh
        gram19.setAutoDraw(True)
    
    # *gram20* updates
    if gram20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram20.frameNStart = frameN  # exact frame index
        gram20.tStart = t  # local t and not account for scr refresh
        gram20.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram20, 'tStartRefresh')  # time at next scr refresh
        gram20.setAutoDraw(True)
    
    # *gram21* updates
    if gram21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram21.frameNStart = frameN  # exact frame index
        gram21.tStart = t  # local t and not account for scr refresh
        gram21.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram21, 'tStartRefresh')  # time at next scr refresh
        gram21.setAutoDraw(True)
    
    # *gram22* updates
    if gram22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram22.frameNStart = frameN  # exact frame index
        gram22.tStart = t  # local t and not account for scr refresh
        gram22.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram22, 'tStartRefresh')  # time at next scr refresh
        gram22.setAutoDraw(True)
    
    # *gram23* updates
    if gram23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram23.frameNStart = frameN  # exact frame index
        gram23.tStart = t  # local t and not account for scr refresh
        gram23.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram23, 'tStartRefresh')  # time at next scr refresh
        gram23.setAutoDraw(True)
    
    # *gram24* updates
    if gram24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram24.frameNStart = frameN  # exact frame index
        gram24.tStart = t  # local t and not account for scr refresh
        gram24.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram24, 'tStartRefresh')  # time at next scr refresh
        gram24.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial_4_answerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial_4_answer"-------
for thisComponent in trial_4_answerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('one_10.started', one_10.tStartRefresh)
thisExp.addData('one_10.stopped', one_10.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = mouse_12.getPos()
buttons = mouse_12.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    for obj in [continue_text,]:
        if obj.contains(mouse_12):
            gotValidClick = True
            mouse_12.clicked_name.append(obj.name)
thisExp.addData('mouse_12.x', x)
thisExp.addData('mouse_12.y', y)
thisExp.addData('mouse_12.leftButton', buttons[0])
thisExp.addData('mouse_12.midButton', buttons[1])
thisExp.addData('mouse_12.rightButton', buttons[2])
if len(mouse_12.clicked_name):
    thisExp.addData('mouse_12.clicked_name', mouse_12.clicked_name[0])
thisExp.addData('mouse_12.started', mouse_12.tStart)
thisExp.addData('mouse_12.stopped', mouse_12.tStop)
thisExp.nextEntry()
thisExp.addData('two_10.started', two_10.tStartRefresh)
thisExp.addData('two_10.stopped', two_10.tStopRefresh)
thisExp.addData('three_10.started', three_10.tStartRefresh)
thisExp.addData('three_10.stopped', three_10.tStopRefresh)
thisExp.addData('seven_10.started', seven_10.tStartRefresh)
thisExp.addData('seven_10.stopped', seven_10.tStopRefresh)
thisExp.addData('eight_10.started', eight_10.tStartRefresh)
thisExp.addData('eight_10.stopped', eight_10.tStopRefresh)
thisExp.addData('nine_10.started', nine_10.tStartRefresh)
thisExp.addData('nine_10.stopped', nine_10.tStopRefresh)
thisExp.addData('four_10.started', four_10.tStartRefresh)
thisExp.addData('four_10.stopped', four_10.tStopRefresh)
thisExp.addData('five_10.started', five_10.tStartRefresh)
thisExp.addData('five_10.stopped', five_10.tStopRefresh)
thisExp.addData('six_10.started', six_10.tStartRefresh)
thisExp.addData('six_10.stopped', six_10.tStopRefresh)
thisExp.addData('ten_10.started', ten_10.tStartRefresh)
thisExp.addData('ten_10.stopped', ten_10.tStopRefresh)
thisExp.addData('eleven_10.started', eleven_10.tStartRefresh)
thisExp.addData('eleven_10.stopped', eleven_10.tStopRefresh)
thisExp.addData('twelve_10.started', twelve_10.tStartRefresh)
thisExp.addData('twelve_10.stopped', twelve_10.tStopRefresh)
thisExp.addData('gram13.started', gram13.tStartRefresh)
thisExp.addData('gram13.stopped', gram13.tStopRefresh)
thisExp.addData('gram14.started', gram14.tStartRefresh)
thisExp.addData('gram14.stopped', gram14.tStopRefresh)
thisExp.addData('gram15.started', gram15.tStartRefresh)
thisExp.addData('gram15.stopped', gram15.tStopRefresh)
thisExp.addData('gram16.started', gram16.tStartRefresh)
thisExp.addData('gram16.stopped', gram16.tStopRefresh)
thisExp.addData('gram17.started', gram17.tStartRefresh)
thisExp.addData('gram17.stopped', gram17.tStopRefresh)
thisExp.addData('gram18.started', gram18.tStartRefresh)
thisExp.addData('gram18.stopped', gram18.tStopRefresh)
thisExp.addData('gram19.started', gram19.tStartRefresh)
thisExp.addData('gram19.stopped', gram19.tStopRefresh)
thisExp.addData('gram20.started', gram20.tStartRefresh)
thisExp.addData('gram20.stopped', gram20.tStopRefresh)
thisExp.addData('gram21.started', gram21.tStartRefresh)
thisExp.addData('gram21.stopped', gram21.tStopRefresh)
thisExp.addData('gram22.started', gram22.tStartRefresh)
thisExp.addData('gram22.stopped', gram22.tStopRefresh)
thisExp.addData('gram23.started', gram23.tStartRefresh)
thisExp.addData('gram23.stopped', gram23.tStopRefresh)
thisExp.addData('gram24.started', gram24.tStartRefresh)
thisExp.addData('gram24.stopped', gram24.tStopRefresh)
# the Routine "trial_4_answer" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trial_5_answer"-------
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_13
mouse_13.clicked_name = []
gotValidClick = False  # until a click is received
pieces = [gram13_7,gram14_7,gram15_7,gram16_7,gram17_7,gram18_7,gram19_7,gram20_7,gram21_7,gram22_7,gram23_7,gram24_7]
picked = []
movingPiece = None

    # this works, it keeps track of what trial it is
    # so in win_checker() add an if statement
        # if this_trial is specific trial
        # change what hitboxes takes in as its 2nd argument
        # depending on the winstate order


def win_checker()->bool:
    order = [hitbox_checker("one", gram21_7), 
                    hitbox_checker("two", gram23_7),
                    hitbox_checker("three", gram17_7),
                    hitbox_checker("four", gram22_7),
                    hitbox_checker("five", gram19_7),
                    hitbox_checker("six", gram18_7),
                    hitbox_checker("seven", gram20_7),
                    hitbox_checker("eight", gram15_7),
                    hitbox_checker("nine", gram14_7),
                    hitbox_checker("ten", gram16_7),
                    hitbox_checker("eleven", gram13_7),
                    hitbox_checker("twelve", gram24_7)]
    if all(order):
        return True

trial_time = []
# keep track of which components have finished
trial_5_answerComponents = [one_11, mouse_13, two_11, three_11, seven_11, eight_11, nine_11, four_11, five_11, six_11, ten_11, eleven_11, twelve_11, gram13_7, gram14_7, gram15_7, gram16_7, gram17_7, gram18_7, gram19_7, gram20_7, gram21_7, gram22_7, gram23_7, gram24_7]
for thisComponent in trial_5_answerComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial_5_answerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "trial_5_answer"-------
while continueRoutine:
    # get current time
    t = trial_5_answerClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial_5_answerClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *one_11* updates
    if one_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        one_11.frameNStart = frameN  # exact frame index
        one_11.tStart = t  # local t and not account for scr refresh
        one_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(one_11, 'tStartRefresh')  # time at next scr refresh
        one_11.setAutoDraw(True)
    # *mouse_13* updates
    if mouse_13.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_13.frameNStart = frameN  # exact frame index
        mouse_13.tStart = t  # local t and not account for scr refresh
        mouse_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_13, 'tStartRefresh')  # time at next scr refresh
        mouse_13.status = STARTED
        mouse_13.mouseClock.reset()
        prevButtonState = mouse_13.getPressed()  # if button is down already this ISN'T a new click
    if mouse_13.status == STARTED:  # only update if started and not finished!
        buttons = mouse_13.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [continue_text,]:
                    if obj.contains(mouse_13):
                        gotValidClick = True
                        mouse_13.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # *two_11* updates
    if two_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        two_11.frameNStart = frameN  # exact frame index
        two_11.tStart = t  # local t and not account for scr refresh
        two_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(two_11, 'tStartRefresh')  # time at next scr refresh
        two_11.setAutoDraw(True)
    
    # *three_11* updates
    if three_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        three_11.frameNStart = frameN  # exact frame index
        three_11.tStart = t  # local t and not account for scr refresh
        three_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(three_11, 'tStartRefresh')  # time at next scr refresh
        three_11.setAutoDraw(True)
    
    # *seven_11* updates
    if seven_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        seven_11.frameNStart = frameN  # exact frame index
        seven_11.tStart = t  # local t and not account for scr refresh
        seven_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(seven_11, 'tStartRefresh')  # time at next scr refresh
        seven_11.setAutoDraw(True)
    
    # *eight_11* updates
    if eight_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        eight_11.frameNStart = frameN  # exact frame index
        eight_11.tStart = t  # local t and not account for scr refresh
        eight_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(eight_11, 'tStartRefresh')  # time at next scr refresh
        eight_11.setAutoDraw(True)
    
    # *nine_11* updates
    if nine_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        nine_11.frameNStart = frameN  # exact frame index
        nine_11.tStart = t  # local t and not account for scr refresh
        nine_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(nine_11, 'tStartRefresh')  # time at next scr refresh
        nine_11.setAutoDraw(True)
    
    # *four_11* updates
    if four_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        four_11.frameNStart = frameN  # exact frame index
        four_11.tStart = t  # local t and not account for scr refresh
        four_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(four_11, 'tStartRefresh')  # time at next scr refresh
        four_11.setAutoDraw(True)
    
    # *five_11* updates
    if five_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        five_11.frameNStart = frameN  # exact frame index
        five_11.tStart = t  # local t and not account for scr refresh
        five_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(five_11, 'tStartRefresh')  # time at next scr refresh
        five_11.setAutoDraw(True)
    
    # *six_11* updates
    if six_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        six_11.frameNStart = frameN  # exact frame index
        six_11.tStart = t  # local t and not account for scr refresh
        six_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(six_11, 'tStartRefresh')  # time at next scr refresh
        six_11.setAutoDraw(True)
    
    # *ten_11* updates
    if ten_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ten_11.frameNStart = frameN  # exact frame index
        ten_11.tStart = t  # local t and not account for scr refresh
        ten_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ten_11, 'tStartRefresh')  # time at next scr refresh
        ten_11.setAutoDraw(True)
    
    # *eleven_11* updates
    if eleven_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        eleven_11.frameNStart = frameN  # exact frame index
        eleven_11.tStart = t  # local t and not account for scr refresh
        eleven_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(eleven_11, 'tStartRefresh')  # time at next scr refresh
        eleven_11.setAutoDraw(True)
    
    # *twelve_11* updates
    if twelve_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        twelve_11.frameNStart = frameN  # exact frame index
        twelve_11.tStart = t  # local t and not account for scr refresh
        twelve_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(twelve_11, 'tStartRefresh')  # time at next scr refresh
        twelve_11.setAutoDraw(True)
    for piece in pieces:
        if mouse.isPressedIn(piece) and movingPiece is None:
            picked.append(piece)
    
    movingPiece = movePicked(picked, mouse, movingPiece)
    
    win_state = False
    
    win_state = win_checker()
    
    
    if win_state:
        continue_text = win_continue()
        continue_text.draw()
    else: 
        win.flip()
    
    
    # *gram13_7* updates
    if gram13_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram13_7.frameNStart = frameN  # exact frame index
        gram13_7.tStart = t  # local t and not account for scr refresh
        gram13_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram13_7, 'tStartRefresh')  # time at next scr refresh
        gram13_7.setAutoDraw(True)
    
    # *gram14_7* updates
    if gram14_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram14_7.frameNStart = frameN  # exact frame index
        gram14_7.tStart = t  # local t and not account for scr refresh
        gram14_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram14_7, 'tStartRefresh')  # time at next scr refresh
        gram14_7.setAutoDraw(True)
    
    # *gram15_7* updates
    if gram15_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram15_7.frameNStart = frameN  # exact frame index
        gram15_7.tStart = t  # local t and not account for scr refresh
        gram15_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram15_7, 'tStartRefresh')  # time at next scr refresh
        gram15_7.setAutoDraw(True)
    
    # *gram16_7* updates
    if gram16_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram16_7.frameNStart = frameN  # exact frame index
        gram16_7.tStart = t  # local t and not account for scr refresh
        gram16_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram16_7, 'tStartRefresh')  # time at next scr refresh
        gram16_7.setAutoDraw(True)
    
    # *gram17_7* updates
    if gram17_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram17_7.frameNStart = frameN  # exact frame index
        gram17_7.tStart = t  # local t and not account for scr refresh
        gram17_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram17_7, 'tStartRefresh')  # time at next scr refresh
        gram17_7.setAutoDraw(True)
    
    # *gram18_7* updates
    if gram18_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram18_7.frameNStart = frameN  # exact frame index
        gram18_7.tStart = t  # local t and not account for scr refresh
        gram18_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram18_7, 'tStartRefresh')  # time at next scr refresh
        gram18_7.setAutoDraw(True)
    
    # *gram19_7* updates
    if gram19_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram19_7.frameNStart = frameN  # exact frame index
        gram19_7.tStart = t  # local t and not account for scr refresh
        gram19_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram19_7, 'tStartRefresh')  # time at next scr refresh
        gram19_7.setAutoDraw(True)
    
    # *gram20_7* updates
    if gram20_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram20_7.frameNStart = frameN  # exact frame index
        gram20_7.tStart = t  # local t and not account for scr refresh
        gram20_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram20_7, 'tStartRefresh')  # time at next scr refresh
        gram20_7.setAutoDraw(True)
    
    # *gram21_7* updates
    if gram21_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram21_7.frameNStart = frameN  # exact frame index
        gram21_7.tStart = t  # local t and not account for scr refresh
        gram21_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram21_7, 'tStartRefresh')  # time at next scr refresh
        gram21_7.setAutoDraw(True)
    
    # *gram22_7* updates
    if gram22_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram22_7.frameNStart = frameN  # exact frame index
        gram22_7.tStart = t  # local t and not account for scr refresh
        gram22_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram22_7, 'tStartRefresh')  # time at next scr refresh
        gram22_7.setAutoDraw(True)
    
    # *gram23_7* updates
    if gram23_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram23_7.frameNStart = frameN  # exact frame index
        gram23_7.tStart = t  # local t and not account for scr refresh
        gram23_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram23_7, 'tStartRefresh')  # time at next scr refresh
        gram23_7.setAutoDraw(True)
    
    # *gram24_7* updates
    if gram24_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram24_7.frameNStart = frameN  # exact frame index
        gram24_7.tStart = t  # local t and not account for scr refresh
        gram24_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram24_7, 'tStartRefresh')  # time at next scr refresh
        gram24_7.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial_5_answerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial_5_answer"-------
for thisComponent in trial_5_answerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('one_11.started', one_11.tStartRefresh)
thisExp.addData('one_11.stopped', one_11.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = mouse_13.getPos()
buttons = mouse_13.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    for obj in [continue_text,]:
        if obj.contains(mouse_13):
            gotValidClick = True
            mouse_13.clicked_name.append(obj.name)
thisExp.addData('mouse_13.x', x)
thisExp.addData('mouse_13.y', y)
thisExp.addData('mouse_13.leftButton', buttons[0])
thisExp.addData('mouse_13.midButton', buttons[1])
thisExp.addData('mouse_13.rightButton', buttons[2])
if len(mouse_13.clicked_name):
    thisExp.addData('mouse_13.clicked_name', mouse_13.clicked_name[0])
thisExp.addData('mouse_13.started', mouse_13.tStart)
thisExp.addData('mouse_13.stopped', mouse_13.tStop)
thisExp.nextEntry()
thisExp.addData('two_11.started', two_11.tStartRefresh)
thisExp.addData('two_11.stopped', two_11.tStopRefresh)
thisExp.addData('three_11.started', three_11.tStartRefresh)
thisExp.addData('three_11.stopped', three_11.tStopRefresh)
thisExp.addData('seven_11.started', seven_11.tStartRefresh)
thisExp.addData('seven_11.stopped', seven_11.tStopRefresh)
thisExp.addData('eight_11.started', eight_11.tStartRefresh)
thisExp.addData('eight_11.stopped', eight_11.tStopRefresh)
thisExp.addData('nine_11.started', nine_11.tStartRefresh)
thisExp.addData('nine_11.stopped', nine_11.tStopRefresh)
thisExp.addData('four_11.started', four_11.tStartRefresh)
thisExp.addData('four_11.stopped', four_11.tStopRefresh)
thisExp.addData('five_11.started', five_11.tStartRefresh)
thisExp.addData('five_11.stopped', five_11.tStopRefresh)
thisExp.addData('six_11.started', six_11.tStartRefresh)
thisExp.addData('six_11.stopped', six_11.tStopRefresh)
thisExp.addData('ten_11.started', ten_11.tStartRefresh)
thisExp.addData('ten_11.stopped', ten_11.tStopRefresh)
thisExp.addData('eleven_11.started', eleven_11.tStartRefresh)
thisExp.addData('eleven_11.stopped', eleven_11.tStopRefresh)
thisExp.addData('twelve_11.started', twelve_11.tStartRefresh)
thisExp.addData('twelve_11.stopped', twelve_11.tStopRefresh)
thisExp.addData('gram13_7.started', gram13_7.tStartRefresh)
thisExp.addData('gram13_7.stopped', gram13_7.tStopRefresh)
thisExp.addData('gram14_7.started', gram14_7.tStartRefresh)
thisExp.addData('gram14_7.stopped', gram14_7.tStopRefresh)
thisExp.addData('gram15_7.started', gram15_7.tStartRefresh)
thisExp.addData('gram15_7.stopped', gram15_7.tStopRefresh)
thisExp.addData('gram16_7.started', gram16_7.tStartRefresh)
thisExp.addData('gram16_7.stopped', gram16_7.tStopRefresh)
thisExp.addData('gram17_7.started', gram17_7.tStartRefresh)
thisExp.addData('gram17_7.stopped', gram17_7.tStopRefresh)
thisExp.addData('gram18_7.started', gram18_7.tStartRefresh)
thisExp.addData('gram18_7.stopped', gram18_7.tStopRefresh)
thisExp.addData('gram19_7.started', gram19_7.tStartRefresh)
thisExp.addData('gram19_7.stopped', gram19_7.tStopRefresh)
thisExp.addData('gram20_7.started', gram20_7.tStartRefresh)
thisExp.addData('gram20_7.stopped', gram20_7.tStopRefresh)
thisExp.addData('gram21_7.started', gram21_7.tStartRefresh)
thisExp.addData('gram21_7.stopped', gram21_7.tStopRefresh)
thisExp.addData('gram22_7.started', gram22_7.tStartRefresh)
thisExp.addData('gram22_7.stopped', gram22_7.tStopRefresh)
thisExp.addData('gram23_7.started', gram23_7.tStartRefresh)
thisExp.addData('gram23_7.stopped', gram23_7.tStopRefresh)
thisExp.addData('gram24_7.started', gram24_7.tStartRefresh)
thisExp.addData('gram24_7.stopped', gram24_7.tStopRefresh)
# the Routine "trial_5_answer" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trial_6_answer"-------
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_14
mouse_14.clicked_name = []
gotValidClick = False  # until a click is received
pieces = [gram13_8,gram14_8,gram15_8,gram16_8,gram17_8,gram18_8,gram19_8,gram20_8,gram21_8,gram22_8,gram23_8,gram24_8]
picked = []
movingPiece = None

    # this works, it keeps track of what trial it is
    # so in win_checker() add an if statement
        # if this_trial is specific trial
        # change what hitboxes takes in as its 2nd argument
        # depending on the winstate order

def win_checker()->bool:
    order = [hitbox_checker("one", gram17_8), 
                    hitbox_checker("two", gram14_8),
                    hitbox_checker("three", gram20_8),
                    hitbox_checker("four", gram22_8),
                    hitbox_checker("five", gram24_8),
                    hitbox_checker("six", gram21_8),
                    hitbox_checker("seven", gram19_8),
                    hitbox_checker("eight", gram16_8),
                    hitbox_checker("nine", gram13_8),
                    hitbox_checker("ten", gram15_8),
                    hitbox_checker("eleven", gram23_8),
                    hitbox_checker("twelve", gram18_8)]
    if all(order):
        return True

trial_time = []
# keep track of which components have finished
trial_6_answerComponents = [one_12, mouse_14, two_12, three_12, seven_12, eight_12, nine_12, four_12, five_12, six_12, ten_12, eleven_12, twelve_12, gram13_8, gram14_8, gram15_8, gram16_8, gram17_8, gram18_8, gram19_8, gram20_8, gram21_8, gram22_8, gram23_8, gram24_8]
for thisComponent in trial_6_answerComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial_6_answerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "trial_6_answer"-------
while continueRoutine:
    # get current time
    t = trial_6_answerClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial_6_answerClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *one_12* updates
    if one_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        one_12.frameNStart = frameN  # exact frame index
        one_12.tStart = t  # local t and not account for scr refresh
        one_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(one_12, 'tStartRefresh')  # time at next scr refresh
        one_12.setAutoDraw(True)
    # *mouse_14* updates
    if mouse_14.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_14.frameNStart = frameN  # exact frame index
        mouse_14.tStart = t  # local t and not account for scr refresh
        mouse_14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_14, 'tStartRefresh')  # time at next scr refresh
        mouse_14.status = STARTED
        mouse_14.mouseClock.reset()
        prevButtonState = mouse_14.getPressed()  # if button is down already this ISN'T a new click
    if mouse_14.status == STARTED:  # only update if started and not finished!
        buttons = mouse_14.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [continue_text,]:
                    if obj.contains(mouse_14):
                        gotValidClick = True
                        mouse_14.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # *two_12* updates
    if two_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        two_12.frameNStart = frameN  # exact frame index
        two_12.tStart = t  # local t and not account for scr refresh
        two_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(two_12, 'tStartRefresh')  # time at next scr refresh
        two_12.setAutoDraw(True)
    
    # *three_12* updates
    if three_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        three_12.frameNStart = frameN  # exact frame index
        three_12.tStart = t  # local t and not account for scr refresh
        three_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(three_12, 'tStartRefresh')  # time at next scr refresh
        three_12.setAutoDraw(True)
    
    # *seven_12* updates
    if seven_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        seven_12.frameNStart = frameN  # exact frame index
        seven_12.tStart = t  # local t and not account for scr refresh
        seven_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(seven_12, 'tStartRefresh')  # time at next scr refresh
        seven_12.setAutoDraw(True)
    
    # *eight_12* updates
    if eight_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        eight_12.frameNStart = frameN  # exact frame index
        eight_12.tStart = t  # local t and not account for scr refresh
        eight_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(eight_12, 'tStartRefresh')  # time at next scr refresh
        eight_12.setAutoDraw(True)
    
    # *nine_12* updates
    if nine_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        nine_12.frameNStart = frameN  # exact frame index
        nine_12.tStart = t  # local t and not account for scr refresh
        nine_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(nine_12, 'tStartRefresh')  # time at next scr refresh
        nine_12.setAutoDraw(True)
    
    # *four_12* updates
    if four_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        four_12.frameNStart = frameN  # exact frame index
        four_12.tStart = t  # local t and not account for scr refresh
        four_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(four_12, 'tStartRefresh')  # time at next scr refresh
        four_12.setAutoDraw(True)
    
    # *five_12* updates
    if five_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        five_12.frameNStart = frameN  # exact frame index
        five_12.tStart = t  # local t and not account for scr refresh
        five_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(five_12, 'tStartRefresh')  # time at next scr refresh
        five_12.setAutoDraw(True)
    
    # *six_12* updates
    if six_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        six_12.frameNStart = frameN  # exact frame index
        six_12.tStart = t  # local t and not account for scr refresh
        six_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(six_12, 'tStartRefresh')  # time at next scr refresh
        six_12.setAutoDraw(True)
    
    # *ten_12* updates
    if ten_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ten_12.frameNStart = frameN  # exact frame index
        ten_12.tStart = t  # local t and not account for scr refresh
        ten_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ten_12, 'tStartRefresh')  # time at next scr refresh
        ten_12.setAutoDraw(True)
    
    # *eleven_12* updates
    if eleven_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        eleven_12.frameNStart = frameN  # exact frame index
        eleven_12.tStart = t  # local t and not account for scr refresh
        eleven_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(eleven_12, 'tStartRefresh')  # time at next scr refresh
        eleven_12.setAutoDraw(True)
    
    # *twelve_12* updates
    if twelve_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        twelve_12.frameNStart = frameN  # exact frame index
        twelve_12.tStart = t  # local t and not account for scr refresh
        twelve_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(twelve_12, 'tStartRefresh')  # time at next scr refresh
        twelve_12.setAutoDraw(True)
    for piece in pieces:
        if mouse.isPressedIn(piece) and movingPiece is None:
            picked.append(piece)
    
    movingPiece = movePicked(picked, mouse, movingPiece)
    
    win_state = False
    
    win_state = win_checker()
    
    if win_state:
        continue_text = win_continue()
        continue_text.draw()
    else: 
        win.flip()
    
    
    # *gram13_8* updates
    if gram13_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram13_8.frameNStart = frameN  # exact frame index
        gram13_8.tStart = t  # local t and not account for scr refresh
        gram13_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram13_8, 'tStartRefresh')  # time at next scr refresh
        gram13_8.setAutoDraw(True)
    
    # *gram14_8* updates
    if gram14_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram14_8.frameNStart = frameN  # exact frame index
        gram14_8.tStart = t  # local t and not account for scr refresh
        gram14_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram14_8, 'tStartRefresh')  # time at next scr refresh
        gram14_8.setAutoDraw(True)
    
    # *gram15_8* updates
    if gram15_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram15_8.frameNStart = frameN  # exact frame index
        gram15_8.tStart = t  # local t and not account for scr refresh
        gram15_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram15_8, 'tStartRefresh')  # time at next scr refresh
        gram15_8.setAutoDraw(True)
    
    # *gram16_8* updates
    if gram16_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram16_8.frameNStart = frameN  # exact frame index
        gram16_8.tStart = t  # local t and not account for scr refresh
        gram16_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram16_8, 'tStartRefresh')  # time at next scr refresh
        gram16_8.setAutoDraw(True)
    
    # *gram17_8* updates
    if gram17_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram17_8.frameNStart = frameN  # exact frame index
        gram17_8.tStart = t  # local t and not account for scr refresh
        gram17_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram17_8, 'tStartRefresh')  # time at next scr refresh
        gram17_8.setAutoDraw(True)
    
    # *gram18_8* updates
    if gram18_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram18_8.frameNStart = frameN  # exact frame index
        gram18_8.tStart = t  # local t and not account for scr refresh
        gram18_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram18_8, 'tStartRefresh')  # time at next scr refresh
        gram18_8.setAutoDraw(True)
    
    # *gram19_8* updates
    if gram19_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram19_8.frameNStart = frameN  # exact frame index
        gram19_8.tStart = t  # local t and not account for scr refresh
        gram19_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram19_8, 'tStartRefresh')  # time at next scr refresh
        gram19_8.setAutoDraw(True)
    
    # *gram20_8* updates
    if gram20_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram20_8.frameNStart = frameN  # exact frame index
        gram20_8.tStart = t  # local t and not account for scr refresh
        gram20_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram20_8, 'tStartRefresh')  # time at next scr refresh
        gram20_8.setAutoDraw(True)
    
    # *gram21_8* updates
    if gram21_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram21_8.frameNStart = frameN  # exact frame index
        gram21_8.tStart = t  # local t and not account for scr refresh
        gram21_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram21_8, 'tStartRefresh')  # time at next scr refresh
        gram21_8.setAutoDraw(True)
    
    # *gram22_8* updates
    if gram22_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram22_8.frameNStart = frameN  # exact frame index
        gram22_8.tStart = t  # local t and not account for scr refresh
        gram22_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram22_8, 'tStartRefresh')  # time at next scr refresh
        gram22_8.setAutoDraw(True)
    
    # *gram23_8* updates
    if gram23_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram23_8.frameNStart = frameN  # exact frame index
        gram23_8.tStart = t  # local t and not account for scr refresh
        gram23_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram23_8, 'tStartRefresh')  # time at next scr refresh
        gram23_8.setAutoDraw(True)
    
    # *gram24_8* updates
    if gram24_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram24_8.frameNStart = frameN  # exact frame index
        gram24_8.tStart = t  # local t and not account for scr refresh
        gram24_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram24_8, 'tStartRefresh')  # time at next scr refresh
        gram24_8.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial_6_answerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial_6_answer"-------
for thisComponent in trial_6_answerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('one_12.started', one_12.tStartRefresh)
thisExp.addData('one_12.stopped', one_12.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = mouse_14.getPos()
buttons = mouse_14.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    for obj in [continue_text,]:
        if obj.contains(mouse_14):
            gotValidClick = True
            mouse_14.clicked_name.append(obj.name)
thisExp.addData('mouse_14.x', x)
thisExp.addData('mouse_14.y', y)
thisExp.addData('mouse_14.leftButton', buttons[0])
thisExp.addData('mouse_14.midButton', buttons[1])
thisExp.addData('mouse_14.rightButton', buttons[2])
if len(mouse_14.clicked_name):
    thisExp.addData('mouse_14.clicked_name', mouse_14.clicked_name[0])
thisExp.addData('mouse_14.started', mouse_14.tStart)
thisExp.addData('mouse_14.stopped', mouse_14.tStop)
thisExp.nextEntry()
thisExp.addData('two_12.started', two_12.tStartRefresh)
thisExp.addData('two_12.stopped', two_12.tStopRefresh)
thisExp.addData('three_12.started', three_12.tStartRefresh)
thisExp.addData('three_12.stopped', three_12.tStopRefresh)
thisExp.addData('seven_12.started', seven_12.tStartRefresh)
thisExp.addData('seven_12.stopped', seven_12.tStopRefresh)
thisExp.addData('eight_12.started', eight_12.tStartRefresh)
thisExp.addData('eight_12.stopped', eight_12.tStopRefresh)
thisExp.addData('nine_12.started', nine_12.tStartRefresh)
thisExp.addData('nine_12.stopped', nine_12.tStopRefresh)
thisExp.addData('four_12.started', four_12.tStartRefresh)
thisExp.addData('four_12.stopped', four_12.tStopRefresh)
thisExp.addData('five_12.started', five_12.tStartRefresh)
thisExp.addData('five_12.stopped', five_12.tStopRefresh)
thisExp.addData('six_12.started', six_12.tStartRefresh)
thisExp.addData('six_12.stopped', six_12.tStopRefresh)
thisExp.addData('ten_12.started', ten_12.tStartRefresh)
thisExp.addData('ten_12.stopped', ten_12.tStopRefresh)
thisExp.addData('eleven_12.started', eleven_12.tStartRefresh)
thisExp.addData('eleven_12.stopped', eleven_12.tStopRefresh)
thisExp.addData('twelve_12.started', twelve_12.tStartRefresh)
thisExp.addData('twelve_12.stopped', twelve_12.tStopRefresh)
continue_instr.autoDraw = False
thisExp.addData('gram13_8.started', gram13_8.tStartRefresh)
thisExp.addData('gram13_8.stopped', gram13_8.tStopRefresh)
thisExp.addData('gram14_8.started', gram14_8.tStartRefresh)
thisExp.addData('gram14_8.stopped', gram14_8.tStopRefresh)
thisExp.addData('gram15_8.started', gram15_8.tStartRefresh)
thisExp.addData('gram15_8.stopped', gram15_8.tStopRefresh)
thisExp.addData('gram16_8.started', gram16_8.tStartRefresh)
thisExp.addData('gram16_8.stopped', gram16_8.tStopRefresh)
thisExp.addData('gram17_8.started', gram17_8.tStartRefresh)
thisExp.addData('gram17_8.stopped', gram17_8.tStopRefresh)
thisExp.addData('gram18_8.started', gram18_8.tStartRefresh)
thisExp.addData('gram18_8.stopped', gram18_8.tStopRefresh)
thisExp.addData('gram19_8.started', gram19_8.tStartRefresh)
thisExp.addData('gram19_8.stopped', gram19_8.tStopRefresh)
thisExp.addData('gram20_8.started', gram20_8.tStartRefresh)
thisExp.addData('gram20_8.stopped', gram20_8.tStopRefresh)
thisExp.addData('gram21_8.started', gram21_8.tStartRefresh)
thisExp.addData('gram21_8.stopped', gram21_8.tStopRefresh)
thisExp.addData('gram22_8.started', gram22_8.tStartRefresh)
thisExp.addData('gram22_8.stopped', gram22_8.tStopRefresh)
thisExp.addData('gram23_8.started', gram23_8.tStartRefresh)
thisExp.addData('gram23_8.stopped', gram23_8.tStopRefresh)
thisExp.addData('gram24_8.started', gram24_8.tStartRefresh)
thisExp.addData('gram24_8.stopped', gram24_8.tStopRefresh)
# the Routine "trial_6_answer" was not non-slip safe, so reset the non-slip timer
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

# ------Prepare to start Routine "trial_answer"-------
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_9
mouse_9.clicked_name = []
gotValidClick = False  # until a click is received
pieces = [gram01_4,gram02_4,gram03_4,gram04_4,gram05_4,gram06_4,gram07_4,gram08_4,gram09_4,gram10_4,gram11_4,gram12_4]
picked = []
movingPiece = None

    # this works, it keeps track of what trial it is
    # so in win_checker() add an if statement
        # if this_trial is specific trial
        # change what hitboxes takes in as its 2nd argument
        # depending on the winstate order

continue_instr.autoDraw = True

def win_checker()->bool:
    order = [hitbox_checker("one", gram08_4), 
                    hitbox_checker("two", gram04_4),
                    hitbox_checker("three", gram07_4),
                    hitbox_checker("four", gram02_4),
                    hitbox_checker("five", gram01_4),
                    hitbox_checker("six", gram05_4),
                    hitbox_checker("seven", gram10_4),
                    hitbox_checker("eight", gram09_4),
                    hitbox_checker("nine", gram03_4),
                    hitbox_checker("ten", gram12_4),
                    hitbox_checker("eleven", gram06_4),
                    hitbox_checker("twelve", gram11_4)]
    if all(order):
        return True

trial_time = []
# keep track of which components have finished
trial_answerComponents = [one_7, mouse_9, two_7, three_7, seven_7, eight_7, nine_7, four_7, five_7, six_7, ten_7, eleven_7, twelve_7, gram01_4, gram02_4, gram03_4, gram04_4, gram05_4, gram06_4, gram07_4, gram08_4, gram09_4, gram10_4, gram11_4, gram12_4]
for thisComponent in trial_answerComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial_answerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "trial_answer"-------
while continueRoutine:
    # get current time
    t = trial_answerClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial_answerClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *one_7* updates
    if one_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        one_7.frameNStart = frameN  # exact frame index
        one_7.tStart = t  # local t and not account for scr refresh
        one_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(one_7, 'tStartRefresh')  # time at next scr refresh
        one_7.setAutoDraw(True)
    # *mouse_9* updates
    if mouse_9.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_9.frameNStart = frameN  # exact frame index
        mouse_9.tStart = t  # local t and not account for scr refresh
        mouse_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_9, 'tStartRefresh')  # time at next scr refresh
        mouse_9.status = STARTED
        mouse_9.mouseClock.reset()
        prevButtonState = mouse_9.getPressed()  # if button is down already this ISN'T a new click
    if mouse_9.status == STARTED:  # only update if started and not finished!
        buttons = mouse_9.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [continue_text,]:
                    if obj.contains(mouse_9):
                        gotValidClick = True
                        mouse_9.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # *two_7* updates
    if two_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        two_7.frameNStart = frameN  # exact frame index
        two_7.tStart = t  # local t and not account for scr refresh
        two_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(two_7, 'tStartRefresh')  # time at next scr refresh
        two_7.setAutoDraw(True)
    
    # *three_7* updates
    if three_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        three_7.frameNStart = frameN  # exact frame index
        three_7.tStart = t  # local t and not account for scr refresh
        three_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(three_7, 'tStartRefresh')  # time at next scr refresh
        three_7.setAutoDraw(True)
    
    # *seven_7* updates
    if seven_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        seven_7.frameNStart = frameN  # exact frame index
        seven_7.tStart = t  # local t and not account for scr refresh
        seven_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(seven_7, 'tStartRefresh')  # time at next scr refresh
        seven_7.setAutoDraw(True)
    
    # *eight_7* updates
    if eight_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        eight_7.frameNStart = frameN  # exact frame index
        eight_7.tStart = t  # local t and not account for scr refresh
        eight_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(eight_7, 'tStartRefresh')  # time at next scr refresh
        eight_7.setAutoDraw(True)
    
    # *nine_7* updates
    if nine_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        nine_7.frameNStart = frameN  # exact frame index
        nine_7.tStart = t  # local t and not account for scr refresh
        nine_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(nine_7, 'tStartRefresh')  # time at next scr refresh
        nine_7.setAutoDraw(True)
    
    # *four_7* updates
    if four_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        four_7.frameNStart = frameN  # exact frame index
        four_7.tStart = t  # local t and not account for scr refresh
        four_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(four_7, 'tStartRefresh')  # time at next scr refresh
        four_7.setAutoDraw(True)
    
    # *five_7* updates
    if five_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        five_7.frameNStart = frameN  # exact frame index
        five_7.tStart = t  # local t and not account for scr refresh
        five_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(five_7, 'tStartRefresh')  # time at next scr refresh
        five_7.setAutoDraw(True)
    
    # *six_7* updates
    if six_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        six_7.frameNStart = frameN  # exact frame index
        six_7.tStart = t  # local t and not account for scr refresh
        six_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(six_7, 'tStartRefresh')  # time at next scr refresh
        six_7.setAutoDraw(True)
    
    # *ten_7* updates
    if ten_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ten_7.frameNStart = frameN  # exact frame index
        ten_7.tStart = t  # local t and not account for scr refresh
        ten_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ten_7, 'tStartRefresh')  # time at next scr refresh
        ten_7.setAutoDraw(True)
    
    # *eleven_7* updates
    if eleven_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        eleven_7.frameNStart = frameN  # exact frame index
        eleven_7.tStart = t  # local t and not account for scr refresh
        eleven_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(eleven_7, 'tStartRefresh')  # time at next scr refresh
        eleven_7.setAutoDraw(True)
    
    # *twelve_7* updates
    if twelve_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        twelve_7.frameNStart = frameN  # exact frame index
        twelve_7.tStart = t  # local t and not account for scr refresh
        twelve_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(twelve_7, 'tStartRefresh')  # time at next scr refresh
        twelve_7.setAutoDraw(True)
    for piece in pieces:
        if mouse.isPressedIn(piece) and movingPiece is None:
            picked.append(piece)
    
    movingPiece = movePicked(picked, mouse, movingPiece)
    
    win_state = False
    
    win_state = win_checker()
    
    
    # in begin routine, create a function that will check if
    # all the tangrams are in the correct spot
    # if they are, then have it return true and draw continue_text
    
    if win_state:
        continue_text = win_continue()
        continue_text.draw()
    else: 
        win.flip()
    
    
    #if mouse.isPressedIn(polygon):
    #    crosses.append(makeCross(mouse.getPos()))
    
    # *gram01_4* updates
    if gram01_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram01_4.frameNStart = frameN  # exact frame index
        gram01_4.tStart = t  # local t and not account for scr refresh
        gram01_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram01_4, 'tStartRefresh')  # time at next scr refresh
        gram01_4.setAutoDraw(True)
    
    # *gram02_4* updates
    if gram02_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram02_4.frameNStart = frameN  # exact frame index
        gram02_4.tStart = t  # local t and not account for scr refresh
        gram02_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram02_4, 'tStartRefresh')  # time at next scr refresh
        gram02_4.setAutoDraw(True)
    
    # *gram03_4* updates
    if gram03_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram03_4.frameNStart = frameN  # exact frame index
        gram03_4.tStart = t  # local t and not account for scr refresh
        gram03_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram03_4, 'tStartRefresh')  # time at next scr refresh
        gram03_4.setAutoDraw(True)
    
    # *gram04_4* updates
    if gram04_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram04_4.frameNStart = frameN  # exact frame index
        gram04_4.tStart = t  # local t and not account for scr refresh
        gram04_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram04_4, 'tStartRefresh')  # time at next scr refresh
        gram04_4.setAutoDraw(True)
    
    # *gram05_4* updates
    if gram05_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram05_4.frameNStart = frameN  # exact frame index
        gram05_4.tStart = t  # local t and not account for scr refresh
        gram05_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram05_4, 'tStartRefresh')  # time at next scr refresh
        gram05_4.setAutoDraw(True)
    
    # *gram06_4* updates
    if gram06_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram06_4.frameNStart = frameN  # exact frame index
        gram06_4.tStart = t  # local t and not account for scr refresh
        gram06_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram06_4, 'tStartRefresh')  # time at next scr refresh
        gram06_4.setAutoDraw(True)
    
    # *gram07_4* updates
    if gram07_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram07_4.frameNStart = frameN  # exact frame index
        gram07_4.tStart = t  # local t and not account for scr refresh
        gram07_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram07_4, 'tStartRefresh')  # time at next scr refresh
        gram07_4.setAutoDraw(True)
    
    # *gram08_4* updates
    if gram08_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram08_4.frameNStart = frameN  # exact frame index
        gram08_4.tStart = t  # local t and not account for scr refresh
        gram08_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram08_4, 'tStartRefresh')  # time at next scr refresh
        gram08_4.setAutoDraw(True)
    
    # *gram09_4* updates
    if gram09_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram09_4.frameNStart = frameN  # exact frame index
        gram09_4.tStart = t  # local t and not account for scr refresh
        gram09_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram09_4, 'tStartRefresh')  # time at next scr refresh
        gram09_4.setAutoDraw(True)
    
    # *gram10_4* updates
    if gram10_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram10_4.frameNStart = frameN  # exact frame index
        gram10_4.tStart = t  # local t and not account for scr refresh
        gram10_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram10_4, 'tStartRefresh')  # time at next scr refresh
        gram10_4.setAutoDraw(True)
    
    # *gram11_4* updates
    if gram11_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram11_4.frameNStart = frameN  # exact frame index
        gram11_4.tStart = t  # local t and not account for scr refresh
        gram11_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram11_4, 'tStartRefresh')  # time at next scr refresh
        gram11_4.setAutoDraw(True)
    
    # *gram12_4* updates
    if gram12_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram12_4.frameNStart = frameN  # exact frame index
        gram12_4.tStart = t  # local t and not account for scr refresh
        gram12_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram12_4, 'tStartRefresh')  # time at next scr refresh
        gram12_4.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial_answerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial_answer"-------
for thisComponent in trial_answerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('one_7.started', one_7.tStartRefresh)
thisExp.addData('one_7.stopped', one_7.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = mouse_9.getPos()
buttons = mouse_9.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    for obj in [continue_text,]:
        if obj.contains(mouse_9):
            gotValidClick = True
            mouse_9.clicked_name.append(obj.name)
thisExp.addData('mouse_9.x', x)
thisExp.addData('mouse_9.y', y)
thisExp.addData('mouse_9.leftButton', buttons[0])
thisExp.addData('mouse_9.midButton', buttons[1])
thisExp.addData('mouse_9.rightButton', buttons[2])
if len(mouse_9.clicked_name):
    thisExp.addData('mouse_9.clicked_name', mouse_9.clicked_name[0])
thisExp.addData('mouse_9.started', mouse_9.tStart)
thisExp.addData('mouse_9.stopped', mouse_9.tStop)
thisExp.nextEntry()
thisExp.addData('two_7.started', two_7.tStartRefresh)
thisExp.addData('two_7.stopped', two_7.tStopRefresh)
thisExp.addData('three_7.started', three_7.tStartRefresh)
thisExp.addData('three_7.stopped', three_7.tStopRefresh)
thisExp.addData('seven_7.started', seven_7.tStartRefresh)
thisExp.addData('seven_7.stopped', seven_7.tStopRefresh)
thisExp.addData('eight_7.started', eight_7.tStartRefresh)
thisExp.addData('eight_7.stopped', eight_7.tStopRefresh)
thisExp.addData('nine_7.started', nine_7.tStartRefresh)
thisExp.addData('nine_7.stopped', nine_7.tStopRefresh)
thisExp.addData('four_7.started', four_7.tStartRefresh)
thisExp.addData('four_7.stopped', four_7.tStopRefresh)
thisExp.addData('five_7.started', five_7.tStartRefresh)
thisExp.addData('five_7.stopped', five_7.tStopRefresh)
thisExp.addData('six_7.started', six_7.tStartRefresh)
thisExp.addData('six_7.stopped', six_7.tStopRefresh)
thisExp.addData('ten_7.started', ten_7.tStartRefresh)
thisExp.addData('ten_7.stopped', ten_7.tStopRefresh)
thisExp.addData('eleven_7.started', eleven_7.tStartRefresh)
thisExp.addData('eleven_7.stopped', eleven_7.tStopRefresh)
thisExp.addData('twelve_7.started', twelve_7.tStartRefresh)
thisExp.addData('twelve_7.stopped', twelve_7.tStopRefresh)
thisExp.addData('gram01_4.started', gram01_4.tStartRefresh)
thisExp.addData('gram01_4.stopped', gram01_4.tStopRefresh)
thisExp.addData('gram02_4.started', gram02_4.tStartRefresh)
thisExp.addData('gram02_4.stopped', gram02_4.tStopRefresh)
thisExp.addData('gram03_4.started', gram03_4.tStartRefresh)
thisExp.addData('gram03_4.stopped', gram03_4.tStopRefresh)
thisExp.addData('gram04_4.started', gram04_4.tStartRefresh)
thisExp.addData('gram04_4.stopped', gram04_4.tStopRefresh)
thisExp.addData('gram05_4.started', gram05_4.tStartRefresh)
thisExp.addData('gram05_4.stopped', gram05_4.tStopRefresh)
thisExp.addData('gram06_4.started', gram06_4.tStartRefresh)
thisExp.addData('gram06_4.stopped', gram06_4.tStopRefresh)
thisExp.addData('gram07_4.started', gram07_4.tStartRefresh)
thisExp.addData('gram07_4.stopped', gram07_4.tStopRefresh)
thisExp.addData('gram08_4.started', gram08_4.tStartRefresh)
thisExp.addData('gram08_4.stopped', gram08_4.tStopRefresh)
thisExp.addData('gram09_4.started', gram09_4.tStartRefresh)
thisExp.addData('gram09_4.stopped', gram09_4.tStopRefresh)
thisExp.addData('gram10_4.started', gram10_4.tStartRefresh)
thisExp.addData('gram10_4.stopped', gram10_4.tStopRefresh)
thisExp.addData('gram11_4.started', gram11_4.tStartRefresh)
thisExp.addData('gram11_4.stopped', gram11_4.tStopRefresh)
thisExp.addData('gram12_4.started', gram12_4.tStartRefresh)
thisExp.addData('gram12_4.stopped', gram12_4.tStopRefresh)
# the Routine "trial_answer" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trial_2_answer"-------
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_10
mouse_10.clicked_name = []
gotValidClick = False  # until a click is received
pieces = [gram01_5,gram02_5,gram03_5,gram04_5,gram05_5,gram06_5,gram07_5,gram08_5,gram09_5,gram10_5,gram11_5,gram12_5]
picked = []
movingPiece = None

    # this works, it keeps track of what trial it is
    # so in win_checker() add an if statement
        # if this_trial is specific trial
        # change what hitboxes takes in as its 2nd argument
        # depending on the winstate order


def win_checker()->bool:
    order = [hitbox_checker("one", gram10_5), 
                    hitbox_checker("two", gram09_5),
                    hitbox_checker("three", gram07_5),
                    hitbox_checker("four", gram03_5),
                    hitbox_checker("five", gram12_5),
                    hitbox_checker("six", gram02_5),
                    hitbox_checker("seven", gram08_5),
                    hitbox_checker("eight", gram11_5),
                    hitbox_checker("nine", gram04_5),
                    hitbox_checker("ten", gram05_5),
                    hitbox_checker("eleven", gram06_5),
                    hitbox_checker("twelve", gram01_5)]
    if all(order):
        return True

trial_time = []
# keep track of which components have finished
trial_2_answerComponents = [one_8, mouse_10, two_8, three_8, seven_8, eight_8, nine_8, four_8, five_8, six_8, ten_8, eleven_8, twelve_8, gram01_5, gram02_5, gram03_5, gram04_5, gram05_5, gram06_5, gram07_5, gram08_5, gram09_5, gram10_5, gram11_5, gram12_5]
for thisComponent in trial_2_answerComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial_2_answerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "trial_2_answer"-------
while continueRoutine:
    # get current time
    t = trial_2_answerClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial_2_answerClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *one_8* updates
    if one_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        one_8.frameNStart = frameN  # exact frame index
        one_8.tStart = t  # local t and not account for scr refresh
        one_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(one_8, 'tStartRefresh')  # time at next scr refresh
        one_8.setAutoDraw(True)
    # *mouse_10* updates
    if mouse_10.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_10.frameNStart = frameN  # exact frame index
        mouse_10.tStart = t  # local t and not account for scr refresh
        mouse_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_10, 'tStartRefresh')  # time at next scr refresh
        mouse_10.status = STARTED
        mouse_10.mouseClock.reset()
        prevButtonState = mouse_10.getPressed()  # if button is down already this ISN'T a new click
    if mouse_10.status == STARTED:  # only update if started and not finished!
        buttons = mouse_10.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [continue_text,]:
                    if obj.contains(mouse_10):
                        gotValidClick = True
                        mouse_10.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # *two_8* updates
    if two_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        two_8.frameNStart = frameN  # exact frame index
        two_8.tStart = t  # local t and not account for scr refresh
        two_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(two_8, 'tStartRefresh')  # time at next scr refresh
        two_8.setAutoDraw(True)
    
    # *three_8* updates
    if three_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        three_8.frameNStart = frameN  # exact frame index
        three_8.tStart = t  # local t and not account for scr refresh
        three_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(three_8, 'tStartRefresh')  # time at next scr refresh
        three_8.setAutoDraw(True)
    
    # *seven_8* updates
    if seven_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        seven_8.frameNStart = frameN  # exact frame index
        seven_8.tStart = t  # local t and not account for scr refresh
        seven_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(seven_8, 'tStartRefresh')  # time at next scr refresh
        seven_8.setAutoDraw(True)
    
    # *eight_8* updates
    if eight_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        eight_8.frameNStart = frameN  # exact frame index
        eight_8.tStart = t  # local t and not account for scr refresh
        eight_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(eight_8, 'tStartRefresh')  # time at next scr refresh
        eight_8.setAutoDraw(True)
    
    # *nine_8* updates
    if nine_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        nine_8.frameNStart = frameN  # exact frame index
        nine_8.tStart = t  # local t and not account for scr refresh
        nine_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(nine_8, 'tStartRefresh')  # time at next scr refresh
        nine_8.setAutoDraw(True)
    
    # *four_8* updates
    if four_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        four_8.frameNStart = frameN  # exact frame index
        four_8.tStart = t  # local t and not account for scr refresh
        four_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(four_8, 'tStartRefresh')  # time at next scr refresh
        four_8.setAutoDraw(True)
    
    # *five_8* updates
    if five_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        five_8.frameNStart = frameN  # exact frame index
        five_8.tStart = t  # local t and not account for scr refresh
        five_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(five_8, 'tStartRefresh')  # time at next scr refresh
        five_8.setAutoDraw(True)
    
    # *six_8* updates
    if six_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        six_8.frameNStart = frameN  # exact frame index
        six_8.tStart = t  # local t and not account for scr refresh
        six_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(six_8, 'tStartRefresh')  # time at next scr refresh
        six_8.setAutoDraw(True)
    
    # *ten_8* updates
    if ten_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ten_8.frameNStart = frameN  # exact frame index
        ten_8.tStart = t  # local t and not account for scr refresh
        ten_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ten_8, 'tStartRefresh')  # time at next scr refresh
        ten_8.setAutoDraw(True)
    
    # *eleven_8* updates
    if eleven_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        eleven_8.frameNStart = frameN  # exact frame index
        eleven_8.tStart = t  # local t and not account for scr refresh
        eleven_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(eleven_8, 'tStartRefresh')  # time at next scr refresh
        eleven_8.setAutoDraw(True)
    
    # *twelve_8* updates
    if twelve_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        twelve_8.frameNStart = frameN  # exact frame index
        twelve_8.tStart = t  # local t and not account for scr refresh
        twelve_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(twelve_8, 'tStartRefresh')  # time at next scr refresh
        twelve_8.setAutoDraw(True)
    for piece in pieces:
        if mouse.isPressedIn(piece) and movingPiece is None:
            picked.append(piece)
    
    movingPiece = movePicked(picked, mouse, movingPiece)
    
    win_state = False
    
    
    win_state = win_checker()
    
    
    # in begin routine, create a function that will check if
    # all the tangrams are in the correct spot
    # if they are, then have it return true and draw continue_text
    
    if win_state:
        continue_text = win_continue()
        continue_text.draw()
    else: 
        win.flip()
    
    
    #if mouse.isPressedIn(polygon):
    #    crosses.append(makeCross(mouse.getPos()))
    
    # *gram01_5* updates
    if gram01_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram01_5.frameNStart = frameN  # exact frame index
        gram01_5.tStart = t  # local t and not account for scr refresh
        gram01_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram01_5, 'tStartRefresh')  # time at next scr refresh
        gram01_5.setAutoDraw(True)
    
    # *gram02_5* updates
    if gram02_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram02_5.frameNStart = frameN  # exact frame index
        gram02_5.tStart = t  # local t and not account for scr refresh
        gram02_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram02_5, 'tStartRefresh')  # time at next scr refresh
        gram02_5.setAutoDraw(True)
    
    # *gram03_5* updates
    if gram03_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram03_5.frameNStart = frameN  # exact frame index
        gram03_5.tStart = t  # local t and not account for scr refresh
        gram03_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram03_5, 'tStartRefresh')  # time at next scr refresh
        gram03_5.setAutoDraw(True)
    
    # *gram04_5* updates
    if gram04_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram04_5.frameNStart = frameN  # exact frame index
        gram04_5.tStart = t  # local t and not account for scr refresh
        gram04_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram04_5, 'tStartRefresh')  # time at next scr refresh
        gram04_5.setAutoDraw(True)
    
    # *gram05_5* updates
    if gram05_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram05_5.frameNStart = frameN  # exact frame index
        gram05_5.tStart = t  # local t and not account for scr refresh
        gram05_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram05_5, 'tStartRefresh')  # time at next scr refresh
        gram05_5.setAutoDraw(True)
    
    # *gram06_5* updates
    if gram06_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram06_5.frameNStart = frameN  # exact frame index
        gram06_5.tStart = t  # local t and not account for scr refresh
        gram06_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram06_5, 'tStartRefresh')  # time at next scr refresh
        gram06_5.setAutoDraw(True)
    
    # *gram07_5* updates
    if gram07_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram07_5.frameNStart = frameN  # exact frame index
        gram07_5.tStart = t  # local t and not account for scr refresh
        gram07_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram07_5, 'tStartRefresh')  # time at next scr refresh
        gram07_5.setAutoDraw(True)
    
    # *gram08_5* updates
    if gram08_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram08_5.frameNStart = frameN  # exact frame index
        gram08_5.tStart = t  # local t and not account for scr refresh
        gram08_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram08_5, 'tStartRefresh')  # time at next scr refresh
        gram08_5.setAutoDraw(True)
    
    # *gram09_5* updates
    if gram09_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram09_5.frameNStart = frameN  # exact frame index
        gram09_5.tStart = t  # local t and not account for scr refresh
        gram09_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram09_5, 'tStartRefresh')  # time at next scr refresh
        gram09_5.setAutoDraw(True)
    
    # *gram10_5* updates
    if gram10_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram10_5.frameNStart = frameN  # exact frame index
        gram10_5.tStart = t  # local t and not account for scr refresh
        gram10_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram10_5, 'tStartRefresh')  # time at next scr refresh
        gram10_5.setAutoDraw(True)
    
    # *gram11_5* updates
    if gram11_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram11_5.frameNStart = frameN  # exact frame index
        gram11_5.tStart = t  # local t and not account for scr refresh
        gram11_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram11_5, 'tStartRefresh')  # time at next scr refresh
        gram11_5.setAutoDraw(True)
    
    # *gram12_5* updates
    if gram12_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram12_5.frameNStart = frameN  # exact frame index
        gram12_5.tStart = t  # local t and not account for scr refresh
        gram12_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram12_5, 'tStartRefresh')  # time at next scr refresh
        gram12_5.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial_2_answerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial_2_answer"-------
for thisComponent in trial_2_answerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('one_8.started', one_8.tStartRefresh)
thisExp.addData('one_8.stopped', one_8.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = mouse_10.getPos()
buttons = mouse_10.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    for obj in [continue_text,]:
        if obj.contains(mouse_10):
            gotValidClick = True
            mouse_10.clicked_name.append(obj.name)
thisExp.addData('mouse_10.x', x)
thisExp.addData('mouse_10.y', y)
thisExp.addData('mouse_10.leftButton', buttons[0])
thisExp.addData('mouse_10.midButton', buttons[1])
thisExp.addData('mouse_10.rightButton', buttons[2])
if len(mouse_10.clicked_name):
    thisExp.addData('mouse_10.clicked_name', mouse_10.clicked_name[0])
thisExp.addData('mouse_10.started', mouse_10.tStart)
thisExp.addData('mouse_10.stopped', mouse_10.tStop)
thisExp.nextEntry()
thisExp.addData('two_8.started', two_8.tStartRefresh)
thisExp.addData('two_8.stopped', two_8.tStopRefresh)
thisExp.addData('three_8.started', three_8.tStartRefresh)
thisExp.addData('three_8.stopped', three_8.tStopRefresh)
thisExp.addData('seven_8.started', seven_8.tStartRefresh)
thisExp.addData('seven_8.stopped', seven_8.tStopRefresh)
thisExp.addData('eight_8.started', eight_8.tStartRefresh)
thisExp.addData('eight_8.stopped', eight_8.tStopRefresh)
thisExp.addData('nine_8.started', nine_8.tStartRefresh)
thisExp.addData('nine_8.stopped', nine_8.tStopRefresh)
thisExp.addData('four_8.started', four_8.tStartRefresh)
thisExp.addData('four_8.stopped', four_8.tStopRefresh)
thisExp.addData('five_8.started', five_8.tStartRefresh)
thisExp.addData('five_8.stopped', five_8.tStopRefresh)
thisExp.addData('six_8.started', six_8.tStartRefresh)
thisExp.addData('six_8.stopped', six_8.tStopRefresh)
thisExp.addData('ten_8.started', ten_8.tStartRefresh)
thisExp.addData('ten_8.stopped', ten_8.tStopRefresh)
thisExp.addData('eleven_8.started', eleven_8.tStartRefresh)
thisExp.addData('eleven_8.stopped', eleven_8.tStopRefresh)
thisExp.addData('twelve_8.started', twelve_8.tStartRefresh)
thisExp.addData('twelve_8.stopped', twelve_8.tStopRefresh)
thisExp.addData('gram01_5.started', gram01_5.tStartRefresh)
thisExp.addData('gram01_5.stopped', gram01_5.tStopRefresh)
thisExp.addData('gram02_5.started', gram02_5.tStartRefresh)
thisExp.addData('gram02_5.stopped', gram02_5.tStopRefresh)
thisExp.addData('gram03_5.started', gram03_5.tStartRefresh)
thisExp.addData('gram03_5.stopped', gram03_5.tStopRefresh)
thisExp.addData('gram04_5.started', gram04_5.tStartRefresh)
thisExp.addData('gram04_5.stopped', gram04_5.tStopRefresh)
thisExp.addData('gram05_5.started', gram05_5.tStartRefresh)
thisExp.addData('gram05_5.stopped', gram05_5.tStopRefresh)
thisExp.addData('gram06_5.started', gram06_5.tStartRefresh)
thisExp.addData('gram06_5.stopped', gram06_5.tStopRefresh)
thisExp.addData('gram07_5.started', gram07_5.tStartRefresh)
thisExp.addData('gram07_5.stopped', gram07_5.tStopRefresh)
thisExp.addData('gram08_5.started', gram08_5.tStartRefresh)
thisExp.addData('gram08_5.stopped', gram08_5.tStopRefresh)
thisExp.addData('gram09_5.started', gram09_5.tStartRefresh)
thisExp.addData('gram09_5.stopped', gram09_5.tStopRefresh)
thisExp.addData('gram10_5.started', gram10_5.tStartRefresh)
thisExp.addData('gram10_5.stopped', gram10_5.tStopRefresh)
thisExp.addData('gram11_5.started', gram11_5.tStartRefresh)
thisExp.addData('gram11_5.stopped', gram11_5.tStopRefresh)
thisExp.addData('gram12_5.started', gram12_5.tStartRefresh)
thisExp.addData('gram12_5.stopped', gram12_5.tStopRefresh)
# the Routine "trial_2_answer" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trial_3_answer"-------
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_11
mouse_11.clicked_name = []
gotValidClick = False  # until a click is received
pieces = [gram01_6,gram02_6,gram03_6,gram04_6,gram05_6,gram06_6,gram07_6,gram08_6,gram09_6,gram10_6,gram11_6,gram12_6]
picked = []
movingPiece = None

    # this works, it keeps track of what trial it is
    # so in win_checker() add an if statement
        # if this_trial is specific trial
        # change what hitboxes takes in as its 2nd argument
        # depending on the winstate order


def win_checker()->bool:
    order = [hitbox_checker("one", gram02_6), 
                    hitbox_checker("two", gram11_6),
                    hitbox_checker("three", gram01_6),
                    hitbox_checker("four", gram04_6),
                    hitbox_checker("five", gram08_6),
                    hitbox_checker("six", gram03_6),
                    hitbox_checker("seven", gram10_6),
                    hitbox_checker("eight", gram09_6),
                    hitbox_checker("nine", gram12_6),
                    hitbox_checker("ten", gram05_6),
                    hitbox_checker("eleven", gram07_6),
                    hitbox_checker("twelve", gram06_6)]
    if all(order):
        return True
# keep track of which components have finished
trial_3_answerComponents = [one_9, mouse_11, two_9, three_9, seven_9, eight_9, nine_9, four_9, five_9, six_9, ten_9, eleven_9, twelve_9, gram01_6, gram02_6, gram03_6, gram04_6, gram05_6, gram06_6, gram07_6, gram08_6, gram09_6, gram10_6, gram11_6, gram12_6]
for thisComponent in trial_3_answerComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial_3_answerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "trial_3_answer"-------
while continueRoutine:
    # get current time
    t = trial_3_answerClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial_3_answerClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *one_9* updates
    if one_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        one_9.frameNStart = frameN  # exact frame index
        one_9.tStart = t  # local t and not account for scr refresh
        one_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(one_9, 'tStartRefresh')  # time at next scr refresh
        one_9.setAutoDraw(True)
    # *mouse_11* updates
    if mouse_11.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_11.frameNStart = frameN  # exact frame index
        mouse_11.tStart = t  # local t and not account for scr refresh
        mouse_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_11, 'tStartRefresh')  # time at next scr refresh
        mouse_11.status = STARTED
        mouse_11.mouseClock.reset()
        prevButtonState = mouse_11.getPressed()  # if button is down already this ISN'T a new click
    if mouse_11.status == STARTED:  # only update if started and not finished!
        buttons = mouse_11.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [continue_text,]:
                    if obj.contains(mouse_11):
                        gotValidClick = True
                        mouse_11.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # *two_9* updates
    if two_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        two_9.frameNStart = frameN  # exact frame index
        two_9.tStart = t  # local t and not account for scr refresh
        two_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(two_9, 'tStartRefresh')  # time at next scr refresh
        two_9.setAutoDraw(True)
    
    # *three_9* updates
    if three_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        three_9.frameNStart = frameN  # exact frame index
        three_9.tStart = t  # local t and not account for scr refresh
        three_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(three_9, 'tStartRefresh')  # time at next scr refresh
        three_9.setAutoDraw(True)
    
    # *seven_9* updates
    if seven_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        seven_9.frameNStart = frameN  # exact frame index
        seven_9.tStart = t  # local t and not account for scr refresh
        seven_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(seven_9, 'tStartRefresh')  # time at next scr refresh
        seven_9.setAutoDraw(True)
    
    # *eight_9* updates
    if eight_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        eight_9.frameNStart = frameN  # exact frame index
        eight_9.tStart = t  # local t and not account for scr refresh
        eight_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(eight_9, 'tStartRefresh')  # time at next scr refresh
        eight_9.setAutoDraw(True)
    
    # *nine_9* updates
    if nine_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        nine_9.frameNStart = frameN  # exact frame index
        nine_9.tStart = t  # local t and not account for scr refresh
        nine_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(nine_9, 'tStartRefresh')  # time at next scr refresh
        nine_9.setAutoDraw(True)
    
    # *four_9* updates
    if four_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        four_9.frameNStart = frameN  # exact frame index
        four_9.tStart = t  # local t and not account for scr refresh
        four_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(four_9, 'tStartRefresh')  # time at next scr refresh
        four_9.setAutoDraw(True)
    
    # *five_9* updates
    if five_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        five_9.frameNStart = frameN  # exact frame index
        five_9.tStart = t  # local t and not account for scr refresh
        five_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(five_9, 'tStartRefresh')  # time at next scr refresh
        five_9.setAutoDraw(True)
    
    # *six_9* updates
    if six_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        six_9.frameNStart = frameN  # exact frame index
        six_9.tStart = t  # local t and not account for scr refresh
        six_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(six_9, 'tStartRefresh')  # time at next scr refresh
        six_9.setAutoDraw(True)
    
    # *ten_9* updates
    if ten_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ten_9.frameNStart = frameN  # exact frame index
        ten_9.tStart = t  # local t and not account for scr refresh
        ten_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ten_9, 'tStartRefresh')  # time at next scr refresh
        ten_9.setAutoDraw(True)
    
    # *eleven_9* updates
    if eleven_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        eleven_9.frameNStart = frameN  # exact frame index
        eleven_9.tStart = t  # local t and not account for scr refresh
        eleven_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(eleven_9, 'tStartRefresh')  # time at next scr refresh
        eleven_9.setAutoDraw(True)
    
    # *twelve_9* updates
    if twelve_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        twelve_9.frameNStart = frameN  # exact frame index
        twelve_9.tStart = t  # local t and not account for scr refresh
        twelve_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(twelve_9, 'tStartRefresh')  # time at next scr refresh
        twelve_9.setAutoDraw(True)
    for piece in pieces:
        if mouse.isPressedIn(piece) and movingPiece is None:
            picked.append(piece)
    
    movingPiece = movePicked(picked, mouse, movingPiece)
    
    win_state = False
    
    
    win_state = win_checker()
    
    
    # in begin routine, create a function that will check if
    # all the tangrams are in the correct spot
    # if they are, then have it return true and draw continue_text
    
    if win_state:
        continue_text = win_continue()
        continue_text.draw()
    else: 
        win.flip()
    
    
    #if mouse.isPressedIn(polygon):
    #    crosses.append(makeCross(mouse.getPos()))
    
    # *gram01_6* updates
    if gram01_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram01_6.frameNStart = frameN  # exact frame index
        gram01_6.tStart = t  # local t and not account for scr refresh
        gram01_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram01_6, 'tStartRefresh')  # time at next scr refresh
        gram01_6.setAutoDraw(True)
    
    # *gram02_6* updates
    if gram02_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram02_6.frameNStart = frameN  # exact frame index
        gram02_6.tStart = t  # local t and not account for scr refresh
        gram02_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram02_6, 'tStartRefresh')  # time at next scr refresh
        gram02_6.setAutoDraw(True)
    
    # *gram03_6* updates
    if gram03_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram03_6.frameNStart = frameN  # exact frame index
        gram03_6.tStart = t  # local t and not account for scr refresh
        gram03_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram03_6, 'tStartRefresh')  # time at next scr refresh
        gram03_6.setAutoDraw(True)
    
    # *gram04_6* updates
    if gram04_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram04_6.frameNStart = frameN  # exact frame index
        gram04_6.tStart = t  # local t and not account for scr refresh
        gram04_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram04_6, 'tStartRefresh')  # time at next scr refresh
        gram04_6.setAutoDraw(True)
    
    # *gram05_6* updates
    if gram05_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram05_6.frameNStart = frameN  # exact frame index
        gram05_6.tStart = t  # local t and not account for scr refresh
        gram05_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram05_6, 'tStartRefresh')  # time at next scr refresh
        gram05_6.setAutoDraw(True)
    
    # *gram06_6* updates
    if gram06_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram06_6.frameNStart = frameN  # exact frame index
        gram06_6.tStart = t  # local t and not account for scr refresh
        gram06_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram06_6, 'tStartRefresh')  # time at next scr refresh
        gram06_6.setAutoDraw(True)
    
    # *gram07_6* updates
    if gram07_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram07_6.frameNStart = frameN  # exact frame index
        gram07_6.tStart = t  # local t and not account for scr refresh
        gram07_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram07_6, 'tStartRefresh')  # time at next scr refresh
        gram07_6.setAutoDraw(True)
    
    # *gram08_6* updates
    if gram08_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram08_6.frameNStart = frameN  # exact frame index
        gram08_6.tStart = t  # local t and not account for scr refresh
        gram08_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram08_6, 'tStartRefresh')  # time at next scr refresh
        gram08_6.setAutoDraw(True)
    
    # *gram09_6* updates
    if gram09_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram09_6.frameNStart = frameN  # exact frame index
        gram09_6.tStart = t  # local t and not account for scr refresh
        gram09_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram09_6, 'tStartRefresh')  # time at next scr refresh
        gram09_6.setAutoDraw(True)
    
    # *gram10_6* updates
    if gram10_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram10_6.frameNStart = frameN  # exact frame index
        gram10_6.tStart = t  # local t and not account for scr refresh
        gram10_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram10_6, 'tStartRefresh')  # time at next scr refresh
        gram10_6.setAutoDraw(True)
    
    # *gram11_6* updates
    if gram11_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram11_6.frameNStart = frameN  # exact frame index
        gram11_6.tStart = t  # local t and not account for scr refresh
        gram11_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram11_6, 'tStartRefresh')  # time at next scr refresh
        gram11_6.setAutoDraw(True)
    
    # *gram12_6* updates
    if gram12_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gram12_6.frameNStart = frameN  # exact frame index
        gram12_6.tStart = t  # local t and not account for scr refresh
        gram12_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gram12_6, 'tStartRefresh')  # time at next scr refresh
        gram12_6.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial_3_answerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial_3_answer"-------
for thisComponent in trial_3_answerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('one_9.started', one_9.tStartRefresh)
thisExp.addData('one_9.stopped', one_9.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = mouse_11.getPos()
buttons = mouse_11.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    for obj in [continue_text,]:
        if obj.contains(mouse_11):
            gotValidClick = True
            mouse_11.clicked_name.append(obj.name)
thisExp.addData('mouse_11.x', x)
thisExp.addData('mouse_11.y', y)
thisExp.addData('mouse_11.leftButton', buttons[0])
thisExp.addData('mouse_11.midButton', buttons[1])
thisExp.addData('mouse_11.rightButton', buttons[2])
if len(mouse_11.clicked_name):
    thisExp.addData('mouse_11.clicked_name', mouse_11.clicked_name[0])
thisExp.addData('mouse_11.started', mouse_11.tStart)
thisExp.addData('mouse_11.stopped', mouse_11.tStop)
thisExp.nextEntry()
thisExp.addData('two_9.started', two_9.tStartRefresh)
thisExp.addData('two_9.stopped', two_9.tStopRefresh)
thisExp.addData('three_9.started', three_9.tStartRefresh)
thisExp.addData('three_9.stopped', three_9.tStopRefresh)
thisExp.addData('seven_9.started', seven_9.tStartRefresh)
thisExp.addData('seven_9.stopped', seven_9.tStopRefresh)
thisExp.addData('eight_9.started', eight_9.tStartRefresh)
thisExp.addData('eight_9.stopped', eight_9.tStopRefresh)
thisExp.addData('nine_9.started', nine_9.tStartRefresh)
thisExp.addData('nine_9.stopped', nine_9.tStopRefresh)
thisExp.addData('four_9.started', four_9.tStartRefresh)
thisExp.addData('four_9.stopped', four_9.tStopRefresh)
thisExp.addData('five_9.started', five_9.tStartRefresh)
thisExp.addData('five_9.stopped', five_9.tStopRefresh)
thisExp.addData('six_9.started', six_9.tStartRefresh)
thisExp.addData('six_9.stopped', six_9.tStopRefresh)
thisExp.addData('ten_9.started', ten_9.tStartRefresh)
thisExp.addData('ten_9.stopped', ten_9.tStopRefresh)
thisExp.addData('eleven_9.started', eleven_9.tStartRefresh)
thisExp.addData('eleven_9.stopped', eleven_9.tStopRefresh)
thisExp.addData('twelve_9.started', twelve_9.tStartRefresh)
thisExp.addData('twelve_9.stopped', twelve_9.tStopRefresh)
continue_instr.autoDraw = False
thisExp.addData('gram01_6.started', gram01_6.tStartRefresh)
thisExp.addData('gram01_6.stopped', gram01_6.tStopRefresh)
thisExp.addData('gram02_6.started', gram02_6.tStartRefresh)
thisExp.addData('gram02_6.stopped', gram02_6.tStopRefresh)
thisExp.addData('gram03_6.started', gram03_6.tStartRefresh)
thisExp.addData('gram03_6.stopped', gram03_6.tStopRefresh)
thisExp.addData('gram04_6.started', gram04_6.tStartRefresh)
thisExp.addData('gram04_6.stopped', gram04_6.tStopRefresh)
thisExp.addData('gram05_6.started', gram05_6.tStartRefresh)
thisExp.addData('gram05_6.stopped', gram05_6.tStopRefresh)
thisExp.addData('gram06_6.started', gram06_6.tStartRefresh)
thisExp.addData('gram06_6.stopped', gram06_6.tStopRefresh)
thisExp.addData('gram07_6.started', gram07_6.tStartRefresh)
thisExp.addData('gram07_6.stopped', gram07_6.tStopRefresh)
thisExp.addData('gram08_6.started', gram08_6.tStartRefresh)
thisExp.addData('gram08_6.stopped', gram08_6.tStopRefresh)
thisExp.addData('gram09_6.started', gram09_6.tStartRefresh)
thisExp.addData('gram09_6.stopped', gram09_6.tStopRefresh)
thisExp.addData('gram10_6.started', gram10_6.tStartRefresh)
thisExp.addData('gram10_6.stopped', gram10_6.tStopRefresh)
thisExp.addData('gram11_6.started', gram11_6.tStartRefresh)
thisExp.addData('gram11_6.stopped', gram11_6.tStopRefresh)
thisExp.addData('gram12_6.started', gram12_6.tStartRefresh)
thisExp.addData('gram12_6.stopped', gram12_6.tStopRefresh)
# the Routine "trial_3_answer" was not non-slip safe, so reset the non-slip timer
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
