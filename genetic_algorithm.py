import ann_criterion
import numpy as np
import time
from random import random, randint, shuffle

population_size = 200
characteristics_num = 60
min_range = -3
max_range = 3
mutation_chance = 0.1
mutation_genes_num = 3
generation_max = 50


class Individual:
	"""
		Objekat ove klase nam predstavlja jednu jedinku u populaciji.
		Ona sadrži vektor svojih "gena" tj. karakteristika i vrednost svog fitness-a kada je ubačena u neuronsku mrežu
	"""

	def __init__(self):
		self.characteristics = []
		self.fitness = 0.0
		self.set_characteristics()

	def __lt__(self, other):
		return self.fitness < other.fitness

	def set_characteristics(self):
		self.characteristics = [round(elem, 3) for elem in
								list(np.random.uniform(min_range, max_range, characteristics_num))]

	def __str__(self):
		return str(self.fitness) + " " + str(self.characteristics)

	def calculate_fitness(self):
		self.fitness = ann_criterion.optimality_criterion(self.characteristics)

	def mutate(self):
		"""
		Radimo mutaciju nad jedinkom sa šansom od 0.1
		Pritom menjamo vrednost nad tri random odabrane karakteristike.
		Nova vrednost je takodje randm generisana.
		"""
		if np.random.uniform(0, 1) <= mutation_chance:
			for i in range(mutation_genes_num):
				pos_to_mutate = randint(0, characteristics_num - 1)
				self.characteristics[pos_to_mutate] = np.random.uniform(min_range, max_range)


def create_population():
	"""
	Ovde kreiramo populaciju prvi put
	:return: vektor jedinki koje smo kreirali
	"""
	population = []
	for i in range(population_size):
		individual = Individual()
		population.append(individual)
	return population


def calculate_fitness(population):
	"""
	Računamo fitness za svaku jedinku u populaciji. U ovom funkciji pozivamo neuronsku mrežu
	:param population: vektor jedinki
	:return: vektor jedinki sa fitness-om
	"""
	for individual in population:
		individual.calculate_fitness()
	return population


def selection(population):
	"""
	Koristimo elitizam za selekciju roditelja za sledecu generaciju
	:param population: vektor jedinki
	:return: vektor jedinki koji ce biti u sledecoj generaciji
	"""

	graded = sorted(population)
	retain_length = int(len(graded) * 0.2)

	parents = graded[:retain_length]

	# ovde ispod su ubačene ostale nasumično izabrane jedinke
	random_select = 0.08
	for individual in graded[retain_length:]:
		if random_select > random():
			parents.append(individual)

	return parents


def crossover(parents):
	"""
	Ovde biramo dve jedinke da nam budu roditelji i ukrštamo im karakteristike iz vektora težina.
	Ovo radimo tako što uzimamo jednu po jednu karakteristiku iz vektora svakog od roditelja i za vrednost deteta
	uzimamo neku vrednost u opsegu izmedju dve vrednosti roditelja.
	Na primer, ako je prva vrednost iz vektora 1. roditelja 20, a prva vrednost iz vektora 2. roditelja 40. Dete može da za tu karakteristiku
	ima vrednost između 20 i 40.
	:param parents: vektor jedinki
	:return: vektor nove populacije koja je sledeća generacija
	"""
	parents_length = len(parents)
	desired_length = population_size - parents_length
	children = []
	while len(children) < desired_length:
		val1 = randint(0, parents_length - 1)
		val2 = randint(0, parents_length - 1)
		if val1 != val2:
			parent1 = parents[val1]
			parent2 = parents[val2]
			child = Individual()
			counter = 0
			for i, j in zip(parent1.characteristics, parent2.characteristics):
				if i < j:
					val = np.random.uniform(i, j)
					child.characteristics[counter] = val
				else:
					val = np.random.uniform(j, i)
					child.characteristics[counter] = val
				counter += 1
			child.calculate_fitness()
			children.append(child)

	# radimo mutaciju nad nekom decom
	for child in children:
		child.mutate()

	new_population = parents
	new_population.extend(children)

	shuffle(new_population)
	return new_population


def begin_evolution(population):
	parents = selection(population)
	new_population = crossover(parents)
	return new_population


def main():
	population = create_population()
	counter = 1
	start = time.time()
	for generation in range(generation_max):
		print("GENERACIJA " + str(counter))
		population = calculate_fitness(population)
		population = begin_evolution(population)
		temp = population
		temp = sorted(temp)
		print(temp[0])
		counter += 1

	sortedd = sorted(population)
	end = time.time()
	print("Minimum funkcije je: " + str(sortedd[0].fitness))
	# print("Vektor karakteristika je: " + str(sortedd[0].characteristics))
	print("Vreme izvrsavanja za 50 generacija je: " + str(end - start))


if __name__ == '__main__':
	main()
