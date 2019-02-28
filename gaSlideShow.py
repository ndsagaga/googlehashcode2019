import random


from Read import read
from Score import score

import Print




def cxPartialyMatched(ind1, ind2):
    """Executes a partially matched crossover (PMX) on the input individuals.
    The two individuals are modified in place. This crossover expects
    :term:`sequence` individuals of indices, the result for any other type of
    individuals is unpredictable.
    :param ind1: The first individual participating in the crossover.
    :param ind2: The second individual participating in the crossover.
    :returns: A tuple of two individuals.
    Moreover, this crossover generates two children by matching
    pairs of values in a certain range of the two parents and swapping the values
    of those indexes. For more details see [Goldberg1985]_.
    This function uses the :func:`~random.randint` function from the python base
    :mod:`random` module.
    .. [Goldberg1985] Goldberg and Lingel, "Alleles, loci, and the traveling
       salesman problem", 1985.
    """
    size = min(len(ind1), len(ind2))
    p1, p2 = [0]*size, [0]*size

    # Initialize the position of each indices in the individuals
    for i in range(size):
        p1[ind1[i].photos[0] -1] = i
        p2[ind2[i].photos[0] -1] = i
    # Choose crossover points
    cxpoint1 = random.randint(0, size)
    cxpoint2 = random.randint(0, size - 1)
    if cxpoint2 >= cxpoint1:
        cxpoint2 += 1
    else: # Swap the two cx points
        cxpoint1, cxpoint2 = cxpoint2, cxpoint1

    # Apply crossover between cx points
    for i in range(cxpoint1, cxpoint2):
        # Keep track of the selected values
        temp1 = ind1[i]
        temp2 = ind2[i]
        # Swap the matched value
        ind1[i], ind1[p1[temp2.photos[0] -1]] = temp2, temp1
        ind2[i], ind2[p2[temp1.photos[0] -1]] = temp1, temp2
        # Position bookkeeping
        p1[temp1.photos[0] -1], p1[temp2.photos[0] -1] = p1[temp2.photos[0] -1], p1[temp1.photos[0] -1]
        p2[temp1.photos[0] -1], p2[temp2.photos[0] -1] = p2[temp2.photos[0] -1], p2[temp1.photos[0] -1]

    return ind1, ind2


def mutInd(individual):
    """Simple Swap mutation"""

    if random.random() < 0.5:
        point1 = random.randint(0, len(individual)-1)
        point2 = random.randint(0, len(individual)-1)
        individual[point1], individual[point2] = individual[point2], individual[point1]







def matePopulation(population):
    while len(population) < 10:
        point1 = random.randint(0, len(population) -1)
        point2 = random.randint(0, len(population) -1)
        c1, c2 = cxPartialyMatched(population[point1], population[point2])
        population = population + [c1] + [c2] + [random.shuffle(population[0])]


def mutatePopulation(population):
    for i in range(0, len(population)):
        mutInd(population[i])


def removeWeak(population):
    scoreID = []

    for i in range(0, len(population)):
        s = score(population[i])
        print(s)
        scoreID.append([population[i], score(population[i])])
    scoreID.sort(key=lambda tup: tup[1], reverse=True)
    survivors = []
    print(str(scoreID[0][1]) + " ..." + str(scoreID[len(scoreID)-1][1]))
    for i in range(0, 5):
        if i < len(population):
            survivors.append(scoreID[i][0])

    return survivors, scoreID[0][1], scoreID[0][0]


def run(population):
    generation = 1
    best = 0.0
    bestSol = None
    while generation < 6 and best < 9999:
        newPop, score, solution = removeWeak(population)

        print("Generation Score:" + str(score))
        population = newPop
        if score > best:
            best = score
            bestSol = solution
        print("Best " + str(best))
        print("Generation: " + str(generation))
        mutatePopulation(population)
        matePopulation(population)
        generation = generation + 1

    Print.print_slides(bestSol)


if __name__ == "__main__":
    main()