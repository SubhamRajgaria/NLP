w, h = 5119, 60 
Matrix = [[0 for x in range(w)] for y in range(h)] 
count1=0  
with open('words.txt', 'r') as file:
    for line in file:
       	d = line.split("\t")
       	d[1]=d[1].strip()
       	w=d[1].split(" ")
	count2=0
	for word in w:
		word=int(word)  
		Matrix[count1][count2]=word    	
		count2+=1	
	count1+=1
#print Matrix
w, h = 60, 60 
Matrix2 = [[0 for x in range(w)] for y in range(h)] 
for i in range (0,59):
	for j in range (i+1,60):
		counter=0
		for x in range (0,5119):
			if (Matrix[i][x]==0):
				break
				for y in range (0,5119):
					if (Matrix[j][y]==0):
						break
 						if (Matrix[i][x]==Matrix[j][y]):
							print true
							counter+=1
		#print counter
		Matrix2[i][j]=counter
		Matrix2[j][i]=counter
#print Matrix2
