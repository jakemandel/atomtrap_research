import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor

# Mouse click function to store coordinates
def storeclick(event):
    global ix, iy
    ix, iy = event.xdata, event.ydata

    print('x = %.5f, y = %.5f'%(ix, iy))

    global coords
    coords.append((ix, iy))

    # 6 clicks
    if len(coords) == 6:
        fig.canvas.mpl_disconnect(cid)
        plt.close()
    return

x = np.arange(0,4*np.pi,.1)
y = np.sin(x)

fig = plt.figure()
ax = fig.add_subplot()
ax.plot(x,y)

coords = []

# Call click function
cid = fig.canvas.mpl_connect('button_press_event', storeclick)
cursor = Cursor(ax, useblit=True, color='r', linewidth=1.7, linestyle='--')

plt.show()

# Fabry Perot:
# Difference = 
# 300/Difference = conv     # 300MHz FSR
# q = (Difference/300)*10   # 10MHz conversion for trap transition

conv = 326.086 # Conversion from Fabry Perot (MHZ/V)

# x-axis difference before conversion
c0 = coords[0][0] - coords[0][0]
c1 = coords[1][0] - coords[0][0]
c2 = coords[2][0] - coords[0][0]
c3 = coords[3][0] - coords[0][0]
c4 = coords[4][0] - coords[0][0]
c5 = coords[5][0] - coords[0][0]
n = 0
c = [] # Initialize list to contain x-axis difference before conversion
for i in coords:
    j = i[0] - coords[0][0]
    c.append(j)
print(c)

# Difference after conversion (MHz/V)
d0 = c0*conv
d1 = c1*conv
d2 = c2*conv
d3 = c3*conv
d4 = c4*conv
d5 = c5*conv

# Accepted Values

# Rubidium 87 Trap Transition
Rb87t_0 = 0
Rb87t_1 = 133.5
Rb87t_2 = 212
Rb87t_3 = 267
Rb87t_4 = 345.5
Rb87t_5 = 424
#Rb87t = [0 133.5 212 267 345.5 424]

# Rubidium 87 Pump
Rb87p_0 = 0
Rb87p_1 = 78.5
Rb87p_2 = 114.5
Rb87p_3 = 157
Rb87p_4 = 193
Rb87p_5 = 229
#Rb87p = [0 78.5 114.5 157 193 229]

# Rubidium 85 (2)
Rb85t_0 = 0
Rb85t_1 = 60.5
Rb85t_2 = 92
Rb85t_3 = 121
Rb85t_4 = 152.5
Rb85t_5 = 184
#Rb85t = [0 60.5 92 121 152.5 184]

# Rubidium 85 (4)
Rb85_0 = 0
Rb85_1 = 31.5
Rb85_2 = 46
Rb85_3 = 63
Rb85_4 = 77.5
Rb85_5 = 92
#Rb85 = [0 31.5 46 63 77.5 92]

# % Difference from transition - Rb 87 Trap
Rb87t_0p = (d0-Rb87t_0)*100
Rb87t_1p = (d1-Rb87t_1)*100
Rb87t_2p = (d2-Rb87t_2)*100
Rb87t_3p = (d3-Rb87t_3)*100
Rb87t_4p = (d4-Rb87t_4)*100
Rb87t_5p = (d5-Rb87t_5)*100

# % Difference from transition - Rb87 pump
Rb87t_0p = (d0-Rb87t_0)*100
Rb87t_1p = (d1-Rb87t_1)*100
Rb87t_2p = (d2-Rb87t_2)*100
Rb87t_3p = (d3-Rb87t_3)*100
Rb87t_4p = (d4-Rb87t_4)*100
Rb87t_5p = (d5-Rb87t_5)*100

# % Difference from transition - Rb85 (2)
Rb87t_0p = (d0-Rb87t_0)*100
Rb87t_1p = (d1-Rb87t_1)*100
Rb87t_2p = (d2-Rb87t_2)*100
Rb87t_3p = (d3-Rb87t_3)*100
Rb87t_4p = (d4-Rb87t_4)*100
Rb87t_5p = (d5-Rb87t_5)*100

# % Difference from transition - Rb85 (2)
Rb87t_0p = (d0-Rb87t_0)*100
Rb87t_1p = (d1-Rb87t_1)*100
Rb87t_2p = (d2-Rb87t_2)*100
Rb87t_3p = (d3-Rb87t_3)*100
Rb87t_4p = (d4-Rb87t_4)*100
Rb87t_5p = (d5-Rb87t_5)*100

# Intervals
interval1 = abs(c1-c0)
interval2 = abs(c2-c1)
interval3 = abs(c3-c2)
interval4 = abs(c4-c3)
interval5 = abs(c5-c4)








