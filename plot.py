import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
import pdb
import sys
import matplotlib.pyplot as plt

#In C, empirically dumped all wilds rooms' recall points, which also serves to verify that the recall_loc() code is correct. 
#Dumped the from->to locations, then parsed out all + sorted + uniqed all of the to locations: this is our set of recallable
#points, which will define our recall shadows.

#A list of all recallable areas.
points = [ [295, 1160], [312, 1177], [365, 1151], [435, 1226], [506, 1308], [553, 1360], [607,  437], [609, 1303], [654,  365], [671,  572], [700,  680], [705,  763], [705, 1403], [736,  391], [778,  651], [797,  445], [801,  545], [806, 1265], [813, 1202], [951,  356], [972,  699], [1007,  306], [1020, 1208], [1031,  316], [1119,  330], [1159,  421], [1191,  968], [1271,  211], [1304, 1092], [1554, 1234], [1582,  392], [1619,  540], [1629, 1223], [1651,  183], [1689,  389], [1692,  470], [1707,  438], [1724,  685], [1814,  255], [1833,  425], [1885,  459] ]

full_set = []
#map dims
x_range = 2300
y_range = 1500

#scipy's voronoi lib doesn't appear to support wrapping, and we're visualizing a torus which wraps
#so build a 3x3 grid of these points and we'll use the center one to fake it.
for p in points:
    for x in range(0, 3):
        for y in range(0, 3):
            new_x = p[0] + (x * x_range)
            new_y = p[1] + (y * y_range)

            full_set.append([new_x, new_y])

#import antigravity
vor = Voronoi(full_set)
fig = voronoi_plot_2d(vor, show_vertices=False, line_colors='green', line_width=.1, line_alpha=1, point_size=2, frameon=False)

#turn the axes off
for axes in fig.axes:
    #...all of them
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)

#only display the center points from within the 3x3 array of identical sets.
plt.xlim(2300, 4600)
plt.ylim(1500, 3000)
#this is redundant with the axes off
plt.gca().invert_yaxis()

#export it with high resolution
fig.savefig('img.png', format='png', dpi=1000)
