import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('algeriaPopulation.csv')

#Sort data by a special value
#sort_data = data.sort_values(by=['growth'], ascending=False)
myList = []
for n in data.population:
	myList.append(n)

def calcPopulation(lst,mydata):
	
	perList = []
	# p = myfile.population[1]-myfile.population[0]
	# s = (p/myfile.population[0])*100
	for i in range(1,len(mydata.population)):
		diff = mydata.population[i]-mydata.population[i-1]
		perc = (diff / mydata.population[i]) * 100
		perList.append(perc)
	
	x = 1
	while x < len(mydata.year):
		_growthRate = "Population growth rate for year:"
		sep = ">>>>>> "
		print(f"{_growthRate} {mydata.year[x]} {sep} {perList[x-1]}")
		x += 1

	plt.plot(mydata.year[1:],perList)
	plt.title("Algeria Population growth rate")
	plt.legend(["Population growth rate"])
	plt.xlabel('year')
	plt.ylabel('population growth rate')
	plt.show()

calcPopulation(myList,data)