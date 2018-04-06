import os

def runforn(n):
	for i in range(n):
		os.system('python randomroutegenerator.py')
		os.system('python main2.py')
		os.system('python maininganother.py')
		#exec(open("./randomroutegenerator.py").read())
		#exec(open("./main2.py").read())	
		#exec(open("./maininganother.py").read())

if __name__ == "__main__":
	pass