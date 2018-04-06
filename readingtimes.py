def reading():
	outputlist= []
	count=0
	l=[]

	with open('timing1.txt','r') as f:
		for i in f:
			s1 = i.strip()
			s1 = float(s1)
			if count%2==0:
				l.append(s1)
				count+=1
			elif count%2==1:
				l.append(s1)
				count+=1
				outputlist.append(l)
				l = []
	sum1 = 0
	sum2 = 0
	for i in range(len(outputlist)):
		sum1 += outputlist[i][0]
		sum2 += outputlist[i][1]
	avgofgreenhori = sum1/len(outputlist)
	avgofredhori = sum2/len(outputlist)
	return (avgofredhori, avgofgreenhori)