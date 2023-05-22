import unittest
from unittest import TestCase, mock

from src.settings import *
from src.bird import Bird
from src.floor import Floor
from src.pipe import Pipe
from src.utils_fun import collide

"""
Run tests with:
python -m unittest tests.py
"""


class TestBird(TestCase):
    
    def test_bird_move(self):
        x, y = 10, 10
        bird = Bird(x, y)
        bird.move() # should staying in place
        self.assertEqual(bird.x, x)


    def test_bird_jump(self):
        x, y = 10, 10
        bird = Bird(x, y)
        bird.jump()
        self.assertEqual(bird.velocity, bird_jump_velocity)


class TestFloor(TestCase):
    
    def test_floor_move(self):
        y = 10
        floor = Floor(y)
        x = floor.x3
        floor.move()
        self.assertLess(floor.x3, x)


class TestPipe(TestCase):
    
    def test_pipe_move(self):
        x = 10
        pipe = Pipe(x)
        pipe.move()
        self.assertLess(pipe.x, x)


class TestCollide(TestCase):
    
    def test_collide_funtion(self):
        global SCREEN
        x, y = 10, 10
        bird = Bird(x, y)
        floor = Floor(y)
        pipe = Pipe(x)
        self.assertTrue( collide(bird, pipe, floor, SCREEN) )


    
if __name__ == '__main__':
    unittest.main()
