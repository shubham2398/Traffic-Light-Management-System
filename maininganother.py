import pickle
import time
import os
import sys
import traci
from done2 import *

obj=redlight()

trafficlights = []
current_states = []

try:
    tools=os.path.join(os.environ['SUMO_HOME'],'tools')
    sys.path.append(tools)
except ImportError:
    sys.exit("please declare environment variable 'SUMO_HOME' as the root directory of your sumo installation (it should contain folders 'bin', 'tools' and 'docs')")

sumoBinary = "C:\\Program Files (x86)\\DLR\\Sumo\\bin\\sumo-gui"
sumoCmd = [sumoBinary, "-c", "C:\\Users\\anike\\Desktop\\SMARTathon\\intersection1\\intersection1\\intersection1.sumocfg"]

traci.start(sumoCmd) 

def throughput():	
	
	traffic_lights = traci.trafficlights.getIDList()
	

	for i in trafficlights:
		current_states.append(traci.trafficlights.getRedYellowGreenState(i))

	throughput = []

	l = []
	l.append(traci.inductionloop.getLastStepVehicleNumber("0"))
	l.append(traci.inductionloop.getLastStepVehicleNumber("1"))
	l.append(traci.inductionloop.getLastStepVehicleNumber("2"))
	l.append(traci.inductionloop.getLastStepVehicleNumber("3"))

	throughput.extend(l)
	return(throughput)
	

step = 0
listOftrafficlights=traci.trafficlights.getIDList()
visited=[]
red = 0
green = 0
countofsteps = 0
#next = 'GrGr'
while traci.simulation.getMinExpectedNumber()>0:
	current=traci.trafficlights.getRedYellowGreenState('0')
	traci.simulationStep()
	val_list=throughput()
	print(val_list)
	obj.talk(val_list)
	tempy = current
	next=obj.getlight()
	if tempy != next:
		countofsteps += 1
	#print(next)
	if next == 'GrGr':
		green += 1
	elif next == 'rGrG':
		red += 1
	traci.trafficlights.setRedYellowGreenState('0',next)
	#time.sleep(0.2)
	step += 1

if traci.simulation.getMinExpectedNumber() == 0:
	print(traci.simulation.getCurrentTime())

traci.close(False)

timeavg = [float(red)/float(countofsteps), float(green)/float(countofsteps)]
with open("timing2.txt" ,'a') as filey:
    for item in timeavg:
        filey.write("{}\n".format(item))