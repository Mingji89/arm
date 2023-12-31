# encoding=utf8
# This is temporary fix to import module from parent folder
# It will be removed when package is published on PyPI
import sys

sys.path.append('../')
# End of fix
from niapy.task import Task
from Problem.Griewank import Griewank
from Problem.fitness_process import clear, show, show_all
from niapy.algorithms.basic import ArtificialBeeColonyAlgorithm
from niapy.algorithms.basic.ga import uniform_crossover, uniform_mutation
from niapy.algorithms.basic import ParticleSwarmAlgorithm
from niapy.algorithms.basic import GreyWolfOptimizer
from niapy.algorithms.basic import GeneticAlgorithm
from niapy.algorithms.basic import DifferentialEvolution
from niapy.algorithms.basic import BatAlgorithm


algo_list = ['PSO', 'ABC', 'GWO', 'GA', 'DE', 'BA']

x = 9
Pso = ParticleSwarmAlgorithm(population_size=x, min_velocity=-4.0, max_velocity=4.0)
abc = ArtificialBeeColonyAlgorithm(population_size=x, limit=2)
gwo = GreyWolfOptimizer(population_size=x)
ga = GeneticAlgorithm(population_size=x, crossover=uniform_crossover, mutation=uniform_mutation, crossover_rate=0.45,
                      mutation_rate=0.9)
de = DifferentialEvolution(population_size=x, differential_weight=0.5, crossover_probability=0.9)
ba = BatAlgorithm(population_size=x)


run = [Pso, abc, gwo, ga, de, ba]
# print(algo_list[run.index(Pso)])

for times in range(10):
    clear(algo_list, times)
    for i in run:
        task = Task(problem=Griewank(dimension=x, upper=100, lower=1, algo=algo_list[run.index(i)], times=times),
                    max_evals=100)
        best = i.run(task=task)
        print('%s -> %f' % (best[0], best[1]))
    # show(algo_list, times)
show_all(algo_list, 10)
