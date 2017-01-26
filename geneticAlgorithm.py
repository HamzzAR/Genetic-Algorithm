import random
import string

def selection(pop,fitness):
	for passnum in range(len(pop)-1,0,-1):
		for i in range(passnum):
			if fitness[i]<fitness[i+1]:
				temp = fitness[i]
				temp2 = pop[i]
				fitness[i] = fitness[i+1]
				pop[i] = pop[i+1]
				fitness[i+1] = temp
				pop[i+1] = temp2
	return pop


def evaluateFitness(pop,go):
  population = []
  for x in range(len(pop)):
    fitness = calcFitness(pop[x],go)
    population.append(fitness)
  return population

def calcFitness(DNA,go):
  score = 0
  for genes in range(len(DNA)):
    if DNA[genes] == go[genes]:
      score+=1
  fitness = score/len(go)
  return fitness

def mutation(pop,go,alphabet,p):
	for DNA in range(len(pop)):
		n = random.uniform(0,1)
		if n < p:
			for x in range(len(go)):
				if pop[DNA][x] != go[x]:
					pop[DNA][x] = random.choice(alphabet)
	return pop


def crossover(pop,go,alphabet,p_c):
  individual = random.choice(pop)
  individual2 = random.choice(pop)
  r = random.uniform(0,1)
  if r < p_c:
	  child = individual[:int(len(go)/2)] + individual[int(len(go)/2):]
	  pop.append(child)
	  pop.remove(pop[-2])
  return pop


def evolve(population,go,alphabet,gen,p,p_c):
	for x in range(gen):
		fitness = evaluateFitness(population,go)
		population = selection(population,fitness)
		population = mutation(population,go,alphabet,p)
		population = crossover(population,go,alphabet,p_c)
    
		result = ''
		for genes in population[0]:
			result+=genes
	
		if result == go:
			print()
			return result
		print('Generation {0}: {1}'.format(x,result))


size = 100
generations = 10000
p_mutation = 0.1
p_crossover = 0.5
goal = 'Example String'
goalLength = len(goal)
alpha = string.printable
population = [random.sample(alpha,goalLength) for x in range(size)]

print('Fittest String:',evolve(population,goal,alpha,generations,p_mutation,p_crossover))
