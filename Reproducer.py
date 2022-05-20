from calendar import c
import random
from select import select


class Reproducer():
    def __init__(self,performance_table,k):
        self.performance_table=performance_table
        self.k = k
    def select(self):

        creatures = []
        keys = list(self.performance_table.keys())
        creature_indices= random.sample(range(0, len(keys)), self.k)
        #print(keys)
        for index in creature_indices:
            creature_id =keys[index]
            creatures.append(creature_id)
        #print(creatures)

        max_id = self.select_max_creature_id(creatures)
        #print('select: ',max_id)
        return max_id
    def select_max_creature_id(self,creatures):
        max_creature_id = ''
        max_score =0
        for creature_id in creatures:
            if max_score < self.performance_table[creature_id]:
                max_creature_id = creature_id
                max_score = self.performance_table[creature_id]
        return max_creature_id
    def point_mutate(self,creature):
        pos = random.randint(1,len(creature.genes)-1)
        creature.genes[pos][1]=random.randint(3,7)
# reproducer = Reproducer({'a':1,'b':2,'c':3,'d':4},2)
# reproducer.select()