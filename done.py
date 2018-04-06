class redlight:

	def __init__(self):
		#light config
		self.n='r'
		self.e='r'
		self.s='r'
		self.w='r'
		self.turn=-1
		#cars passing
		self.cpn=0
		self.cpe=0
		self.cps=0
		self.cpw=0
		#misc data elements
		self.edelta=0
		self.yellowtime=5
		self.defaulttime={'ns':90,'ew':90}
		self.record=[[],[],[],[]]
		self.count=0
		self.prev=[]

	#-------functions for light light configuration-------------------------------------------------------
	def setlight(self,turn,yel=False):

		self.n='r'
		self.e='r'
		self.s='r'
		self.w='r'
		if not yel:
			if turn=='n' or turn=='s':
				self.n='G'
				self.s='G'
			elif turn=='e' or turn=='w':
				self.e='G'
				self.w='G'
			else:
				return -10

		elif yel:  
			if turn=='n' or turn=='s':
				self.n='y'
				self.s='y'
			elif turn=='e' or turn=='w':
				self.e='y'
				self.w='y' 
			else :
				return -1
		self.turn=turn
	#to return the final config of lights-------------------------------------------------------------------

	def getlight(self):

		return str(self.n+self.e+self.s+self.w)

	#to set the values of car passed--------------------------------------------------------------------------
	def setcp(self):
		value=sum(self.record[0])
		self.cpn=value
		value=sum(self.record[1])
		self.cpe=value
		value=sum(self.record[2])
		self.cps=value
		value=sum(self.record[3])
		self.cpw=value

	#getter--------------------------------------------------------------------------------------------------

	def talk(self,rec):
		if self.count<(self.defaulttime['ns']+self.defaulttime['ew']):
			if self.count<(self.defaulttime['ns']-self.edelta):
				self.setlight('n')
			else:
				self.setlight('e')
			self.record[0].append(rec[0])
			self.record[1].append(rec[1])
			self.record[2].append(rec[2])
			self.record[3].append(rec[3])
			self.count+=1

		else:

			self.setcp()
			self.calcdelta()
			#------------------reset everything--------------------------------------------------------------
			self.record=[[],[],[],[]]
			self.count=0
			self.setlight('n')




	#calculate the delta-------------------------------------------------------------------------------------

	def calcdelta(self):
		score1=(self.cpn+self.cps)
		score2=(self.cpe+self.cpw)
		self.delta=score1-score2
		self.delta=self.delta*1.25
		if score1==0:
			self.delta=70
		elif score2==0:
			self.delta=-70
		print(score1,score2)
		print(self.delta,'the delta')
		self.calc_edelta()


	#calculate the edelta------------------------------------------------------------------------------------

	def calc_edelta(self):
		sum1=0
		count = 0
		self.prev.append(self.delta)
		#print(len(self.prev))
		if len(self.prev)<5:
			if len(self.prev)<3:
				e=0
			elif len(self.prev)==3:
				e=((25*self.prev[0])+(25*self.prev[1])+(50*self.prev[2]))
			elif len(self.prev)==4:
				e=(5*self.prev[0]+25*self.prev[1]+25*self.prev[2]+45*self.prev[3])//100
		else:
			#self.cong()
			w=[5,5,25,25,40]
			self.prev.pop(0)
			for x in self.prev: 
				sum1=sum1+x*w[count]
				count+=1
			e=sum1//100
		if e>self.defaulttime['ns']//2:
			e=self.defaulttime['ns']//2
		elif e<-self.defaulttime['ns']//2:
			e=self.defaulttime['ns']//2

		self.edelta=e

		#print(e,'edelta')