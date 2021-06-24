# level 2
Unfortuantely, didn't have the foresight to save the prompt, but essentially it was something like:
- You need to calibrate the lambchop doomsday device
- at the base of the lazer there are pegs that you can fix gears too
- You have gears of all sizes starting at diameter 1
- Given a list of integers representing the distance between each peg
- fix gears to the pegs so that each gear reachs and turns the peg next to it, and the last gear turns twice as fast as the first gear in the chain

The trick here was even though the distances were all integers, the gears didn't need to be, and for the final gear needs to move twice as fast as the first then it needs to have twice the radius. 

Consider the case of two pegs that are 1 unit apart, the only way for the gears to meet is at the half, or at 1/3 or 2/3 distance from the first peg. They'll never meet directly in the middle because that would force all the geers to be the same size.

So, in a loop, we start with a gear radius 1/3 and calculate the rest, then test the first and last, if the first isn't half the size of the last, reject, and step the radius up by 1/3 and calculate again. If they are, then return true.

This is a good example of a dynamic programming problem.