import os
sum=0
for i in range(5):
	sum=sum+os.system('python main2.py')

print(sum/5)