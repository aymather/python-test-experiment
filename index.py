from psychopy import core, visual, event
import time
import random

win = visual.Window([400, 400], monitor = "testMonitor")
right_arrow = visual.shapeStim(
        win,
        lineWidth = None,
        vertices = ((.7,0),(0,-.5),(0,-.2),(-.5,-.2),(-.5,.2),(0,.2),(0,.5))
    )

left_arrow = visual.shapeStim(
    win,
    lineWidth = None,
    vertices = ((-.7,0),(0,-.5),(0,-.2),(.5,-.2),(.5,.2),(0,.2),(0,.5))
)

numberOfTrials = 5
delay = [200, 250, 300, 350, 400, 450, 500, 550]

for trial in range(numberOfTrials):

    d = random.choice(delay)

    if (random.random() >= .5):
        arrow = right_arrow
        arrow.fillColor = 'black'
    else:
        arrow = left_arrow
        arrow.fillColor = 'black'

    # Draw and flip
    arrow.draw()
    win.flip()
    trialstart = time.time()

    # Wait for a response and print RT/keypressed
    c = event.waitKeys()
    trialend = time.time()
    rt = trialend - trialstart
    print(c)
    print(rt)

    arrow.fillColor = 'red'
    arrow.draw()
    win.flip()

    core.wait(1)

win.flip()
core.quit()

# THIS IS A COMMENT
