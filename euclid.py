import networkx as nx
import operator
def main():
	eucl={}
	sim={}   
	with open('words.txt', 'r') as f:
    		for l in f:
       			d = l.split("\t")
       			d[1]=d[1].strip()
       			w=d[1].split()
       			eucl.setdefault(d[0], [])
       			for word in w:
       				if(word not in eucl[d[0]]):
       					eucl.setdefault(d[0], []).append(word)
	print "Dict done"
	target=open('Euclidean.txt','w')	
	for key in eucl:
		count1=0
		print key
		for key2 in eucl:
			count2=0
			if(key2==key):
				continue
			list1=eucl[key]
			list2=eucl[key2]
			for num in list1:
				if (num not in list2):
					count2+=1
			for num in list2:
				if(num not in list1):
					count2+=1
			count1=count1+float(count2)/(len(eucl[key])+len(eucl[key2]))
		sim.setdefault(key,[]).append(count1/59)
		print >> target,key,
		print >> target,format((count1/59),'0.6f')
	print sim
	target.close()
main()
