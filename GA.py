import Environment
import random
import Creature
import Genome
import Reproducer
import numpy as np
class Population():
    def __init__(self,pop_size=3):
        self.population = [Creature.Creature(Genome.Genome(2)) for i in range(pop_size)]
        self.pop_table = {}
        for creature in self.population:
            self.pop_table[str(creature)]=creature
        print(self.pop_table)
    def get_creature(self,id):
        return self.pop_table[id]
    def add_creature(self,creature):
        self.pop_table[str(creature)] = creature
        self.population.append(creature)

def get_fittest(performance_dict):
    max_cr = ''
    max_score = -1000
    for cr,score in performance_dict.items():
        if score > max_score:
            max_cr=cr
    return max_cr
num_of_generation=1


env = Environment.Environment(population=[])
pop = Population()
performance_dict = {}
mae_dict={}
for i in range(num_of_generation):
    for cr in pop.population:
        res = env.developCreature(cr)
        avg_mae = [np.mean([x[i] for x in res['mae']]) for i in range(8)]
        print(avg_mae)
        final_score = avg_mae[-1:][0]
        print(final_score)
        performance_dict[str(cr)] = 1/(final_score - res['runtime']/10000)
        mae_dict[str(cr)]=final_score
    # reproducer = Reproducer.Reproducer(performance_dict,2)
    # new_cr = reproducer.select()
    # reproducer.point_mutate(new_cr)
    # pop.add_creature(new_cr)
    print(mae_dict)
    print(performance_dict)
    fittest = get_fittest(performance_dict)
    f_cr = pop.get_creature(fittest)
    print('fittest:',f_cr,', score: ',performance_dict[fittest],'\n','NN:',f_cr.genome.genes)

# cr = Creature.Creature(Genome.Genome(2))
# cr.develop(train_data_shape=[1024,128])
# print(cr.model.summary())

    