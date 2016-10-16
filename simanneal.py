import random
import math
"""
Runs a rudimentary simulated annealing algorithm on a fixed first point traveling salesman problem, where the salesman returns to the original point
Original point always the OG NYC bois

"""

def distance(citya, cityb):
	R = 3963  # radius of Earth (miles)
	lat1, lon1 = math.radians(citya[0]), math.radians(citya[1])
	lat2, lon2 = math.radians(cityb[0]), math.radians(cityb[1])
	return math.acos(math.sin(lat1) * math.sin(lat2) + 
		math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2)) * R	

def acceptance_probability(currentEnergy, newEnergy, temp):
		if newEnergy < currentEnergy:
			return 1
		return math.exp((currentEnergy - newEnergy) / temperature)

class TSPTour:
	def __init__(self, tour):
		self.tour = tour
		
	def randomize(self):
		self.tour = list(cities.keys())
		random.shuffle(self.tour)
		for i in range(len(self.tour)):
			if(self.tour[i] == 'New York City'):
				self.tour[0], self.tour[i] = self.tour[i], self.tour[0]

	def total_energy(self):
		total = 0

		for i in range(len(self.tour)):
			if(i == len(self.tour) - 1):
				total += distance(cities[self.tour[i]], cities[self.tour[0]])
				return total
			total += distance(cities[self.tour[i]], cities[self.tour[i+1]])
	def get_tour(self):
		tours = self.tour
		return tours

	def retmove(self):
		newTour = []
		for i in self.tour:
			newTour.append(i)
		a = random.randint(1, len(newTour) - 1)
		b = random.randint(1, len(newTour) - 1)
		newTour[a], newTour[b] = newTour[b], newTour[a]
		return newTour

cities = {
        'New York City': (40.72, 74.00),
        'Los Angeles': (34.05, 118.25),
        'Chicago': (41.88, 87.63),
        'Houston': (29.77, 95.38),
        'Phoenix': (33.45, 112.07),
        'Philadelphia': (39.95, 75.17),
        'San Antonio': (29.53, 98.47),
        'Dallas': (32.78, 96.80),
        'San Diego': (32.78, 117.15),
        'San Jose': (37.30, 121.87),
        'Detroit': (42.33, 83.05),
        'San Francisco': (37.78, 122.42),
        'Jacksonville': (30.32, 81.70),
        'Indianapolis': (39.78, 86.15),
        'Austin': (30.27, 97.77),
        'Columbus': (39.98, 82.98),
        'Fort Worth': (32.75, 97.33),
        'Charlotte': (35.23, 80.85),
        'Memphis': (35.12, 89.97),
        'Baltimore': (39.28, 76.62)
    }
 
global current
current = TSPTour([])
current.randomize()
global best
best = TSPTour(current.get_tour())
print "Initial Energy (Random) : " + str(current.total_energy())
#Temperature basically tells us how readily we should accept solutions and how much time we have left
temperature = 1000
cooling_rate = .003
run = 1 #Tracking variable
#main annealing loop
while temperature > 1:
	#generate new tour by randomly swapping two cities in the old tour
	
	newSol = TSPTour(current.retmove())
	#Find energies of current and new tours
	current_eneg = current.total_energy()
	new_eneg = newSol.total_energy()
	#Determines whether to accept new solution or not based on acceptance probability and randomnity
	if acceptance_probability(current_eneg, new_eneg, temperature) > random.random():
		current = TSPTour(newSol.get_tour())
	#Determine if current solution is best solution so far
	if current.total_energy() < best.total_energy():
		print("OVERRIDING, New Best: " + str(current.total_energy()) + " Old Best: " + str(best.total_energy()))
		best = TSPTour(current.get_tour())
	#Temperature lowers
	temperature *= 1 - cooling_rate

	run+=1 

print "Final: "+str(best.total_energy())
print "Tour: "+str(best.get_tour())

"""

print current.tour
print current.total_energy()
stuff = current.retmove()
print stuff
print(TSPTour(stuff).total_energy())

"""


