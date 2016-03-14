import sys
import csv
import numpy as np
import random
from collections import defaultdict


def availble(l,bid):
	flag = True
	for elmt in l:
		if elmt < bid:
			flag = False
		else:
			flag = True
	return flag

def greedy(queries, kywds2advtser, bids, budgets):
	result = {}
	revenue = 0
	for query in queries:
		allbudgets = []
		allbids = []
		winner = None
		highest = 0
		#print kywds2advtser[query]
		for advertiser in kywds2advtser[query]:
			key = (advertiser,query)	
			allbudgets.append(budgets[advertiser])
			if  all(budget <=0 for budget in allbudgets):
				break	
			if bids[key] <= budgets[advertiser]:
				allbids.append(bids[key])
				if bids[key] > highest:
					highest = bids[key]
					winner = advertiser
		if winner != None:
			newbudget = budgets[winner] - bids[(winner,query)]
			del(budgets[winner])
			budgets[winner] = newbudget
		result[query]=winner
		revenue += highest
	return revenue

def main():
	matrix = np.loadtxt('bidder_dataset.csv', delimiter=",",skiprows=1,
	dtype= '|S15')
	#print matrix.shape
	budgets  = dict((int(i[0]),int(i[3])) for i in matrix if i[3]!='')
	bids  = dict(((int(i[0]),i[1]),float(i[2])) for i in matrix)
	#print bids

	#print queries
	templist  = list((i[1],int(i[0])) for i in matrix)
	kywds2advtser = defaultdict(list)
	for k,v in templist:
		kywds2advtser[k].append(v)
	#print kywds2advtser
	queries = np.loadtxt('queries.txt', delimiter="\n", dtype= '|S15')

	totalBudget = sum(budgets.values())
	method = sys.argv[1]
	if method.lower() == 'greedy':
		revenues = []
		for i in range(0,100):
			random.shuffle(queries)
			temp = greedy(queries, kywds2advtser, bids, budgets)
			budgets  = dict((int(i[0]),int(i[3])) for i in matrix if i[3]!='')
			#print temp
			revenues.append(temp)
		result = sum(revenues)/100
		competRate = result/totalBudget
		print result
		print competRate

if __name__ == "__main__":
    main()
	


