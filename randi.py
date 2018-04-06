#!/usr/bin/env python
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
	
	with open("intersection1.rou.xml", "w") as routes:
		print("""<routes>
		<vType id="genericvehicle" accel="0.8" decel="4.5" sigma="0.5" length="5" minGap="2.5" maxSpeed="30.67" guiShape="passenger"/>
		<vType id="slowvehicle" accel="0.5" decel="4.5" sigma="0.5" length="5" minGap="2.5" maxSpeed="10.00" guiShape="passenger"/>        

		<route id="right" edges="edge1to0 edge0to3" />
		<route id="left" edges="edge3to0 edge0to1" />
		<route id="down" edges="edge2to0 edge0to4" />		
		<route id="up" edges="edge4to0 edge0to2" /> """, file=routes)
		lastVeh = 0
		vehNr = 0
		for i in range(N):	
			x = random.randint(0,3)	
			if i%4==x:		
				print('    <vehicle id="down_%i" type="genericvehicle" route="down" depart="%i" color="1,0,0"/>' % (vehNr, i), file=routes)
				vehNr += 1	
			if i%4==x:									
				print('    <vehicle id="up_%i" type="genericvehicle" route="up" depart="%i" color="1,0,0"/>' % (vehNr, i), file=routes)
				vehNr += 1	
			if i%4==x:
				print('    <vehicle id="right_%i" type="slowvehicle" route="right" depart="%i" />' % (vehNr, i), file=routes)
				vehNr += 1	
			if i%4==x:		
				print('    <vehicle id="left_%i" type="slowvehicle" route="left" depart="%i" />' % (vehNr, i), file=routes)
				vehNr += 1
	
		print("</routes>", file=routes)
generate_routefile()