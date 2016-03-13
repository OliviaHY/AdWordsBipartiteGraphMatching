import csv
import numpy as np
from collections import defaultdict

#ifile  = open('bidder_dataset.csv', "rb")

#matrix = np.genfromtxt('bidder_dataset.csv', delimiter=",",skiprows=0,dtype= None,
						#names = ('Advertiser','Keyword','Bid Value','Budget'))

#matrix = np.loadtxt('bidder_dataset.csv', delimiter=",",skiprows=1,
	#dtype= {'names': ('Advertiser','Keyword','Bid Value'),
	#'formats':(np.int, '|S15', np.float)},usecols=[0,1,2])
matrix = np.loadtxt('bidder_dataset.csv', delimiter=",",skiprows=1,
	dtype= '|S15')
print matrix
budgets  = dict((int(i[0]),int(i[3])) for i in matrix if i[3]!='')
#budgets = budgets.astype(np.int)
#print budgets
budgets  = dict((int(i[0]),int(i[3])) for i in matrix if i[3]!='')
queries = np.loadtxt('queries.txt', delimiter="\n", dtype= '|S15')
bids  = dict(((int(i[0]),i[1]),float(i[2])) for i in matrix)
print bids

#print queries
templist  = list((i[1],int(i[0])) for i in matrix)
tempdict = defaultdict(list)
for k,v in templist:
	tempdict[k].append(v)
#print tempdict
queries = np.loadtxt('queries.txt', delimiter="\n", dtype= '|S15')

# for query in queries:
# 	i = 0
# 	for advertiser in matrix[:,0]:
# 		if query == matrix[i,1]:
# 			print matrix[i,:]
# 		i+=1

