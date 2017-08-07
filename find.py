#!/usr/bin/python
import beggarmypython
import random
import string
import matplotlib.pyplot as plt
import numpy as np

deck = 36*list('-') + 4*list('K') + 4*list('A') + 4*list('Q') + 4*list('J')

bestsofar = 0
bestdecksofar = deck
count = 0
results = {}
results_list = []
while True:
	count += 1
	random.shuffle(deck)
	res = beggarmypython.play((string.join(deck[:26],''),string.join(deck[26:],'')), verbose=False)
	results_list = results_list + [res]
	if res > bestsofar:
		bestsofar = res
		bestdecksofar = deck
		print bestsofar
		print bestdecksofar
	try:
		results[res] += 1
	except:
		results[res] = 1
	if count % 1000 == 1:
		print count
		print results
		print bestsofar
		print bestdecksofar
		a = np.hstack((results_list))
		plt.hist(a,bins='auto')
#>>> plt.title("Histogram with 'auto' bins")
		plt.show()
