#!/usr/bin/python3

import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig =plt.figure()
ax1 = fig.add_subplot(1,1,1)

def axisHandler(i):
    pullData = open("reading.txt","r").read()
    dataArray = pullData.split('\n')
    xar = []
    yar = []
    print("i   {}".format(i))
    for eachLine in dataArray:
        if len(eachLine)>1:
            index,_,Temp = eachLine.split(' ')
            xar.append(int(index))
            yar.append(float(Temp))
    ax1.clear()
    ax1.plot(xar,yar)
    ax1.set_xlabel("Time (s)")
    ax1.set_ylabel("Temperature (C)")

#    plotter()
def  defPlotter():
    ani = animation.FuncAnimation(fig, axisHandler, interval=10000)
    plt.show()

if __name__  == "__main__":
    defPlotter()

