import runmultsim
import readingtimes2
import readingtimes

runmultsim.runforn(2)
avggreenforhori, avgredforhori = readingtimes.reading()
avggreenforhori2, avgredforhori2 = readingtimes2.reading()
print("Benchmarks for algo\'s run (the learned approach): ")
print("-------------------------------------------------------------------------")
print("Average duration for green light in the horizontal road: ",avggreenforhori)
print("Average duration for red light on the horizontal road: ", avgredforhori)
print()
print("Benchmarks for naive run (the random approach): ")
print("-------------------------------------------------------------------------")
print("Average duration for green light in the horizontal road: ",avggreenforhori2)
print("Average duration for red light on the horizontal road: ", avgredforhori2)