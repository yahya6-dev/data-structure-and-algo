import random

def roll():
	r = random.randint(1,6)
	return r

def game():
	record = 0
	last   = roll()
	while True:
		current = roll()
		if last == 5 and current == 5:
			record  += 1
			break
		last =  current
		record += 1
	print("total is $%d"%record)
	return record

game() 
