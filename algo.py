from __future__ import absolute_import
from __future__ import print_function
import time
import os
import sys

import optparse
import subprocess
import random
import traci

try:
    tools=os.path.join(os.environ['SUMO_HOME'],'tools')
    sys.path.append(tools)
except ImportError:
    sys.exit("please declare environment variable 'SUMO_HOME' as the root directory of your sumo installation (it should contain folders 'bin', 'tools' and 'docs')")

sumoBinary = "C:\\Program Files (x86)\\DLR\\Sumo\\bin\\sumo-gui"
sumoCmd = [sumoBinary, "-c", "C:\\Users\\nived\\Desktop\\sumo_experimentation\\FTM_remastered\\intersection3\\intersection3.sumocfg"]


traffic_lights = []
current_states = []
traci.start(sumoCmd) 


while traci.simulation.getMinExpectedNumber() > 0:
	traci.simulationStep()

	
	
	traffic_lights = traci.trafficlights.getIDList()
		

	for i in traffic_lights:
		current_states.append(traci.trafficlights.getRedYellowGreenState(i))

	throughput1 = []
	throughput2 = []

	l1 = []
	l1.append(traci.inductionloop.getLastStepVehicleNumber("0"))
	l1.append(traci.inductionloop.getLastStepVehicleNumber("1"))
	l1.append(traci.inductionloop.getLastStepVehicleNumber("2"))
	l1.append(traci.inductionloop.getLastStepVehicleNumber("3"))

	throughput1.extend(l1)

	l2 = []
	l2.append(traci.inductionloop.getLastStepVehicleNumber("4"))
	l2.append(traci.inductionloop.getLastStepVehicleNumber("5"))
	l2.append(traci.inductionloop.getLastStepVehicleNumber("6"))
	l2.append(traci.inductionloop.getLastStepVehicleNumber("7"))

	throughput2.extend(l2)

	print(throughput1,throughput2)

traci.close()







	



