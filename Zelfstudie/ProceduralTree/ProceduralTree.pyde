"""
Recursive Tree
by Daniel Shiffman.    

Renders a simple tree-like structure via recursion. 
The branching angle is calculated as a function of 
the horizontal mouse location. Move the mouse left
and right to change the angle.
"""

def setup():
    size(1200, 720)

def draw():
    background(0)
    frameRate(2)
    stroke(255)
    # Let's pick an angle 0 to 90 degrees based on the mouse position
    a = 90*( 0.5 + random(1.0))
    # Convert it to radians
    # Start the tree from the bottom of the screen
    translate(width / 2, height)
    # Draw a line 120 pixels
    stroke(180,120,40)
    branchSize = -240 * 0.5 + random(-60)
    line(0, 0, 0, branchSize)
    # Move to the end of that line
    translate(0, branchSize)
    # Start the recursive branching!
    branch(120, radians(a * 0.5 + random(1.0)))

def branch(h, theta):
    # Each branch will be 2/3rds the size of the previous one
    h *= 0.65 + random(0.12)
    # All recursive functions must have an exit condition!!!!
    # Here, ours is when the length of the branch is 2 pixels or less
    if(random(2)) >= 1:
        stroke(150,255,40)
    else:
        stroke(160,190,40)
    if h > 2 + random(2):
        # Save the current state of transformation (i.e. where are we now)
        pushMatrix()
        rotate(theta * 0.6 + random(0.8))  # Rotate by theta
        line(0, 0, 0, -h)  # Draw the branch
        translate(0, -h * 0.8 + random(0.4))  # Move to the end of the branch
        branch(h, theta)  # Ok, now call myself to draw two branches!!
        # Whenever we get back here, we "pop" in order to restore the previous
        # matrix state
        popMatrix()
        branchNumber = (int)(1+random(2))
        # Repeat the same thing, only branch off to the "left" this time!
        for i in range (0,branchNumber):
            with pushMatrix():
                rotate(-theta * 0.6 - random(0.8))
                line(0, 0, 0, -h)
                translate(0, -h * 0.8 + random(0.4))
                branch(h, theta)