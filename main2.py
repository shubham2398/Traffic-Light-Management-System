import pickle
import time
import os
import sys
import traci
from done import *

obj2=redlight()

trafficlights = []
current_states = []

obj1=redlight()

try:
    tools=os.path.join(os.environ['SUMO_HOME'],'tools')
    sys.path.append(tools)
except ImportError:
    sys.exit("please declare environment variable 'SUMO_HOME' as the root directory of your sumo installation (it should contain folders 'bin', 'tools' and 'docs')")

sumoBinary = "C:\\Program Files (x86)\\DLR\\Sumo\\bin\\sumo-gui"
sumoCmd = [sumoBinary, "-c", "C:\\Users\\SHUBHAM  THAKRAL\\Desktop\\samsung hackathon\\newwwww\\intersection3.sumocfg"]

traci.start(sumoCmd) 
	

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



	#print(val_list)
	obj1.talk(throughput1)
	tempy = current
	next=obj1.getlight()
	if tempy != next:
		countofsteps += 1
	#print(next)
	if next == 'GrGr':
		green += 1
	elif next == 'rGrG':
		red += 1
	traci.trafficlights.setRedYellowGreenState('0',next)
	obj2.talk(throughput2)
	tempy = current
	next=obj2.getlight()
	if tempy != next:
		countofsteps += 1
	#print(next)
	if next == 'GrGr':
		green += 1
	elif next == 'rGrG':
		red += 1
	traci.trafficlights.setRedYellowGreenState('3',next)


	#time.sleep(0.2)
	step += 1

if traci.simulation.getMinExpectedNumber() == 0:
	print(traci.simulation.getCurrentTime())

traci.close(False)

timeavg = [float(red)/float(countofsteps), float(green)/float(countofsteps)]
with open("timing1.txt" ,'a') as filey:
    for item in timeavg:
        filey.write("{}\n".format(item))