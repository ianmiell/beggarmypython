#!/usr/bin/python
import beggarmypython
import random
import string

deck = 36*list('-') + 4*list('K') + 4*list('A') + 4*list('Q') + 4*list('J')

bestsofar = 0
bestdecksofar = deck
count = 0
results = {}
while True:
	count += 1
	random.shuffle(deck)
	res = beggarmypython.play((string.join(deck[:26],''),string.join(deck[26:],'')), verbose=False)
	if res > bestsofar:
		bestsofar = res
		bestdecksofar = deck
		print bestsofar
		print bestdecksofar
	else:
		try:
			results[res] += 1
		except:
			results[res] = 1
	if count % 1000000 == 1:
		print count
		print results
