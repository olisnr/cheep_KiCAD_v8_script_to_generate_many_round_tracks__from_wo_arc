# use exec(open("/ALL/WiNDOWs/520/520-nofuture_2024/python/pcb_multi_arcs.py").read())

import math
from pcbnew import *

points_per_circle =     180
radius_start =          99.3
radius_delta =          -.6
arcs =                  52

pcb = GetBoard()

for arc in range(arcs):
    for track in range(int(points_per_circle / 2)):
        a = 2 * math.pi / points_per_circle * track
        b = 2 * math.pi / points_per_circle * (track + 1)

        t = PCB_TRACK(pcb)
        t.SetStart(VECTOR2I_MM(math.sin(a) * (radius_start + radius_delta * arc), math.cos(a) * (radius_start + radius_delta * arc)))
        t.SetEnd(  VECTOR2I_MM(math.sin(b) * (radius_start + radius_delta * arc), math.cos(b) * (radius_start + radius_delta * arc)))
        pcb.Add(t)

Refresh()
