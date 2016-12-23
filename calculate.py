import networkx as nx
import operator
def main():
	G2={}   
	with open('Full_DT_nodes.txt', 'r') as f:
    		for l in f:
       			d = l.split("\t")
	 		d[2]=d[2].strip()
	 		d[0]=int(d[0])
	 		w=d[1].split("/")
	 		G2.setdefault(d[0], []).append(w)
	G=nx.Graph()
	G_noun=nx.Graph()
	G_adj=nx.Graph()
	G_verb=nx.Graph()
	with open('words.txt', 'r') as f:
		for l in f:
			d = l.split("\t")
			d[1]=d[1].strip()
			w=d[1].split()
			#G.add_node(d[0])
			for word in w:
				word=int(word)
				G.add_edge(d[0],word)
				if(G2[word][0][1]=='JJ' or G2[word][0][1]=='JJR' or G2[word][0][1]=='JJS'):
					G_adj.add_edge(d[0],word)
				if(G2[word][0][1]=='NN' or G2[word][0][1]=='NNS' or G2[word][0][1]=='NNPS' or G2[word][0][1]=='NNP'):
					G_noun.add_edge(d[0],word)
				if(G2[word][0][1]=='VB' or G2[word][0][1]=='VBD' or G2[word][0][1]=='VBG' or
				 G2[word][0][1]=='VBN' or G2[word][0][1]=='VBP' or G2[word][0][1]=='VBZ'):
					G_verb.add_edge(d[0],word)
	print G.number_of_nodes()
	#degree(G,G_noun,G_adj,G_verb)
	#cluster(G,G_noun,G_adj,G_verb)

#def degree(G,G_noun,G_adj,G_verb):
	deg_total=nx.degree(G)
	deg_noun=nx.degree(G_noun)
	deg_adj=nx.degree(G_adj)
	deg_verb=nx.degree(G_verb)
	max_tot=max(deg_total.iteritems(), key=operator.itemgetter(1))[0]
	max_noun= max(deg_noun.iteritems(), key=operator.itemgetter(1))[0]
	max_verb= max(deg_verb.iteritems(), key=operator.itemgetter(1))[0]
	max_adj= max(deg_adj.iteritems(), key=operator.itemgetter(1))[0]
	print deg_total['bicycle']

#def cluster(G,G_noun,G_adj,G_verb):
	clust_tot=nx.clustering(G, nodes=None, weight=None)
	clust_noun=nx.clustering(G_noun, nodes=None, weight=None)
	clust_adj=nx.clustering(G_adj, nodes=None, weight=None)
	clust_verb=nx.clustering(G_verb, nodes=None, weight=None)

#def centrality(G,G_noun,G_adj,G_verb):
	degree_centrality=nx.degree_centrality(G)
	print "Degree done"
	"""betweenness_centrality=nx.betweenness_centrality(G,k=60,normalized=True,weight=None,endpoints=False, seed=None)
	print "Betweenness Done"
	eigenvector_centrality=nx. eigenvector_centrality(G, max_iter=10000, tol=1e-06, nstart=None, weight='weight')
	print "Eigen done"
	katz_centrality=nx.katz_centrality(G, alpha=0.1, beta=1.0, max_iter=100000,tol=1e-06, nstart=None, normalized=True, weight='weight')"""
        #katz_centrality not converging
        print "Katz_done"
	#closeness_centrality=nx.closeness_centrality(G, u=None, distance=None, normalized=True)	
	print "Closeness done"

	target=open('Final_list.txt','w')
	with open('words.txt','r') as f:
		for l in f:
			d=l.split("\t")
			word=d[0]
			deg=float(deg_total[word])/deg_total[max_tot]
			deg_n=float(deg_noun[word])/deg_noun[max_noun]
			deg_a=float(deg_adj[word])/deg_adj[max_adj]
			deg_v=float(deg_verb[word])/deg_verb[max_verb]
			print >> target, word,
			print >> target,format(deg,'0.6f'),
			print >> target,format(deg_n,'0.6f'),
			print >> target,format(deg_a,'0.6f'),
			print >> target,format(deg_v,'0.6f'),
			print >> target,format(clust_tot[word],'0.6f'),
			print >> target,format(clust_noun[word],'0.6f'),
			print >> target,format(clust_adj[word],'0.6f'),
			print >> target,format(clust_verb[word],'0.6f'),
			print >> target,format(degree_centrality[word],'0.6f')
			#print >> target,format(betweenness_centrality[word],'0.6f'),
			#print >> target,format(eigenvector_centrality[word],'0.6f'),
			#print >> target,format(katz_centrality[word],'0.6f'),
			#print >> target,format(closeness_centrality[word],'0.6f')
main()

