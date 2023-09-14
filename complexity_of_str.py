from faker import Faker
import time
import matplotlib.pyplot as plt
def test():
	strings = []
	faker = Faker()
	for i in range(1000):
		strings.append([faker.user_name()*i,faker.user_name()*(i+10)]) 
	return strings

def case():
	strs = test()
	result = []
	x = []
	for st in strs:
		start = time.time()
		if st[0] < st[1]:
			pass
		end = time.time()
		result.append(end-start)
		x.append(len(st[1]))
	plt.plot(x,result)
	plt.show()

if __name__=="__main__":
	case()
