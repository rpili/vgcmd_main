# Initialize components for Routine "trial"
trialClock = core.Clock()
one = visual.ImageStim(
    win=win,
    name='one', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/one.png', mask=None,
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
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/two.png', mask=None,
    ori=0, pos=(-.45, .30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
three = visual.ImageStim(
    win=win,
    name='three', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/three.png', mask=None,
    ori=0, pos=(-0.20, 0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
seven = visual.ImageStim(
    win=win,
    name='seven', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/seven.png', mask=None,
    ori=0, pos=(-0.70, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
eight = visual.ImageStim(
    win=win,
    name='eight', 
    image='/Users/rjpil/OneDrive/GS/CECLAB/vgcmd_main/stimuli/eight.png', mask=None,
    ori=0, pos=(-0.45, -0.30), size=(0.22, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)

    