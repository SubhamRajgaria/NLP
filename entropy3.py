import math
import operator
fdata=open("Full_DT_adj_list",'r')   #
def entropy(line):
    fdata.seek(0)
    node=line.strip().split("\t")[0]
    list=line.strip().split("\t")[1]
    words= (list.split(' '))#list of neighbouring nodes
    deg={}
    wd_idx=0
    for i in range(0,len(words)):
        words[i]=int(words[i])
        deg.setdefault(words[i],[])        
        #traversing adj list
      #  print "\n",words[wd_idx],"--->",
    #print len(words)
    for l in fdata:
        node_2=l.strip().split("\t")[0]
        node_2=int(node_2)
        if (node_2 in words):#required for searching
            com=0              #no. of common neighbours this node has with ini. node
            list_2=l.strip().split("\t")[1]
            list_2=list_2.split(' ')
            for term in list_2:
                term=int(term)
                if term in words:#common found
                    #print term,
                    com+=1
            deg.setdefault(node_2,[]).append(com+1)
    #print len(deg)
    #print deg[deg.keys()[len(deg)-1]][0]
    max_deg=max(deg.iteritems(), key=operator.itemgetter(1))[1]

    ans=0
    for num in range(0,max_deg[0]+1):
        count=0
        for num_2 in range(0,len(deg)):
            if((deg[deg.keys()[num_2]])):
                if((deg[deg.keys()[num_2]][0])>num):
                    count+=1
        ans=ans+(float(count)/((len(deg)+1)*len(deg)))
    for num in range(max_deg[0],len(deg)):
        ans=ans+(float(1)/((len(deg)+1)*len(deg)))
    return format(ans,'0.6f')
    

def main():
    
    with open ('words.txt','r')as ip:
        for line in ip:
            node=line.strip().split("\t")[0]
            ans=entropy(line)
            print node,ans
            """
    ans=entropy("6	1 2 3 4 5")
    print ans
            """
        
main()
