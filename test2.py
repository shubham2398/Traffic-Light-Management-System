from __future__ import absolute_import
from __future__ import print_function
import time
import os
import sys

import optparse
import subprocess
import random


#!/usr/bin/env python
"""
@file    runner.py
@author  Lena Kalleske
@author  Daniel Krajzewicz
@author  Michael Behrisch
@author  Jakob Erdmann
@date    2009-03-26
@version $Id: runner.py 24864 2017-06-23 07:47:53Z behrisch $

Tutorial for traffic light control via the TraCI interface.

SUMO, Simulation of Urban MObility; see http://sumo.dlr.de/
Copyright (C) 2009-2017 DLR/TS, Germany

This file is part of SUMO.
SUMO is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.
"""

# we need to import python modules from the $SUMO_HOME/tools directory

def generate_routefile():
    N = 50  # number of time steps
    # demand per second from different directions
    pWE = 1. / 10
    pEW = 1. / 10
    pNS = 1. / 10
    pSN = 1. / 10
    with open("intersection1/intersection1.rou.xml", "w") as routes:
        print("""<routes>
        <vType id="genericvehicle" accel="0.8" decel="4.5" sigma="0.5" length="5" minGap="2.5" maxSpeed="16.67" guiShape="passenger"/>        

        <route id="right" edges="edge1to0 edge0to3" />
		<route id="left" edges="edge3to0 edge0to1" />
		<route id="down" edges="edge2to0 edge0to4" />
		<route id="up" edges="edge4to0 edge0to2" />""", file=routes)
        lastVeh = 0
        vehNr = 0
        for i in range(N):
            if random.uniform(0, 1) < pWE:
                print('    <vehicle id="right_%i" type="genericvehicle" route="right" depart="%i" />' % (
                    vehNr, i), file=routes)
                vehNr += 1
                lastVeh = i
            if random.uniform(0, 1) < pEW:
                print('    <vehicle id="left_%i" type="genericvehicle" route="left" depart="%i" />' % (
                    vehNr, i), file=routes)
                vehNr += 1
                lastVeh = i
            if random.uniform(0, 1) < pNS:
                print('    <vehicle id="down_%i" type="genericvehicle" route="down" depart="%i" color="1,0,0"/>' % (
                    vehNr, i), file=routes)
                vehNr += 1
                lastVeh = i

            if random.uniform(0, 1) < pSN:
                print('    <vehicle id="up_%i" type="genericvehicle" route="up" depart="%i" color="1,0,0"/>' % (
                    vehNr, i), file=routes)
                vehNr += 1
                lastVeh = i
        print("</routes>", file=routes)

# The program looks like this
#    <tlLogic id="0" type="static" programID="0" offset="0">
# the locations of the tls are      NESW
#        <phase duration="31" state="GrGr"/>
#        <phase duration="6"  state="yryr"/>
#        <phase duration="31" state="rGrG"/>
#        <phase duration="6"  state="ryry"/>
#    </tlLogic>







# this is the main entry point of this scri
  # first, generate the route file for this simulation
generate_routefile()

    # this is the normal way of using traci. sumo is started as a
    # subprocess and then the python script connects and runs
    


try:
    tools=os.path.join(os.environ['SUMO_HOME'],'tools')
    sys.path.append(tools)
except ImportError:
    sys.exit("please declare environment variable 'SUMO_HOME' as the root directory of your sumo installation (it should contain folders 'bin', 'tools' and 'docs')")

sumoBinary = "C:\\Program Files (x86)\\DLR\\Sumo\\bin\\sumo-gui"
sumoCmd = [sumoBinary, "-c", "C:\\Users\\nived\\Desktop\\sumo_experimentation\\FTM\\intersection1\\intersection1.sumocfg"]

import traci

traci.start(sumoCmd) 

def totaltime():
	return traci.simulation.getCurrentTime()

def randcall():
	step = 0
	listOftrafficlights=traci.trafficlights.getIDList()
	visited=[]
	while traci.simulation.getMinExpectedNumber() > 0:
		#x=input("Enter seq:")
		#traci.trafficlights.setRedYellowGreenState("0",x)
		traci.simulationStep()
		#stat=[]
		upthrough = 0
		downthrough = 0
		leftthrough = 0
		rightthrough = 0
		lis = traci.vehicle.getIDList()
		temp = []
		traffic = [100,100]
		for i in lis:
			temp.append(traci.vehicle.getPosition(i))
		#print(lis)
		for i in range(len(temp)):
			if 'up' in lis[i] and lis[i] not in visited:
				if temp[i][1] > traffic[1]:
					visited.append(lis[i])
					#stat.append(True)
					upthrough += 1
				else:
					pass
					#stat.append(False)
			if 'down' in lis[i] and lis[i] not in visited:
				if temp[i][1] < traffic[1]:
					visited.append(lis[i])
					#stat.append(True)
					downthrough += 1
				else:
					pass
					#stat.append(False)
			if 'right' in lis[i] and lis[i] not in visited:
				if temp[i][0] > traffic[0]:
					visited.append(lis[i])
					#stat.append(True)
					rightthrough += 1
				else:
					pass
					#stat.append(False)
			if 'left' in lis[i] and lis[i] not in visited:
				if temp[i][0] < traffic[0]:
					visited.append(lis[i])
					#stat.append(True)
					leftthrough += 1
				else:
					pass
					#stat.append(False)
		#print("temp",temp)
		#print("left: ",leftthrough,"\nright: ", rightthrough,"\nup",upthrough,"\ndown: ",downthrough)
		#time.sleep(0.4)
		step += 1
		if traci.simulation.getMinExpectedNumber() == 0:
			return(totaltime())

print(randcall())

traci.close(False)