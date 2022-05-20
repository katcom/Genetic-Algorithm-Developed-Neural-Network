import random
import unittest
from Genome import Genome
from Creature import Creature
from Reproducer import Reproducer
class GenomeTest(unittest.TestCase):
    def test_genome_not_none(self):
        gen = Genome(3)
        self.assertIsNotNone(gen.genes)
    def test_Genome_Length(self):
        gen = Genome(3)
        self.assertEqual(len(gen.genes),3)
    def test_invalid_genome_length_2(self):
        gen = Genome(2)
        self.assertEqual(len(gen.genes),2)
    def test_invalid_genome_length_1(self):
        with self.assertRaises(Exception):
            gen = Genome(1)
class CreatureTest(unittest.TestCase):
    def test_creature_has_genome(self):
        gen = Genome();
        gen.genes = [[0,2],[1,2]]
        creature = Creature(gen)
        self.assertIsNotNone(creature.genome)
    def test_model_created_successful(self):
        gen = Genome();
        gen.genes = [[0,2],[1,2]]
        creature = Creature(gen)
        self.assertEqual(len(creature.model.layers),0)
    def test_model_built_successful(self):
        gen = Genome();
        gen.genes = [[0,2],[1,2]]
        creature = Creature(gen)
        creature.develop(1024)
        self.assertNotEqual(len(creature.model.layers),0)

class ReproducerTest(unittest.TestCase):
    def test_select_max_creature_successfully(self):
        reproducer = Reproducer({'a':1,'b':2,'c':3,'d':4},2)
        max_id = reproducer.select_max_creature_id(['a','b','d'])
        self.assertEqual(max_id,'d')
    def test_select_max_creature_failed(self):
        reproducer = Reproducer({'a':1,'b':2,'c':3,'d':4},2)
        max_id = reproducer.select_max_creature_id(['a','b','d'])
        self.assertNotEqual(max_id,'a')
    def test_select_successfully(self):
        reproducer = Reproducer({'a':1,'b':2,'c':3,'d':4},2)
        random.seed(10)
        max_id = reproducer.select()
        self.assertEqual(max_id,'b')
if __name__ == '__main__':
    unittest.main()