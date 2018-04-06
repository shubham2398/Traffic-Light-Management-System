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
from __future__ import absolute_import
from __future__ import print_function

import os
import sys
import optparse
import subprocess
import random

# we need to import python modules from the $SUMO_HOME/tools directory

def generate_routefile():    
	N = 1000  # number of time steps
	# demand per second from different directions
	
	with open("intersection3.rou.xml", "w") as routes:
		print("""<routes>
		<vType id="genericvehicle" accel="0.8" decel="4.5" sigma="0.5" length="5" minGap="2.5" maxSpeed="30.67" guiShape="passenger"/>
		<vType id="slowvehicle" accel="0.5" decel="4.5" sigma="0.5" length="5" minGap="2.5" maxSpeed="1.00" guiShape="passenger"/>        

		<route id="right" edges="edge1to0 edge0to3 edge3to7" />
		<route id="left" edges="edge7to3 edge3to0 edge0to1" />
		<route id="down1" edges="edge2to0 edge0to4" />	
		<route id="down2" edges="edge5to3 edge3to6" />
		<route id="up1" edges="edge4to0 edge0to2" />
		<route id="up2" edges="edge6to3 edge3to5" /> """, file=routes)
		lastVeh = 0
		vehNr = 0
		for i in range(N):		
				if i%8==0:		
					print('    <vehicle id="down1_%i" type="genericvehicle" route="down1" depart="%i" color="1,0,0"/>' % (vehNr, i), file=routes)
					vehNr += 1	
				if i%8==1:									
					print('    <vehicle id="up1_%i" type="genericvehicle" route="up1" depart="%i" color="1,0,0"/>' % (vehNr, i), file=routes)
					vehNr += 1	
				if i%8==2:
					print('    <vehicle id="down2_%i" type="genericvehicle" route="down2" depart="%i" />' % (vehNr, i), file=routes)
					vehNr += 1	
				if i%8==3:		
					print('    <vehicle id="up2_%i" type="genericvehicle" route="up2" depart="%i" />' % (vehNr, i), file=routes)
					vehNr += 1
				if i%8==4:		
					print('    <vehicle id="right_%i" type="slowvehicle" route="right" depart="%i" />' % (vehNr, i), file=routes)
					vehNr += 1
				if i%8==5:		
					print('    <vehicle id="left_%i" type="slowvehicle" route="left" depart="%i" />' % (vehNr, i), file=routes)
					vehNr += 1
				if i%8==6:		
					print('    <vehicle id="left_%i" type="slowvehicle" route="left" depart="%i" />' % (vehNr, i), file=routes)
					vehNr += 1
				if i%8==7:		
					print('    <vehicle id="right_%i" type="slowvehicle" route="right" depart="%i" />' % (vehNr, i), file=routes)
					vehNr += 1			

		   
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
	
