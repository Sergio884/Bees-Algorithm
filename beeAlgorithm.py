from bees_algorithm import BeesAlgorithm

def hypersphere(x):
    y = -sum([pow(xi,2) for xi in x])
    return y

search_boundaries=([-5,-5,-5,-5], [5,5,5,5])
alg = BeesAlgorithm(hypersphere,search_boundaries[0],search_boundaries[1])

#alg.performSingleStep()
alg.performFullOptimisation(max_iteration=5000)

best = alg.best_solution
print(best.score) # is the score of the best solution (e.g. 0.0 in our case)
print(best.values) # are the coordinates of the best solution (e.g. [0.0, 0.0, 0.0, 0.0] in our case)