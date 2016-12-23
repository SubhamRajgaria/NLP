import networkx as nx
import operator
def check(w,G):
	for i in range(0,len(w)):
		w[i]=int(w[i])
	fdata=open("Full_DT_adj_list",'r')
	fdata.seek(0)
	for l in fdata:
		node_2=l.strip().split("\t")[0]
		node_2=int(node_2)
        if (node_2 in w):#required for searching
            com=0              #no. of common neighbours this node has with ini. node
            list_2=l.strip().split("\t")[1]
            list_2=list_2.split(' ')
            for term in list_2:
                term=int(term)
                if term in words:#common found
                   G.add_edge(node_2,term)
def main():
	G=nx.Graph()
	with open('words.txt', 'r') as f:
		for l in f:
			d = l.split("\t")
			d[1]=d[1].strip()
			w=d[1].split()
			#G.add_node(d[0])
			check(w,G)
			print "Hi"
			for word in w:
				word=int(word)
				G.add_edge(d[0],word)
	print G.number_of_nodes()
	#degree(G,G_noun,G_adj,G_verb)
	#cluster(G,G_noun,G_adj,G_verb)

#def degree(G,G_noun,G_adj,G_verb):

#def cluster(G,G_noun,G_adj,G_verb):
#def centrality(G,G_noun,G_adj,G_verb):
	betweenness_centrality=nx.betweenness_centrality(G,k=600,normalized=True,weight=None,endpoints=False, seed=None)
	print "Betweenness Done"

	target=open('bet_2.txt','w')
	with open('words.txt','r') as f:
		for l in f:
			d=l.split("\t")
			word=d[0]
			print >> target, word,
			print >> target,format(betweenness_centrality[word],'0.6f')
main()

